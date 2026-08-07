import streamlit as st

from styles import load_css
from kpi import *

st.set_page_config(
    page_title="Enterprise Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================

st.markdown(
"""
<div class='title'>
Enterprise Sales Executive Dashboard
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='subtitle'>
Live SQL Server Analytics Powered by Python
</div>
""",
unsafe_allow_html=True
)

st.divider()

# ============================================
# KPI ROW
# ============================================

col1,col2,col3,col4,col5,col6 = st.columns(6)

with col1:

    st.markdown(f"""
    <div class='kpi-card'>
    <div class='kpi-title'>Revenue</div>
    <div class='kpi-value'>₦{get_total_revenue()/1000000:,.2f}M</div>
    </div>
    """,unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class='kpi-card'>
    <div class='kpi-title'>Profit</div>
    <div class='kpi-value'>₦{get_total_profit()/1000000:,.2f}M</div>
    </div>
    """,unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class='kpi-card'>
    <div class='kpi-title'>Orders</div>
    <div class='kpi-value'>{get_total_orders():,}</div>
    </div>
    """,unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class='kpi-card'>
    <div class='kpi-title'>Customers</div>
    <div class='kpi-value'>{get_total_customers():,}</div>
    </div>
    """,unsafe_allow_html=True)

with col5:

    st.markdown(f"""
    <div class='kpi-card'>
    <div class='kpi-title'>Average Order</div>
    <div class='kpi-value'>₦{get_average_order():,.0f}</div>
    </div>
    """,unsafe_allow_html=True)

with col6:

    st.markdown(f"""
    <div class='kpi-card'>
    <div class='kpi-title'>Gross Margin</div>
    <div class='kpi-value'>{get_gross_margin():.2%}</div>
    </div>
    """,unsafe_allow_html=True)

st.divider()

st.info("✅ Dashboard Shell Completed Successfully")

st.write("Next step: Interactive Charts")