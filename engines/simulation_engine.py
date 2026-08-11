def simulate_business(
    revenue,
    profit,
    orders,
    customers,
    revenue_growth=0,
    profit_growth=0,
    order_growth=0,
    customer_growth=0,
):

    new_revenue = revenue * (1 + revenue_growth / 100)

    new_profit = profit * (1 + profit_growth / 100)

    new_orders = orders * (1 + order_growth / 100)

    new_customers = customers * (1 + customer_growth / 100)

    margin = (
        (new_profit / new_revenue) * 100
        if new_revenue
        else 0
    )

    return {

        "Revenue": new_revenue,

        "Profit": new_profit,

        "Orders": new_orders,

        "Customers": new_customers,

        "Margin": margin,

    }