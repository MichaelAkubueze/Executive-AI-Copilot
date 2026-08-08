import streamlit as st

from gauges import executive_gauge

from targets import (
    load_targets,
    revenue_target,
    profit_target,
    order_target,
    customer_target,
)

from kpi import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
)


def render_gauges(df):

    targets = load_targets()

    g1, g2, g3, g4 = st.columns(4)

    with g1:
        st.plotly_chart(
            executive_gauge(
                "Revenue Achievement",
                get_total_revenue(df),
                revenue_target(targets),
            ),
            use_container_width=True,
        )

    with g2:
        st.plotly_chart(
            executive_gauge(
                "Profit Achievement",
                get_total_profit(df),
                profit_target(targets),
                "#10B981",
            ),
            use_container_width=True,
        )

    with g3:
        st.plotly_chart(
            executive_gauge(
                "Orders Achievement",
                get_total_orders(df),
                order_target(targets),
                "#F59E0B",
            ),
            use_container_width=True,
        )

    with g4:
        st.plotly_chart(
            executive_gauge(
                "Customer Achievement",
                get_total_customers(df),
                customer_target(targets),
                "#8B5CF6",
            ),
            use_container_width=True,
        )