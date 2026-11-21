import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = "FitPlanner AI"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash-lite"
    )

    MAX_WORKOUT_DAYS = 7
    MIN_WORKOUT_DAYS = 1

    FITNESS_GOALS = [
        "Build muscle",
        "Lose fat",
        "General fitness",
        "Improve endurance"
    ]

    EXPERIENCE_LEVELS = [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

    EQUIPMENT_OPTIONS = [
        "No equipment",
        "Home dumbbells",
        "Full gym"
    ]