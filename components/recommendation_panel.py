import streamlit as st

from advisor import generate_recommendation
from insights import executive_summary


def render_recommendations(df):

    st.markdown("## 🧠 Executive Intelligence")

    col1, col2 = st.columns([3,2])

    with col1:

        st.markdown("### Executive Summary")

        st.info(
            executive_summary(df)
        )

    with col2:

        st.markdown("### AI Recommendation")

        st.success(
            generate_recommendation(df)
        )