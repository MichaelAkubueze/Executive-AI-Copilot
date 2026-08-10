import streamlit as st

from engines.digital_twin_engine import simulate_business

from utils.formatter import millions


def render_digital_twin(df):

    st.subheader("🏢 Executive Digital Twin")

    c1, c2, c3 = st.columns(3)

    with c1:

        marketing = st.slider(
            "Marketing Investment %",
            0,
            30,
            5,
        )

    with c2:

        pricing = st.slider(
            "Pricing Increase %",
            -10,
            20,
            2,
        )

    with c3:

        savings = st.slider(
            "Cost Reduction %",
            0,
            25,
            3,
        )

    result = simulate_business(
        df,
        marketing,
        pricing,
        savings,
    )

    a, b, c = st.columns(3)

    with a:

        st.metric(
            "Projected Revenue",
            millions(result["Revenue"])
        )

    with b:

        st.metric(
            "Projected Profit",
            millions(result["Profit"])
        )

    with c:

        st.metric(
            "Projected ROI",
            f"{result['ROI']:.2f}%"
        )

    d, e = st.columns(2)

    with d:

        st.metric(
            "Projected Customers",
            f"{result['Customers']:,.0f}"
        )

    with e:

        st.metric(
            "Projected Orders",
            f"{result['Orders']:,.0f}"
        )