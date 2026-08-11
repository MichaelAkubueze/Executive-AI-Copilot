import streamlit as st

from engines.executive_engine import executive_alerts


def render_executive_alerts(df):

    alerts = executive_alerts(df)

    st.subheader("🚨 Executive Alert Center")

    for icon, message in alerts:

        if icon == "🔴":
            st.error(message)

        elif icon == "🟠":
            st.warning(message)

        else:
            st.success(message)
            
def executive_briefing(df):

    health = business_health(df)

    revenue = health["revenue_score"]
    margin = health["margin_score"]
    customers = health["customer_score"]
    orders = health["order_score"]

    focus = []

    if revenue < 80:
        focus.append("Increase revenue in underperforming regions.")

    if customers < 90:
        focus.append("Improve customer acquisition.")

    if orders < 90:
        focus.append("Increase order volume.")

    if margin < 100:
        focus.append("Improve profitability.")

    if not focus:
        focus.append("Maintain current business momentum.")

    briefing = f"""
### Executive Morning Briefing

Business Health is **{health['score']}% ({health['status']})**.

Revenue achievement is **{revenue:.1f}%** of target.

Profit Margin achievement is **{margin:.1f}%**.

Customer achievement is **{customers:.1f}%**.

Order achievement is **{orders:.1f}%**.

### Recommended Management Focus

• {" ".join(focus)}
"""

    return briefing