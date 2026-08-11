import streamlit as st

from engines.scenario_engine import simulate


def render_simulator(df):

    st.subheader("🎯 Executive Scenario Simulator")

    st.caption(
        "Model different business scenarios and instantly evaluate their financial impact."
    )

    # ==========================================================
    # SCENARIO INPUTS
    # ==========================================================

    col1, col2 = st.columns(2)

    with col1:

        revenue_growth = st.slider(
            "📈 Revenue Growth (%)",
            -30,
            50,
            10,
            key="revenue_growth",
        )

        expense_reduction = st.slider(
            "💰 Expense Reduction (%)",
            0,
            40,
            5,
            key="expense_reduction",
        )

    with col2:

        customer_growth = st.slider(
            "👥 Customer Growth (%)",
            -20,
            40,
            5,
            key="customer_growth",
        )

        order_growth = st.slider(
            "🛒 Order Growth (%)",
            -20,
            40,
            5,
            key="order_growth",
        )

    # ==========================================================
    # RUN SIMULATION
    # ==========================================================

    result = simulate(
        df,
        revenue_growth,
        expense_reduction,
        customer_growth,
        order_growth,
    )

    st.divider()

    # ==========================================================
    # PROJECTED KPI CARDS
    # ==========================================================

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "💰 Projected Revenue",
            f"₦{result['Revenue']:,.0f}",
        )

    with c2:

        st.metric(
            "📈 Projected Profit",
            f"₦{result['Profit']:,.0f}",
        )

    c3, c4 = st.columns(2)

    with c3:

        st.metric(
            "📊 Projected Margin",
            f"{result['Margin']:.2f}%",
        )

    with c4:

        st.metric(
            "🏢 Business Health",
            f"{result['BusinessHealth']:.1f}%",
        )

    st.divider()

    # ==========================================================
    # AI EXECUTIVE STRATEGY
    # ==========================================================

    health = result["BusinessHealth"]

    if health >= 90:

        st.success(
            """
### 🟢 AI Executive Recommendation

This scenario is **HIGHLY RECOMMENDED**.

Expected Benefits

• Significant revenue improvement

• Strong profit growth

• Healthy business outlook

• Low execution risk

Recommendation

Proceed with implementation.
"""
        )

    elif health >= 75:

        st.info(
            """
### 🟠 AI Executive Recommendation

This scenario is **VIABLE**.

Expected Benefits

• Moderate business growth

• Profit improvement

• Stable performance

Recommendation

Proceed while closely monitoring KPIs.
"""
        )

    else:

        st.warning(
            """
### 🔴 AI Executive Recommendation

This scenario carries **HIGH BUSINESS RISK**.

Concerns

• Low projected business health

• Weak financial outlook

• Increased execution risk

Recommendation

Review assumptions before implementation.
"""
        )

    # ==========================================================
    # EXECUTIVE SUMMARY
    # ==========================================================

    st.divider()

    st.subheader("🧠 Executive Scenario Summary")

    st.write(
        f"""
If revenue grows by **{revenue_growth}%**, expenses reduce by **{expense_reduction}%**,
customers increase by **{customer_growth}%**, and orders increase by **{order_growth}%**:

- Revenue is projected to become **₦{result['Revenue']:,.0f}**
- Profit is projected to become **₦{result['Profit']:,.0f}**
- Gross Margin is projected to reach **{result['Margin']:.2f}%**
- Overall Business Health becomes **{result['BusinessHealth']:.1f}%**
"""
    )