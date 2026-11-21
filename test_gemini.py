
from google import genai
from config.settings import Settings

print("Checking Gemini configuration...")

# Check API key
if not Settings.GEMINI_API_KEY:
    print("ERROR: Gemini API key is missing!")
    raise SystemExit(1)

print("API key found:", Settings.GEMINI_API_KEY[:5] + "*****")

# Check model
print("Configured model:", repr(Settings.GEMINI_MODEL))

try:
    client = genai.Client(
        api_key=Settings.GEMINI_API_KEY
    )

    print("\nTesting Gemini API connection...")

    response = client.models.generate_content(
        model=Settings.GEMINI_MODEL,
        contents="Create a simple 3-day beginner muscle-building workout plan."
    )

    print("\nSUCCESS! Gemini API is working.")
    print("\nGemini response:")
    print(response.text)

except Exception as error:
    print("\nGEMINI API FAILED")
    print("Error type:", type(error).__name__)
    print("Error details:", error)
