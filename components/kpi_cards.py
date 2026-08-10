import streamlit as st

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_average_order,
    get_gross_margin,
    get_mom_growth,
    get_yoy_growth,
    customer_growth,
    order_growth,
)

from engines.kpi_engine import (
    revenue_achievement,
    profit_achievement,
    orders_achievement,
    customer_achievement,
    margin_achievement,
    performance_status,
)

from components.metric_card import metric_card


# ==========================================================
# ENTERPRISE KPI DASHBOARD
# ==========================================================

def render_kpis(df):

    st.markdown("## 📊 Executive KPI Dashboard")

    # ======================================================
    # KPI ENGINE
    # ======================================================

    revenue_progress = revenue_achievement(df)
    revenue_status, revenue_colour = performance_status(revenue_progress)

    profit_progress = profit_achievement(df)
    profit_status, profit_colour = performance_status(profit_progress)

    orders_progress = orders_achievement(df)
    orders_status, orders_colour = performance_status(orders_progress)

    customer_progress = customer_achievement(df)
    customer_status, customer_colour = performance_status(customer_progress)

    margin_progress = margin_achievement(df)
    margin_status, margin_colour = performance_status(margin_progress)

    # ======================================================
    # ROW 1
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card(

            title="Revenue",

            value=f"₦{get_total_revenue(df)/1_000_000:.2f}M",

            icon="💰",

            trend=f"▲ {get_mom_growth(df)*100:.2f}%",

            target="₦100M",

            progress=revenue_progress,

            badge=revenue_status,

            badge_color=revenue_colour,

        )

    with c2:

        metric_card(

            title="Profit",

            value=f"₦{get_total_profit(df)/1_000_000:.2f}M",

            icon="📈",

            trend=f"▲ {get_yoy_growth(df)*100:.2f}%",

            target="₦30M",

            progress=profit_progress,

            badge=profit_status,

            badge_color=profit_colour,

        )

    with c3:

        metric_card(

            title="Orders",

            value=f"{get_total_orders(df):,}",

            icon="🛒",

            trend=f"▲ {order_growth(df)*100:.2f}%",

            target="12,000",

            progress=orders_progress,

            badge=orders_status,

            badge_color=orders_colour,

        )

    with c4:

        metric_card(

            title="Customers",

            value=f"{get_total_customers(df):,}",

            icon="👥",

            trend=f"▲ {customer_growth(df)*100:.2f}%",

            target="1,200",

            progress=customer_progress,

            badge=customer_status,

            badge_color=customer_colour,

        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ======================================================
    # ROW 2
    # ======================================================

    c5, c6 = st.columns(2)

    with c5:

        metric_card(

            title="Average Order",

            value=f"₦{get_average_order(df):,.2f}",

            icon="💳",

            trend="",

            target="₦8,000",

            progress=85,

            badge="Stable",

            badge_color="#2563EB",

        )

    with c6:

        metric_card(

            title="Gross Margin",

            value=f"{get_gross_margin(df):.2%}",

            icon="📊",

            trend="",

            target="35%",

            progress=margin_progress,

            badge=margin_status,

            badge_color=margin_colour,

        )