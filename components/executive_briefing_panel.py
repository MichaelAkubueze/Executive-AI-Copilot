import streamlit as st

from engines.executive_engine import executive_briefing


def render_executive_briefing(df):

    st.subheader("📰 Executive Morning Briefing")

    st.info(executive_briefing(df))