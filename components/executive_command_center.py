import streamlit as st

from engines.executive_engine import (
    business_health,
    executive_alerts,
    executive_briefing,
)


def render_command_center(df):

    st.title("🎯 Executive Command Center")

    health = business_health(df)

    alerts = executive_alerts(df)

    briefing = executive_briefing(df)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Business Health",
            f"{health['score']:.1f}%"
        )

    with c2:

        if health["revenue_score"] >= 90:
            risk = "🟢 Low"
        elif health["revenue_score"] >= 75:
            risk = "🟠 Medium"
        else:
            risk = "🔴 High"

        st.metric(
            "Revenue Risk",
            risk,
        )

    with c3:

        confidence = round(
            (health["score"] + health["margin_score"]) / 2,
            1,
        )

        st.metric(
            "Forecast Confidence",
            f"{confidence}%",
        )

    st.divider()

    st.subheader("📰 Executive Briefing")

    st.markdown(briefing)

    st.divider()

    st.subheader("🚨 Executive Alerts")

    for icon, message in alerts:

        if icon == "🔴":
            st.error(message)

        elif icon == "🟠":
            st.warning(message)

        else:
            st.success(message)