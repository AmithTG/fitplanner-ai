
import pytest

from utils.validators import (
    validate_user_inputs,
    validate_workout_plan
)


def test_valid_user_inputs():

    validate_user_inputs(
        fitness_goal="Build muscle",
        experience_level="Beginner",
        days_per_week=3,
        equipment="No equipment",
        injuries=""
    )


def test_invalid_fitness_goal():

    with pytest.raises(ValueError):

        validate_user_inputs(
            fitness_goal="Become superhuman",
            experience_level="Beginner",
            days_per_week=3,
            equipment="No equipment",
            injuries=""
        )


def test_invalid_workout_days():

    with pytest.raises(ValueError):

        validate_user_inputs(
            fitness_goal="Build muscle",
            experience_level="Beginner",
            days_per_week=0,
            equipment="No equipment",
            injuries=""
        )


def test_invalid_equipment():

    with pytest.raises(ValueError):

        validate_user_inputs(
            fitness_goal="Build muscle",
            experience_level="Beginner",
            days_per_week=3,
            equipment="Unknown equipment",
            injuries=""
        )


def test_valid_workout_plan():

    plan = {
        "plan_title": "Beginner Workout",
        "summary": "A beginner workout plan.",
        "weekly_schedule": [
            {
                "day": "Monday",
                "focus": "Full Body",
                "warmup": "Walk for five minutes.",
                "exercises": [
                    {
                        "name": "Bodyweight Squat",
                        "sets": "3",
                        "reps": "10",
                        "rest": "60 seconds",
                        "instructions": "Perform a controlled squat."
                    }
                ],
                "cooldown": "Gentle stretching."
            }
        ],
        "recovery_tips": ["Get adequate sleep."],
        "progression_tips": ["Increase repetitions gradually."],
        "safety_disclaimer": "Exercise within your abilities."
    }

    validate_workout_plan(
        plan=plan,
        days_per_week=1
    )


def test_wrong_number_of_workout_days():

    plan = {
        "plan_title": "Test",
        "summary": "Test plan",
        "weekly_schedule": [],
        "recovery_tips": ["Rest"],
        "progression_tips": ["Progress gradually"],
        "safety_disclaimer": "Exercise carefully."
    }

    with pytest.raises(ValueError):

        validate_workout_plan(
            plan=plan,
            days_per_week=3
        )
