import streamlit as st

from copilot import ExecutiveCopilot


def render_copilot(df):

    st.info(
        "💡 Ask the Executive AI about your business performance."
    )

    assistant = ExecutiveCopilot(df)

    # ----------------------------
    # Session History
    # ----------------------------

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # ----------------------------
    # User Question
    # ----------------------------

    question = st.text_input(
        "Ask a business question",
        placeholder="Example: Best Region"
    )

    # ----------------------------
    # Ask Button
    # ----------------------------

    if st.button("Ask AI"):

        if question.strip() != "":

            answer = assistant.ask(question)

            st.session_state.chat_history.append(
                (question, answer)
            )

    # ----------------------------
    # Conversation History
    # ----------------------------

    if st.session_state.chat_history:

        st.markdown("### Conversation")

        for q, a in reversed(st.session_state.chat_history):

            with st.chat_message("user"):
                st.write(q)

            with st.chat_message("assistant"):
                st.success(a)