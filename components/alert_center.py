import streamlit as st

from kpi import *

from analytics import *

from targets import (
    load_targets,
    revenue_target,
    profit_target,
)


def render_alerts(df):

    targets = load_targets()

    alerts = []

    # -----------------------------
    # Revenue
    # -----------------------------

    revenue = get_total_revenue(df)

    rev_target = revenue_target(targets)

    if revenue < rev_target:

        alerts.append(
            (
                "🔴 Revenue Alert",
                f"Revenue is ₦{rev_target-revenue:,.0f} below target."
            )
        )

    else:

        alerts.append(
            (
                "🟢 Revenue",
                "Revenue target achieved."
            )
        )

    # -----------------------------
    # Profit
    # -----------------------------

    profit = get_total_profit(df)

    prof_target = profit_target(targets)

    if profit < prof_target:

        alerts.append(
            (
                "🟠 Profit Alert",
                "Profit is below expected target."
            )
        )

    else:

        alerts.append(
            (
                "🟢 Profit",
                "Profit target achieved."
            )
        )

    # -----------------------------
    # Margin
    # -----------------------------

    margin = get_gross_margin(df)

    if margin < 0.25:

        alerts.append(
            (
                "🔴 Margin Alert",
                "Gross Margin below 25%."
            )
        )

    # -----------------------------
    # Customer Growth
    # -----------------------------

    growth = customer_growth(df)

    if growth < 0:

        alerts.append(
            (
                "🟠 Customer Growth",
                "Customer base is shrinking."
            )
        )

    elif growth < 0.03:

        alerts.append(
            (
                "🟡 Customer Growth",
                "Customer growth is slow."
            )
        )

    else:

        alerts.append(
            (
                "🟢 Customer Growth",
                "Healthy customer growth."
            )
        )

    # -----------------------------

    st.markdown("## 🚨 Executive Alert Center")

    for title, message in alerts:

        if "🔴" in title:

            st.error(f"**{title}**\n\n{message}")

        elif "🟠" in title:

            st.warning(f"**{title}**\n\n{message}")

        elif "🟡" in title:

            st.warning(f"**{title}**\n\n{message}")

        else:

            st.success(f"**{title}**\n\n{message}")