import streamlit as st

from engines.recommendation_engine import generate_recommendations


def render_recommendations(df):

    recommendations = generate_recommendations(df)

    for rec in recommendations:

        if rec["priority"] == "High":
            st.error(
                f"### 🔴 {rec['title']}\n\n{rec['action']}"
            )

        elif rec["priority"] == "Medium":
            st.warning(
                f"### 🟡 {rec['title']}\n\n{rec['action']}"
            )

        else:
            st.success(
                f"### 🟢 {rec['title']}\n\n{rec['action']}"
            )