import streamlit as st

from database import load_sales_data
from components.sidebar import render_sidebar
from engines.forecast_ai import generate_forecast_insights
from reports.forecast_report import create_forecast_report

from engines.forecast_engine import (
    forecast_next_month,
    forecast_growth,
    forecast_status,
    executive_forecast,
)

from components.forecast_charts import (
    revenue_forecast_chart,
    profit_forecast_chart,
    orders_forecast_chart,
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Forecasting",
    page_icon="🔮",
    layout="wide",
)


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("🔮 Forecasting Analytics")

st.caption(
    "Enterprise Revenue, Profit and Order Forecasting"
)


# ==========================================================
# LOAD DATA
# ==========================================================

df = load_sales_data()

df = render_sidebar(df)


# ==========================================================
# FORECAST CALCULATION
# ==========================================================

forecast = forecast_next_month(df)

growth = forecast_growth(df)

status = forecast_status(df)


# ==========================================================
# FORECAST KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)


with k1:

    st.metric(
        "Expected Revenue",
        f"₦{forecast['Revenue']:,.0f}",
    )


with k2:

    st.metric(
        "Expected Profit",
        f"₦{forecast['Profit']:,.0f}",
    )


with k3:

    st.metric(
        "Expected Orders",
        f"{forecast['Orders']:,.0f}",
    )


with k4:

    st.metric(
        "Revenue Growth",
        f"{growth:.2f}%",
    )


# ==========================================================
# FORECAST STATUS
# ==========================================================

st.divider()

st.subheader("📊 Forecast Outlook")

st.info(
    f"""
### Forecast Status

**{status}**

The forecast is based on the current
three-month moving average methodology.

Expected Revenue:
**₦{forecast['Revenue']:,.2f}**

Expected Profit:
**₦{forecast['Profit']:,.2f}**

Expected Orders:
**{forecast['Orders']:,.0f}**

Recent Revenue Growth:
**{growth:.2f}%**
"""
)


# ==========================================================
# REVENUE FORECAST
# ==========================================================

st.divider()

st.subheader("📈 Revenue Forecast")

st.plotly_chart(
    revenue_forecast_chart(df),
    use_container_width=True,
)


# ==========================================================
# PROFIT FORECAST
# ==========================================================

st.divider()

st.subheader("💰 Profit Forecast")

st.plotly_chart(
    profit_forecast_chart(df),
    use_container_width=True,
)


# ==========================================================
# ORDERS FORECAST
# ==========================================================

st.divider()

st.subheader("📦 Orders Forecast")

st.plotly_chart(
    orders_forecast_chart(df),
    use_container_width=True,
)


# ==========================================================
# EXECUTIVE FORECAST SUMMARY
# ==========================================================

st.divider()

st.subheader("📋 Executive Forecast Summary")

st.markdown(
    executive_forecast(df)
)

# ==========================================================
# AI FORECAST INTELLIGENCE
# ==========================================================

st.divider()

st.subheader("🧠 AI Forecast Intelligence")

forecast_insight = generate_forecast_insights(df)

left, right = st.columns([2, 1])


# ==========================================================
# AI FORECAST SUMMARY
# ==========================================================

with left:

    st.success(
        f"""
### Forecast Executive Summary

📈 Expected Revenue:
**₦{forecast_insight['Revenue']:,.0f}**

💰 Expected Profit:
**₦{forecast_insight['Profit']:,.0f}**

📦 Expected Orders:
**{forecast_insight['Orders']:,.0f}**

🎯 Revenue Growth:
**{forecast_insight['Growth']:.2f}%**

📊 Forecast Profit Margin:
**{forecast_insight['Margin']:.2f}%**

🔮 Forecast Status:
**{forecast_insight['Status']}**

### Business Outlook

{forecast_insight['Outlook']}
"""
    )


# ==========================================================
# AI RECOMMENDATIONS
# ==========================================================

with right:

    st.markdown(
        "### 🎯 Forecast Recommendations"
    )

    for recommendation in forecast_insight[
        "Recommendations"
    ]:

        st.markdown(
            f"- {recommendation}"
        )
# ==========================================================
# FORECAST EXECUTIVE REPORT
# ==========================================================

st.divider()

st.subheader("📄 Forecast Executive Report")

if st.button("Generate Forecast Executive Report"):

    report = create_forecast_report(
        forecast_insight,
        df,
        forecast
    )

    st.success(
        "Forecast Executive Report Generated Successfully!"
    )

    with open(report, "rb") as pdf:

        st.download_button(
            label="⬇ Download Forecast Executive Report",
            data=pdf,
            file_name=report,
            mime="application/pdf",
        )
        