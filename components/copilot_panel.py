import streamlit as st

from engines.copilot_engine import (
    executive_summary,
    answer_question,
)


def render_copilot(df):

    st.info(executive_summary(df))

    question = st.text_input(
    "💬 Ask Executive Copilot",
    placeholder="Why is revenue below target?",
    key="executive_copilot_question"
)

    if question:

        answer = answer_question(
            df,
            question,
        )

        st.success(answer)