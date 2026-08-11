import streamlit as st
from datetime import datetime


def render_header():

    col1, col2 = st.columns([5, 2])

    with col1:

        st.title("📊 Enterprise Sales Analytics Platform")

        st.caption(
            "Executive Decision Intelligence System"
        )

    with col2:

        st.metric(
            "Report Date",
            datetime.now().strftime("%d %b %Y"),
        )

        st.caption(
            datetime.now().strftime("%I:%M %p")
        )

    st.divider()