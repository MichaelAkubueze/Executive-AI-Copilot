from engines.kpi_engine import (
    revenue_achievement,
    profit_achievement,
    orders_achievement,
    customer_achievement,
    margin_achievement,
)


def generate_alerts(df):

    alerts = []

    revenue = revenue_achievement(df)
    profit = profit_achievement(df)
    orders = orders_achievement(df)
    customers = customer_achievement(df)
    margin = margin_achievement(df)

    # Revenue
    if revenue < 60:
        alerts.append({
            "level": "critical",
            "title": "Revenue Target Miss",
            "message": f"Revenue achievement is only {revenue:.1f}%."
        })

    elif revenue < 80:
        alerts.append({
            "level": "warning",
            "title": "Revenue Below Target",
            "message": f"Revenue achievement is {revenue:.1f}%."
        })

    # Profit
    if profit < 60:
        alerts.append({
            "level": "critical",
            "title": "Profit Risk",
            "message": f"Profit achievement is only {profit:.1f}%."
        })

    # Orders
    if orders < 70:
        alerts.append({
            "level": "warning",
            "title": "Low Order Volume",
            "message": f"Orders achieved {orders:.1f}% of target."
        })

    # Customers
    if customers < 70:
        alerts.append({
            "level": "warning",
            "title": "Customer Growth Slow",
            "message": f"Customer target achievement is {customers:.1f}%."
        })

    # Margin
    if margin < 80:
        alerts.append({
            "level": "info",
            "title": "Margin Opportunity",
            "message": f"Gross margin is at {margin:.1f}% of target."
        })

    if len(alerts) == 0:

        alerts.append({

            "level": "success",

            "title": "Excellent Performance",

            "message": "All KPIs are within expected thresholds."

        })

    return alerts