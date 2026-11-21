
from typing import Any

import streamlit as st

from utils.formatter import format_workout_plan


def display_workout_plan(
    plan: dict[str, Any]
) -> None:
    """
    Display the personalized workout plan.
    """

    st.success("Your personalized workout plan is ready!")

    st.header(f"💪 {plan['plan_title']}")

    st.write(plan["summary"])

    st.divider()

    st.subheader("📅 Weekly Workout Schedule")

    for day in plan["weekly_schedule"]:

        with st.expander(
            f"🏋️ {day['day']} | {day['focus']}",
            expanded=True
        ):

            st.markdown("### 🔥 Warm-up")

            st.write(day["warmup"])

            st.markdown("### 💪 Exercises")

            for index, exercise in enumerate(
                day["exercises"],
                start=1
            ):

                st.markdown(
                    f"**{index}. {exercise['name']}**"
                )

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Sets",
                    exercise["sets"]
                )

                col2.metric(
                    "Repetitions",
                    exercise["reps"]
                )

                col3.metric(
                    "Rest",
                    exercise["rest"]
                )

                st.caption(exercise["instructions"])

                st.divider()

            st.markdown("### 🧘 Cool-down")

            st.write(day["cooldown"])

    # Recovery and progression.
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🌿 Recovery Tips")

        for tip in plan["recovery_tips"]:
            st.markdown(f"- {tip}")

    with col2:

        st.subheader("📈 Progression Tips")

        for tip in plan["progression_tips"]:
            st.markdown(f"- {tip}")

    # Safety information.
    st.divider()

    st.subheader("⚠️ Safety Information")

    st.info(plan["safety_disclaimer"])

    # Download Markdown.
    markdown_content = format_workout_plan(plan)

    st.download_button(
        label="📥 Download Workout Plan",
        data=markdown_content,
        file_name="my_workout_plan.md",
        mime="text/markdown",
        use_container_width=True
    )
