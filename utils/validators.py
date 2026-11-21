
from typing import Any

from config.settings import Settings


def validate_user_inputs(
    fitness_goal: str,
    experience_level: str,
    days_per_week: int,
    equipment: str,
    injuries: str
) -> None:
    """
    Validate all structured user inputs.
    """

    if fitness_goal not in Settings.FITNESS_GOALS:
        raise ValueError("Please select a valid fitness goal.")

    if experience_level not in Settings.EXPERIENCE_LEVELS:
        raise ValueError("Please select a valid experience level.")

    if equipment not in Settings.EQUIPMENT_OPTIONS:
        raise ValueError("Please select valid equipment access.")

    if (
        not isinstance(days_per_week, int)
        or isinstance(days_per_week, bool)
        or not Settings.MIN_WORKOUT_DAYS <= days_per_week
        <= Settings.MAX_WORKOUT_DAYS
    ):
        raise ValueError("Workout days must be between 1 and 7.")

    if not isinstance(injuries, str):
        raise ValueError("Invalid injury or limitation information.")


def validate_workout_plan(
    plan: dict[str, Any],
    days_per_week: int
) -> None:
    """
    Validate the JSON response returned by Groq.
    """

    if not isinstance(plan, dict):
        raise ValueError("The AI returned an invalid plan.")

    required_fields = [
        "plan_title",
        "summary",
        "weekly_schedule",
        "recovery_tips",
        "progression_tips",
        "safety_disclaimer"
    ]

    for field in required_fields:
        if field not in plan:
            raise ValueError(f"Missing information: {field}")

    for field in [
        "plan_title",
        "summary",
        "safety_disclaimer"
    ]:
        if not isinstance(plan[field], str) or not plan[field].strip():
            raise ValueError(f"Invalid information in {field}.")

    schedule = plan["weekly_schedule"]

    if not isinstance(schedule, list):
        raise ValueError("Invalid weekly workout schedule.")

    if len(schedule) != days_per_week:
        raise ValueError(
            f"Expected {days_per_week} workout sessions, "
            f"but received {len(schedule)}."
        )

    required_day_fields = [
        "day",
        "focus",
        "warmup",
        "exercises",
        "cooldown"
    ]

    required_exercise_fields = [
        "name",
        "sets",
        "reps",
        "rest",
        "instructions"
    ]

    for day in schedule:

        if not isinstance(day, dict):
            raise ValueError("Invalid workout session.")

        for field in required_day_fields:
            if field not in day:
                raise ValueError(
                    f"Workout session is missing {field}."
                )

            if not isinstance(day[field], str) and field != "exercises":
                raise ValueError(f"Invalid workout field: {field}")

            if field != "exercises" and not day[field].strip():
                raise ValueError(f"Empty workout field: {field}")

        exercises = day["exercises"]

        if not isinstance(exercises, list) or not exercises:
            raise ValueError("A workout must contain exercises.")

        for exercise in exercises:

            if not isinstance(exercise, dict):
                raise ValueError("Invalid exercise information.")

            for field in required_exercise_fields:

                if field not in exercise:
                    raise ValueError(
                        f"Exercise is missing information: {field}"
                    )

                value = exercise[field]

                if not isinstance(value, (str, int, float)):
                    raise ValueError(
                        f"Invalid exercise information: {field}"
                    )

                if not str(value).strip():
                    raise ValueError(
                        f"Empty exercise information: {field}"
                    )

    for field in ["recovery_tips", "progression_tips"]:

        if (
            not isinstance(plan[field], list)
            or not plan[field]
            or not all(
                isinstance(tip, str) and tip.strip()
                for tip in plan[field]
            )
        ):
            raise ValueError(f"Invalid {field} information.")
