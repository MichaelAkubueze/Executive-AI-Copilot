import streamlit as st

from engines.insights_engine import generate_insights


def render_insights(df):

    insights = generate_insights(df)

    st.subheader("💡 Executive Insights")

    for title, text in insights:

        with st.container():

            st.markdown(
                f"""
**{title}**

{text}
"""
            )

            st.divider()
            
            