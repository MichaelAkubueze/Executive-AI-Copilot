import streamlit as st

from engines.scenario_engine import simulate


def render_simulator(df):

    st.subheader("🎯 Executive Scenario Simulator")

    growth = st.slider(

        "Revenue Growth %",

        -30,

        50,

        10,

    )

    savings = st.slider(

        "Expense Reduction %",

        0,

        40,

        5,

    )

    result = simulate(

        df,

        growth,

        savings,

    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(

            "Projected Revenue",

            f"₦{result['Revenue']:,.0f}"

        )

    with c2:

        st.metric(

            "Projected Profit",

            f"₦{result['Profit']:,.0f}"

        )