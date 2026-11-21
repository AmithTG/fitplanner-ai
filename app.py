
import streamlit as st

from config.settings import Settings
from services.workout_service import generate_workout_plan
from components.workout_display import display_workout_plan


# PAGE CONFIGURATION

st.set_page_config(
    page_title="FitPlanner AI",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)


# SESSION STATE INITIALIZATION

if "workout_plan" not in st.session_state:
    st.session_state.workout_plan = None

if "user_inputs" not in st.session_state:
    st.session_state.user_inputs = None

if "variation" not in st.session_state:
    st.session_state.variation = 0


# CUSTOM CSS

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        [data-testid="stSidebar"] {
            background-color: #f1f5f9;
        }

        .stButton button[kind="primary"] {
            background-color: #2563eb;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# HEADER

st.title("💪 FitPlanner AI")

st.markdown(
    """
    Your personal AI fitness coach.

    Generate personalized weekly workout plans based on
    your fitness goals, experience and available equipment.
    """
)

st.divider()


# SIDEBAR

with st.sidebar:

    st.title("💪 FitPlanner AI")

    st.divider()

    st.subheader("How it works")

    st.markdown(
        """
        1. Enter your fitness information.
        2. Select your fitness goal.
        3. Choose your available equipment.
        4. Mention any physical limitations.
        5. Generate your personalized workout plan.
        """
    )

    st.divider()

    st.subheader("Features")

    st.markdown(
        """
        - Personalized workout plans
        - Equipment-based exercises
        - Experience-level adjustments
        - Injury-aware recommendations
        - Weekly workout schedules
        - Downloadable workout plans
        """
    )

    st.divider()

    st.caption(
        "Powered by Python, Streamlit and Google Gemini API."
    )


# USER INPUT FORM

st.subheader("👤 Tell Us About Yourself")

with st.form("workout_form"):

    col1, col2 = st.columns(2)

    # Personal fitness information
    with col1:

        fitness_goal = st.selectbox(
            "🎯 Fitness Goal",
            options=Settings.FITNESS_GOALS
        )

        experience_level = st.selectbox(
            "📊 Experience Level",
            options=Settings.EXPERIENCE_LEVELS
        )

        days_per_week = st.slider(
            "📅 Days Available Per Week",
            min_value=1,
            max_value=7,
            value=3
        )

    # Equipment and physical limitations
    with col2:

        equipment = st.selectbox(
            "🏋️ Equipment Access",
            options=Settings.EQUIPMENT_OPTIONS
        )

        injuries = st.text_area(
            "⚠️ Injuries or Physical Limitations (Optional)",
            placeholder=(
                "Example: Bad knees, lower back discomfort, "
                "no overhead pressing..."
            ),
            height=130
        )

    submitted = st.form_submit_button(
        "🚀 Generate My Workout Plan",
        type="primary",
        use_container_width=True
    )


# GENERATE WORKOUT PLAN

if submitted:

    # Save user inputs in session state
    st.session_state.user_inputs = {
        "fitness_goal": fitness_goal,
        "experience_level": experience_level,
        "days_per_week": days_per_week,
        "equipment": equipment,
        "injuries": injuries
    }

    # Reset variation for a new plan
    st.session_state.variation = 0

    # Clear previous plan
    st.session_state.workout_plan = None

    try:

        with st.spinner(
            "🤖 Your AI fitness coach is preparing your workout plan..."
        ):

            plan = generate_workout_plan(
                **st.session_state.user_inputs,
                variation=0
            )

            st.session_state.workout_plan = plan

        st.success("Your workout plan has been generated!")

    except ValueError as error:

        st.error(str(error))

    except RuntimeError as error:

        st.error("Gemini API request failed.")

        with st.expander("View technical error details"):
            st.exception(error)

    except Exception as error:

        st.error("Something unexpected happened. Please try again.")

        with st.expander("View technical error details"):
            st.exception(error)


# REGENERATE WORKOUT PLAN

if st.session_state.user_inputs:

    st.divider()

    if st.button(
        "🔄 Regenerate Workout Plan",
        use_container_width=True,
        disabled=st.session_state.workout_plan is None
    ):

        try:

            with st.spinner(
                "Creating another personalized workout variation..."
            ):

                next_variation = st.session_state.variation + 1

                plan = generate_workout_plan(
                    **st.session_state.user_inputs,
                    variation=next_variation
                )

                st.session_state.workout_plan = plan
                st.session_state.variation = next_variation

            st.success("A new workout variation is ready!")

        except ValueError as error:

            st.error(str(error))

        except RuntimeError as error:

            st.error("Gemini API request failed during regeneration.")

            with st.expander("View technical error details"):
                st.exception(error)

        except Exception as error:

            st.error("Something went wrong while regenerating your plan.")

            with st.expander("View technical error details"):
                st.exception(error)


# DISPLAY GENERATED WORKOUT PLAN

if st.session_state.workout_plan:

    st.divider()

    display_workout_plan(
        st.session_state.workout_plan
    )


# FOOTER

st.divider()

st.caption(
    """
    FitPlanner AI | Built using Python, Streamlit and Google Gemini.

    This application provides general fitness information,
    not medical advice. Consult a qualified healthcare
    professional before exercising with an injury or
    medical condition.
    """
)
