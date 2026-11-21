
import json
import logging
from typing import Any

from google import genai
from google.genai import types

from config.settings import Settings
from prompts.workout_prompts import build_workout_prompts
from utils.validators import (
    validate_user_inputs,
    validate_workout_plan
)

logger = logging.getLogger(__name__)


def generate_workout_plan(
    fitness_goal: str,
    experience_level: str,
    days_per_week: int,
    equipment: str,
    injuries: str = "",
    variation: int = 0
) -> dict[str, Any]:

    # Validate user inputs
    validate_user_inputs(
        fitness_goal=fitness_goal,
        experience_level=experience_level,
        days_per_week=days_per_week,
        equipment=equipment,
        injuries=injuries
    )

    if (
        not isinstance(variation, int)
        or isinstance(variation, bool)
        or variation < 0
    ):
        raise ValueError("Invalid workout variation.")

    if not Settings.GEMINI_API_KEY:
        raise ValueError(
            "Gemini API key is missing. Check your .env file."
        )

    if not Settings.GEMINI_MODEL:
        raise ValueError(
            "Gemini model is not configured."
        )

    # Build prompts
    system_prompt, user_prompt = build_workout_prompts(
        fitness_goal=fitness_goal,
        experience_level=experience_level,
        days_per_week=days_per_week,
        equipment=equipment,
        injuries=injuries,
        variation=variation
    )

    # Call Gemini API
    try:
        print("\n========== GEMINI REQUEST ==========")
        print("Model:", Settings.GEMINI_MODEL)
        print("Goal:", fitness_goal)
        print("Experience:", experience_level)
        print("Days:", days_per_week)
        print("Equipment:", equipment)
        print("Variation:", variation)
        print("====================================\n")

        client = genai.Client(
            api_key=Settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model=Settings.GEMINI_MODEL,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.5,
                max_output_tokens=6000,
                response_mime_type="application/json"
            )
        )

        content = response.text

    except Exception as error:
        logger.exception("Gemini API request failed")

        raise RuntimeError(
            f"Gemini API request failed: {error}"
        ) from error

    # Check Gemini response
    if not content or not content.strip():
        raise ValueError(
            "Gemini returned an empty response. Please try again."
        )

    print("\n========== GEMINI RAW RESPONSE ==========")
    print(content)
    print("=========================================\n")

    # Parse JSON response
    try:
        plan = json.loads(content)

    except json.JSONDecodeError as error:
        logger.exception("Gemini returned invalid JSON")

        raise ValueError(
            f"Gemini returned invalid JSON: {error}"
        ) from error

    # Validate generated workout plan
    try:
        validate_workout_plan(
            plan=plan,
            days_per_week=days_per_week
        )

    except Exception as error:
        logger.exception("Workout plan validation failed")

        raise ValueError(
            f"Generated workout plan failed validation: {error}"
        ) from error

    print("\nWorkout plan generated and validated successfully.")

    return plan
