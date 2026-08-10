import streamlit as st

from engines.copilot_engine import ask_copilot


def render_ai_copilot(df):

    st.subheader("🤖 Executive AI Copilot")

    question = st.text_input(
        "Ask a business question",
        placeholder="Example: Why did revenue drop?",
    )

    if st.button("Ask AI"):

        answer = ask_copilot(question, df)

        st.success(answer)