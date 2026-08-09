import streamlit as st

from copilot import ask_copilot


def render_copilot(df):

    st.markdown("## 🤖 Executive AI Copilot")

    question = st.text_input(
        "Ask a business question"
    )

    if question:

        answer = ask_copilot(question, df)

        st.success(answer)