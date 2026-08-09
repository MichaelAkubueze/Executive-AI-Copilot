import streamlit as st

from database import load_sales_data

#from styles import load_css
#from theme.css import load_theme
from styles import load_css

from components.header import render_header
from components.sidebar import render_sidebar

from components.kpi_cards import render_kpis
from components.scorecard import render_scorecard
from components.alert_center import render_alerts
from components.gauges_panel import render_gauges
from components.recommendation_panel import render_recommendations
from components.copilot_panel import render_copilot
from components.charts_panel import render_charts
from components.footer import render_footer


# ===========================================================
# PAGE CONFIG
# ===========================================================

st.set_page_config(
    page_title="Enterprise Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

# ===========================================================
# LOAD GLOBAL STYLE
# ===========================================================

#load_css()
#load_theme()
load_css()
# ===========================================================
# LOAD DATA
# ===========================================================

sales_df = load_sales_data()

sales_df = render_sidebar(sales_df)

# ===========================================================
# HEADER
# ===========================================================

render_header()

#st.divider()

# ===========================================================
# EXECUTIVE KPI SECTION
# ===========================================================

st.subheader("📊 Executive Dashboard")
st.caption("Real-time Business Performance Overview")

render_kpis(sales_df)
#
st.markdown("<br>", unsafe_allow_html=True)
#
# ===========================================================
# EXECUTIVE PERFORMANCE
# ===========================================================

left, right = st.columns([2, 1])

with left:

    st.subheader("🎯 Executive Performance")

    #render_scorecard(sales_df)

with right:

    st.subheader("🚨 Executive Alerts")

    #render_alerts(sales_df)

st.divider()

# ===========================================================
# GAUGES
# ===========================================================

st.subheader("📈 Target Achievement")

#render_gauges(sales_df)

st.divider()

# ===========================================================
# AI RECOMMENDATION
# ===========================================================

st.subheader("🧠 AI Executive Recommendation")

#render_recommendations(sales_df)

st.divider()

# ===========================================================
# AI COPILOT
# ===========================================================

st.subheader("🤖 Executive AI Copilot")

#render_copilot(sales_df)

st.divider()

# ===========================================================
# EXECUTIVE ANALYTICS
# ===========================================================

st.subheader("📉 Executive Analytics")

#render_charts(sales_df)

st.divider()

# ===========================================================
# FOOTER
# ===========================================================

#render_footer()