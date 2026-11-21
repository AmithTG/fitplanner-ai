# 💪 FitPlanner AI - Workout Plan Generator

An AI-powered workout plan generator built using Python, Streamlit, and the Google Gemini API.

FitPlanner AI creates personalized weekly workout plans based on the user's fitness goals, experience level, available training days, equipment, and physical limitations.

## Features

- Personalized workout plans using Google Gemini AI.
- Four fitness goals.
- Three experience levels.
- Flexible workout schedules from 1 to 7 days.
- Equipment-based exercise recommendations.
- Optional injury and limitation information.
- Day-by-day workout schedules.
- Exercise sets, repetitions, and rest periods.
- Warm-up and cool-down recommendations.
- Recovery and progression tips.
- Regenerate workout plans.
- Download plans in Markdown format.
- Input and response validation.
- API error handling.

## Technology Stack

- Python 3.11+
- Streamlit
- Google Gemini API
- Google Gen AI SDK (`google-genai`)
- Gemini Flash model
- JSON
- Pytest

## Project Structure

```text
fitplanner-ai/
│
├── app.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── services/
│   ├── __init__.py
│   └── workout_service.py
├── prompts/
│   ├── __init__.py
│   └── workout_prompts.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   └── formatter.py
├── components/
│   ├── __init__.py
│   └── workout_display.py
├── tests/
│   ├── __init__.py
│   └── test_validators.py
├── .streamlit/
│   └── config.toml
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fitplanner-ai.git
cd fitplanner-ai
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.8-flash
```

Replace `your_gemini_api_key` with your Google Gemini API key.

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Important:** Never commit or share your `.env` file or API key.

### 5. Run the application

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Run Tests

```bash
pytest -v
```

## Prompt Engineering

The application uses a detailed system prompt and structured user prompt to generate personalized workout plans.

The system prompt defines the AI's role, exercise selection requirements, equipment restrictions, experience-level adjustments, safety requirements, and JSON response format.

The user prompt passes structured fitness information, including fitness goals, experience level, workout frequency, available equipment, and physical limitations, to Gemini.

The application requests structured JSON output to ensure consistency and simplify response validation.

## Error Handling

The application handles:

- Missing API credentials.
- Invalid user inputs.
- Gemini API failures.
- Empty AI responses.
- Malformed or incomplete JSON.
- Incomplete workout plans.
- Incorrect workout session counts.

## Safety Disclaimer

The generated workout plans provide general fitness information and are not medical advice.

Users with injuries or medical conditions should seek guidance from qualified healthcare professionals before starting an exercise program.

## Author

Amith

## License

Created for educational purposes.