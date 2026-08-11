from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)


def simulate(
    df,
    revenue_growth=0,
    expense_reduction=0,
    customer_growth=0,
    order_growth=0,
):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)

    # Current operating cost
    expenses = revenue - profit

    # Apply scenario assumptions
    projected_revenue = revenue * (1 + revenue_growth / 100)

    projected_expenses = expenses * (1 - expense_reduction / 100)

    projected_profit = projected_revenue - projected_expenses

    projected_orders = orders * (1 + order_growth / 100)

    projected_customers = customers * (1 + customer_growth / 100)

    projected_margin = (
        projected_profit / projected_revenue * 100
        if projected_revenue
        else 0
    )

    # Business Health Score
    health = (
        min(projected_revenue / 100_000_000 * 40, 40)
        + min(projected_margin / 25 * 30, 30)
        + min(projected_customers / 1200 * 15, 15)
        + min(projected_orders / 12000 * 15, 15)
    )

    return {

        "Revenue": projected_revenue,

        "Profit": projected_profit,

        "Orders": projected_orders,

        "Customers": projected_customers,

        "Margin": projected_margin,

        "BusinessHealth": round(health, 1),

    }