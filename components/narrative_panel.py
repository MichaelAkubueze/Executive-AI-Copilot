import streamlit as st

from engines.narrative_engine import generate_narrative


def render_narrative(df):

    st.subheader("🧠 Executive Narrative")

    narrative = generate_narrative(df)

    st.info(narrative)