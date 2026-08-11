import streamlit as st

from database import load_sales_data
from styles import load_css

from components.insights_panel import render_insights
from components.forecast_panel import render_forecast
from components.simulator_panel import render_simulator
from components.digital_twin_panel import render_digital_twin
from components.board_report_panel import render_board_report
from components.narrative_panel import render_narrative
from components.executive_health_panel import render_business_health
from components.executive_alert_panel import render_executive_alerts
from components.executive_briefing_panel import render_executive_briefing
from components.executive_command_center import render_command_center
from components.opportunity_panel import render_opportunity
from components.risk_panel import render_risk

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
# PAGE CONFIGURATION
# ===========================================================

st.set_page_config(
    page_title="Enterprise Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

# ===========================================================
# LOAD GLOBAL CSS
# ===========================================================

load_css()

# ===========================================================
# LOAD DATA
# ===========================================================

#sales_df = load_sales_data()
#render_command_center(sales_df)
sales_df = load_sales_data()
from engines.executive_engine import business_health

#health = business_health(sales_df)

#st.write(health)

# ===========================================================
# SIDEBAR FILTERS
# ===========================================================

sales_df = render_sidebar(sales_df)

# ===========================================================
# HEADER
# ===========================================================

render_header()

# ===========================================================
# EXECUTIVE COMMAND CENTER
# ===========================================================

render_command_center(sales_df)

st.divider()


# ===========================================================
# EXECUTIVE DASHBOARD
# ===========================================================

st.subheader("📊 Executive Dashboard")
st.caption("Real-time Business Performance Overview")

render_kpis(sales_df)
render_insights(sales_df)
render_narrative(sales_df)
render_opportunity(sales_df)
render_risk(sales_df)
st.divider()
render_business_health(sales_df)
render_executive_alerts(sales_df)
render_executive_briefing(sales_df)
st.divider()

# ===========================================================
# SCORECARD & ALERTS
# ===========================================================

left, right = st.columns([2, 1])

with left:
    render_scorecard(sales_df)

with right:
    render_alerts(sales_df)

st.divider()

# ===========================================================
# TARGET ACHIEVEMENT
# ===========================================================

st.subheader("📈 Target Achievement")
render_gauges(sales_df)

st.divider()

# ===========================================================
# AI RECOMMENDATIONS
# ===========================================================

st.subheader("🧠 AI Executive Recommendation")
render_recommendations(sales_df)
render_forecast(sales_df)
render_digital_twin(sales_df)
st.divider()

render_board_report(sales_df)
render_simulator(sales_df)

st.divider()

# ===========================================================
# EXECUTIVE COPILOT
# ===========================================================

st.subheader("🤖 Executive AI Copilot")
render_copilot(sales_df)

st.divider()

# ===========================================================
# EXECUTIVE ANALYTICS
# ===========================================================

render_charts(sales_df)

st.divider()

# ===========================================================
# FOOTER
# ===========================================================

render_footer()