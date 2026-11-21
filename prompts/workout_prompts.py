
from typing import Tuple


def build_workout_prompts(
    fitness_goal: str,
    experience_level: str,
    days_per_week: int,
    equipment: str,
    injuries: str = "",
    variation: int = 0
) -> Tuple[str, str]:
    """
    Build personalized system and user prompts
    for Gemini workout plan generation.
    """

    system_prompt = """
You are FitPlanner AI, an experienced fitness programming
assistant specializing in personalized workout planning.

Your responsibility is to create practical, structured,
goal-oriented and safe weekly workout plans.

PERSONALIZATION RULES:

1. FITNESS GOALS

- Build muscle:
  Prioritize resistance training, balanced muscle development,
  appropriate training volume and progressive overload.

- Lose fat:
  Combine resistance training with suitable cardiovascular
  activities. Never promise specific fat-loss results.

- General fitness:
  Balance strength training, cardiovascular fitness and mobility.

- Improve endurance:
  Prioritize cardiovascular conditioning and gradual progression.

2. EXPERIENCE LEVEL

- Beginner:
  Recommend simple exercises, manageable training volume,
  appropriate rest and clear exercise instructions.

- Intermediate:
  Recommend moderate training volume, exercise variations
  and structured progression.

- Advanced:
  Recommend appropriately challenging exercises,
  structured programming and progressive overload.

3. EQUIPMENT RESTRICTIONS

- No equipment:
  Use bodyweight exercises only.

- Home dumbbells:
  Use dumbbell and bodyweight exercises only.

- Full gym:
  Barbells, dumbbells, cables, resistance machines
  and bodyweight exercises are allowed.

Never recommend equipment that the user does not have.

4. INJURIES AND PHYSICAL LIMITATIONS

- Treat all reported limitations as important constraints.
- Avoid exercises that directly conflict with reported limitations.
- Suggest alternatives where appropriate.
- Do not diagnose medical conditions.
- Do not recommend medical treatment.
- Do not claim that an exercise is medically safe.
- If a limitation is unclear or potentially serious,
  recommend assessment by a qualified healthcare professional.

5. WORKOUT SCHEDULE

- Generate EXACTLY the requested number of workout sessions.
- Use different weekdays for each session.
- Include appropriate recovery between demanding sessions.
- Do not count recovery days as workout sessions.
- Distribute training volume sensibly across the week.

6. WORKOUT SESSION STRUCTURE

Every workout session MUST contain:

- day
- focus
- warmup
- exercises
- cooldown

Every exercise MUST contain:

- name
- sets
- reps
- rest
- instructions

Use realistic sets, repetitions and rest periods.

7. RECOVERY AND PROGRESSION

Include practical recovery recommendations.

Explain progressive overload in simple language.

Encourage gradual increases in repetitions or resistance
while maintaining proper exercise technique.

Avoid excessive training volume and unrealistic schedules.

8. OUTPUT QUALITY

- Personalize the plan using every provided user input.
- Avoid generic exercise lists.
- Use clear, simple and actionable language.
- Provide a balanced workout plan.
- Ensure all exercises match the available equipment.
- Ensure the number of workout sessions is exact.

9. JSON OUTPUT REQUIREMENTS

Return ONLY one valid JSON object.

Use double quotes for all keys and string values.

Do not include Markdown code fences.

Do not include comments or additional text.

Do not omit any required fields.

Do not return null values for required fields.

The weekly_schedule must contain exactly the requested
number of workout sessions.

The exercises field must be a non-empty array.

All required exercise fields must be present.

REQUIRED JSON STRUCTURE:

{
    "plan_title": "Personalized Workout Plan",
    "summary": "Explanation of the personalized plan",
    "weekly_schedule": [
        {
            "day": "Monday",
            "focus": "Workout focus",
            "warmup": "Warm-up instructions",
            "exercises": [
                {
                    "name": "Exercise name",
                    "sets": "3",
                    "reps": "10-12",
                    "rest": "60 seconds",
                    "instructions": "Exercise instructions"
                }
            ],
            "cooldown": "Cool-down instructions"
        }
    ],
    "recovery_tips": [
        "Recovery tip"
    ],
    "progression_tips": [
        "Progression tip"
    ],
    "safety_disclaimer": "Safety information"
}
"""

    limitation = (
        injuries.strip()
        if injuries and injuries.strip()
        else "None reported"
    )

    user_prompt = f"""
Create a personalized weekly workout plan using the
following user information.

USER FITNESS PROFILE
--------------------

Fitness Goal: {fitness_goal}

Experience Level: {experience_level}

Available Workout Days Per Week: {days_per_week}

Available Equipment: {equipment}

Injuries or Physical Limitations: {limitation}

Workout Variation Number: {variation}


PERSONALIZATION REQUIREMENTS
----------------------------

1. Generate EXACTLY {days_per_week} workout sessions.

2. Prioritize the user's selected fitness goal:
   {fitness_goal}

3. Adjust exercise difficulty and training volume to:
   {experience_level}

4. Use only the equipment available:
   {equipment}

5. Respect all reported physical limitations:
   {limitation}

6. Include appropriate warm-ups and cool-downs.

7. Provide exercise names, sets, repetitions,
   rest periods and clear instructions.

8. Include practical recovery recommendations.

9. Include progressive overload recommendations.

10. Distribute workout sessions sensibly across the week.

11. Avoid repeating the same workout unnecessarily.

12. Make the plan realistic and achievable.

13. If injuries or limitations are reported,
    include an appropriate safety disclaimer.


WORKOUT VARIATION
-----------------

Current variation number: {variation}

If the variation number is greater than zero,
create a meaningfully different workout plan.

Change exercise selection, workout focus or organization
where appropriate.

Do not violate equipment restrictions, experience-level
requirements or physical limitations.


FINAL INSTRUCTION
-----------------

Return ONLY the valid JSON object using the exact
required structure from the system instructions.

Do not include Markdown formatting or additional explanations.
"""
    return system_prompt, user_prompt
