import streamlit as st

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_customers,
    get_gross_margin,
    customer_growth,
)

from targets import (
    get_target,
    achievement,
    variance,
    status,
)

from utils.currency import format_currency
from utils.numbers import format_number


# ==========================================================
# EXECUTIVE ALERT CENTER
# ==========================================================

def render_alerts(df):

    alerts = []

    # ------------------------------------------------------
    # Revenue
    # ------------------------------------------------------

    revenue = get_total_revenue(df)
    target = get_target("Revenue")

    if achievement(revenue, target) < 85:

        alerts.append({

            "priority": "🔴 CRITICAL",

            "title": "Revenue Target",

            "message":
                f"Revenue is "
                f"{format_currency(abs(variance(revenue, target)))} "
                f"below target.",

            "status": status(revenue, target)

        })

    # ------------------------------------------------------
    # Profit
    # ------------------------------------------------------

    profit = get_total_profit(df)
    target = get_target("Profit")

    if achievement(profit, target) < 85:

        alerts.append({

            "priority": "🟠 HIGH",

            "title": "Profit Target",

            "message":
                f"Profit is "
                f"{format_currency(abs(variance(profit, target)))} "
                f"below target.",

            "status": status(profit, target)

        })

    # ------------------------------------------------------
    # Gross Margin
    # ------------------------------------------------------

    margin = get_gross_margin(df)

    if margin < 0.25:

        alerts.append({

            "priority": "🟠 HIGH",

            "title": "Gross Margin",

            "message":
                f"Gross Margin is only {margin:.2%}.",

            "status": "Watch"

        })

    # ------------------------------------------------------
    # Customers
    # ------------------------------------------------------

    customers = get_total_customers(df)
    target = get_target("Customers")

    if achievement(customers, target) < 90:

        alerts.append({

            "priority": "🟡 MEDIUM",

            "title": "Customer Target",

            "message":
                f"Only {format_number(customers)} customers recorded "
                f"against target of {format_number(target)}.",

            "status": status(customers, target)

        })

    # ------------------------------------------------------
    # Customer Growth
    # ------------------------------------------------------

    growth = customer_growth(df)

    if growth < 0:

        alerts.append({

            "priority": "🔴 CRITICAL",

            "title": "Customer Growth",

            "message": "Customer base is shrinking.",

            "status": "Critical"

        })

    elif growth < 0.03:

        alerts.append({

            "priority": "🟡 MEDIUM",

            "title": "Customer Growth",

            "message": "Customer growth is slower than expected.",

            "status": "Watch"

        })

    # ------------------------------------------------------
    # Render
    # ------------------------------------------------------

    st.markdown("### 🚨 Executive Alert Center")

    if len(alerts) == 0:

        st.success("✅ No executive alerts detected.")

        return

    for alert in alerts:

        text = f"""
**{alert['priority']} — {alert['title']}**

{alert['message']}

**Status:** {alert['status']}
"""

        if "CRITICAL" in alert["priority"]:

            st.error(text)

        elif "HIGH" in alert["priority"]:

            st.warning(text)

        else:

            st.info(text)
            
            