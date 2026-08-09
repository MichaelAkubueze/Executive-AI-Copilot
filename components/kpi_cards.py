import streamlit as st

from analytics import *

from components.metric_card import metric_card


def render_kpis(df):

    st.markdown("## 📊 Executive KPI Dashboard")
    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card(
            "Revenue",
            f"₦{get_total_revenue(df)/1_000_000:.2f}M",
            icon="💰",
            trend=f"▲ {get_mom_growth(df)*100:.2f}%",
            target="₦100M",
            progress=74,
            badge="Business Growth",
            badge_color="#2563EB",
        )

    with c2:

        metric_card(
            "Profit",
            f"₦{get_total_profit(df)/1_000_000:.2f}M",
            icon="📈",
            trend=f"▲ {get_yoy_growth(df)*100:.2f}%",
            target="₦30M",
            progress=74,
            badge="Healthy",
            badge_color="#10B981",
        )

    with c3:

        metric_card(
            "Orders",
            f"{get_total_orders(df):,}",
            icon="🛒",
            trend=f"▲ {order_growth(df)*100:.2f}%",
            target="12,000",
            progress=83,
            badge="Active",
            badge_color="#F59E0B",
        )

    with c4:

        metric_card(
            "Customers",
            f"{get_total_customers(df):,}",
            icon="👥",
            trend=f"▲ {customer_growth(df)*100:.2f}%",
            target="1,200",
            progress=83,
            badge="Growing",
            badge_color="#8B5CF6",
        )
        
        
        st.markdown("<br>", unsafe_allow_html=True)