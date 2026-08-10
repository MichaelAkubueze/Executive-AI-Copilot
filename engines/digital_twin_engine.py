from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
)


def simulate_business(
    df,
    marketing=0,
    pricing=0,
    operating_cost=0,
):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    customers = get_total_customers(df)
    orders = get_total_orders(df)

    # Marketing Effect
    customer_growth = marketing * 0.6

    customers = customers * (1 + customer_growth / 100)

    orders = orders * (1 + customer_growth / 100)

    # Pricing Effect
    revenue = revenue * (1 + pricing / 100)

    # Operating Cost Reduction
    profit = profit * (
        1
        + pricing / 100
        + operating_cost / 100
    )

    roi = (profit / revenue) * 100 if revenue else 0

    return {

        "Revenue": revenue,

        "Profit": profit,

        "Customers": customers,

        "Orders": orders,

        "ROI": roi,

    }