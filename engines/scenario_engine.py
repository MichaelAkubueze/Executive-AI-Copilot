from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
)


def simulate(
        df,
        revenue_growth=0,
        expense_reduction=0,
):

    revenue = get_total_revenue(df)

    profit = get_total_profit(df)

    orders = get_total_orders(df)

    customers = get_total_customers(df)

    revenue = revenue * (1 + revenue_growth/100)

    profit = profit * (
        1
        + revenue_growth/100
        + expense_reduction/100
    )

    return {

        "Revenue": revenue,

        "Profit": profit,

        "Orders": orders,

        "Customers": customers,

    }