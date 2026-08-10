from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)


def generate_insights(df):

    insights = []

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    margin = get_gross_margin(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)

    # Revenue

    if revenue > 80_000_000:
        insights.append(
            (
                "🟢 Revenue is performing strongly.",
                f"Current revenue is ₦{revenue:,.2f}."
            )
        )
    else:
        insights.append(
            (
                "🟡 Revenue requires attention.",
                f"Current revenue is ₦{revenue:,.2f}."
            )
        )

    # Profit

    if profit > 25_000_000:
        insights.append(
            (
                "🟢 Profit is healthy.",
                f"Profit currently stands at ₦{profit:,.2f}."
            )
        )
    else:
        insights.append(
            (
                "🔴 Profit needs improvement.",
                f"Profit is ₦{profit:,.2f}."
            )
        )

    # Margin

    insights.append(
        (
            "📈 Gross Margin",
            f"Current margin is {margin:.2%}."
        )
    )

    # Orders

    insights.append(
        (
            "🛒 Orders Processed",
            f"{orders:,} orders have been completed."
        )
    )

    # Customers

    insights.append(
        (
            "👥 Customer Base",
            f"The business currently serves {customers:,} customers."
        )
    )

    return insights