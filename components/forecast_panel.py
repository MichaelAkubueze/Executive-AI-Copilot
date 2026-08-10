import streamlit as st

from engines.forecast_engine import (
    executive_forecast,
)


def render_forecast(df):

    st.subheader("🔮 Executive Forecast")

    st.info(

        executive_forecast(df)

    )