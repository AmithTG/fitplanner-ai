
from typing import Any


def format_workout_plan(
    plan: dict[str, Any]
) -> str:
    """
    Convert workout plan JSON into readable Markdown.
    """

    lines = []

    lines.append(f"# {plan['plan_title']}")
    lines.append("")
    lines.append(plan["summary"])
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# Weekly Workout Schedule")
    lines.append("")

    for day in plan["weekly_schedule"]:

        lines.append(f"## {day['day']} - {day['focus']}")
        lines.append("")

        lines.append("### Warm-up")
        lines.append(day["warmup"])
        lines.append("")

        lines.append("### Exercises")

        for index, exercise in enumerate(day["exercises"], 1):

            lines.append(f"#### {index}. {exercise['name']}")
            lines.append(f"- **Sets:** {exercise['sets']}")
            lines.append(f"- **Repetitions:** {exercise['reps']}")
            lines.append(f"- **Rest:** {exercise['rest']}")
            lines.append(
                f"- **Instructions:** {exercise['instructions']}"
            )
            lines.append("")

        lines.append("### Cool-down")
        lines.append(day["cooldown"])
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("# Recovery Tips")
    lines.append("")

    for tip in plan["recovery_tips"]:
        lines.append(f"- {tip}")

    lines.append("")
    lines.append("# Progression Tips")
    lines.append("")

    for tip in plan["progression_tips"]:
        lines.append(f"- {tip}")

    lines.append("")
    lines.append("# Safety Disclaimer")
    lines.append("")
    lines.append(plan["safety_disclaimer"])

    return "\n".join(lines)
