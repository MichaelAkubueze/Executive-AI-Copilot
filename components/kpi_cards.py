import streamlit as st

from kpi import *

from analytics import *

from components.metric_card import metric_card


def render_kpis(df):

    st.markdown("## Executive KPIs")

    row1 = st.columns(4)

    with row1[0]:

        metric_card(

            "Revenue",

            f"₦{get_total_revenue(df)/1000000:,.1f}M",

            "💰",

            round(get_mom_growth(df)*100,2),

            "%",

            "Business Growth",

        )

    with row1[1]:

        metric_card(

            "Profit",

            f"₦{get_total_profit(df)/1000000:,.1f}M",

            "📈",

            round(get_yoy_growth(df)*100,2),

            "%",

            "Healthy",

        )

    with row1[2]:

        metric_card(

            "Orders",

            f"{get_total_orders(df):,}",

            "🛒",

            round(order_growth(df)*100,2),

            "%",

            "Active",

        )

    with row1[3]:

        metric_card(

            "Customers",

            f"{get_total_customers(df):,}",

            "👥",

            round(customer_growth(df)*100,2),

            "%",

            "Growing",

        )

    row2 = st.columns(2)

    with row2[0]:

        metric_card(

            "Average Order",

            f"₦{get_average_order(df):,.0f}",

            "💳",

            None,

            "",

            "Stable",

        )

    with row2[1]:

        metric_card(

            "Gross Margin",

            f"{get_gross_margin(df):.2%}",

            "📊",

            None,

            "",

            "Excellent",

        )