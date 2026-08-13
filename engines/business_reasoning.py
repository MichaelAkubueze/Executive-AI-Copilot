from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)

from engines.executive_engine import business_health


def analyze_business(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)
    margin = get_gross_margin(df)

    health = business_health(df)

    insights = []

    # Revenue vs Target
    if health["revenue_score"] < 75:
        insights.append(
            "Revenue is below target and requires executive attention."
        )
    elif health["revenue_score"] < 95:
        insights.append(
            "Revenue is healthy but still below strategic expectations."
        )
    else:
        insights.append(
            "Revenue target has been achieved."
        )

    # Margin
    if margin >= 25:
        insights.append(
            "Profit margin remains above the company's strategic target."
        )
    else:
        insights.append(
            "Profit margin requires improvement."
        )

    # Orders
    if health["order_score"] < 90:
        insights.append(
            "Order volume is below target."
        )

    # Customers
    if health["customer_score"] < 90:
        insights.append(
            "Customer acquisition can be improved."
        )

    return {
        "Revenue": revenue,
        "Profit": profit,
        "Margin": margin,
        "Orders": orders,
        "Customers": customers,
        "Health": health,
        "Insights": insights,
    }