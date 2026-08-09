import streamlit as st

from gauges import executive_gauge

from targets import get_target

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
)


# ==========================================================
# EXECUTIVE GAUGES
# ==========================================================

def render_gauges(df):

    g1, g2, g3, g4 = st.columns(4)

    with g1:

        st.plotly_chart(

            executive_gauge(

                title="Revenue Achievement",

                actual=get_total_revenue(df),

                target=get_target("Revenue"),

                colour="#2563EB",

            ),

            use_container_width=True,

        )

    with g2:

        st.plotly_chart(

            executive_gauge(

                title="Profit Achievement",

                actual=get_total_profit(df),

                target=get_target("Profit"),

                colour="#10B981",

            ),

            use_container_width=True,

        )

    with g3:

        st.plotly_chart(

            executive_gauge(

                title="Orders Achievement",

                actual=get_total_orders(df),

                target=get_target("Orders"),

                colour="#F59E0B",

            ),

            use_container_width=True,

        )

    with g4:

        st.plotly_chart(

            executive_gauge(

                title="Customer Achievement",

                actual=get_total_customers(df),

                target=get_target("Customers"),

                colour="#8B5CF6",

            ),

            use_container_width=True,

        )
        
        