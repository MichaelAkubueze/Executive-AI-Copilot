import streamlit as st

from engines.alert_engine import generate_alerts


def render_alerts(df):

    alerts = generate_alerts(df)

    for alert in alerts:

        if alert["level"] == "critical":
            st.error(f"🚨 **{alert['title']}**\n\n{alert['message']}")

        elif alert["level"] == "warning":
            st.warning(f"⚠️ **{alert['title']}**\n\n{alert['message']}")

        elif alert["level"] == "info":
            st.info(f"ℹ️ **{alert['title']}**\n\n{alert['message']}")

        else:
            st.success(f"✅ **{alert['title']}**\n\n{alert['message']}")