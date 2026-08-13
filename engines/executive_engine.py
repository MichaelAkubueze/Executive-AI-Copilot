from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)
from engines.target_engine import get_target
from ai_config import (
    DEFAULT_REVENUE_TARGET,
    DEFAULT_CUSTOMER_TARGET,
    DEFAULT_ORDER_TARGET,
    HIGH_MARGIN,
    STATUS_EXCELLENT,
    STATUS_HEALTHY,
    STATUS_WATCH,
    STATUS_CRITICAL,
)
def safe_percent(actual, target):
    """
    Returns achievement percentage capped between 0 and 100.
    """

    if target <= 0:
        return 0

    pct = (actual / target) * 100

    return max(0, min(pct, 100))


def business_health(df):

    # -----------------------------
    # ACTUAL VALUES
    # -----------------------------

    revenue = get_total_revenue(df)

    profit = get_total_profit(df)

    customers = get_total_customers(df)

    orders = get_total_orders(df)

    gross_margin = get_gross_margin(df)

    # -----------------------------
    # TARGETS
    # -----------------------------

    revenue_target = get_target("Revenue") or DEFAULT_REVENUE_TARGET
    profit_margin_target = HIGH_MARGIN
    customer_target = get_target("Customers") or DEFAULT_CUSTOMER_TARGET
    order_target = get_target("Orders") or DEFAULT_ORDER_TARGET

    # -----------------------------
    # KPI ACHIEVEMENTS
    # -----------------------------

    revenue_score = safe_percent(
        revenue,
        revenue_target,
    )

    margin_score = safe_percent(
        gross_margin,
        profit_margin_target,
    )

    customer_score = safe_percent(
        customers,
        customer_target,
    )

    order_score = safe_percent(
        orders,
        order_target,
    )

    # -----------------------------
    # WEIGHTED SCORE
    # -----------------------------

    score = (

        revenue_score * 0.40 +

        margin_score * 0.30 +

        customer_score * 0.15 +

        order_score * 0.15

    )

    score = round(score, 1)

    # -----------------------------
    # STATUS
    # -----------------------------

    if score >= 90:
        status = STATUS_EXCELLENT

    elif score >= 75:
        status = STATUS_HEALTHY

    elif score >= 60:
        status = STATUS_WATCH

    else:
        status = STATUS_CRITICAL

    return {

        "score": score,

        "status": status,

        "revenue_score": round(revenue_score, 1),

        "margin_score": round(margin_score, 1),

        "customer_score": round(customer_score, 1),

        "order_score": round(order_score, 1),

    }
    
    
def executive_alerts(df):

    health = business_health(df)

    alerts = []

    # ---------------------------------
    # Revenue
    # ---------------------------------

    if health["revenue_score"] < 80:

        alerts.append(
            (
                "🔴",
                f"Revenue is only {health['revenue_score']:.1f}% of target."
            )
        )

    elif health["revenue_score"] < 95:

        alerts.append(
            (
                "🟠",
                "Revenue is below target. Monitor closely."
            )
        )

    else:

        alerts.append(
            (
                "🟢",
                "Revenue target is being achieved."
            )
        )

    # ---------------------------------
    # Profit Margin
    # ---------------------------------

    if health["margin_score"] >= 100:

        alerts.append(
            (
                "🟢",
                "Profit margin exceeds target."
            )
        )

    else:

        alerts.append(
            (
                "🟠",
                "Profit margin is below expected level."
            )
        )

    # ---------------------------------
    # Customers
    # ---------------------------------

    if health["customer_score"] < 90:

        alerts.append(
            (
                "🟠",
                "Customer growth requires attention."
            )
        )

    else:

        alerts.append(
            (
                "🟢",
                "Customer acquisition is healthy."
            )
        )

    # ---------------------------------
    # Orders
    # ---------------------------------

    if health["order_score"] < 90:

        alerts.append(
            (
                "🟠",
                "Order volume is below planned target."
            )
        )

    else:

        alerts.append(
            (
                "🟢",
                "Order volume is healthy."
            )
        )

    return alerts

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