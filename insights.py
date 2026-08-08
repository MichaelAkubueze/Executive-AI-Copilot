from kpi import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_average_order,
    get_gross_margin,
)


def executive_summary(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)
    avg_order = get_average_order(df)
    margin = get_gross_margin(df)

    summary = []

    # -------------------------------------------------------
    # Revenue
    # -------------------------------------------------------

    if revenue >= 100_000_000:
        summary.append(
            "Revenue performance is excellent and exceeds the enterprise benchmark."
        )

    elif revenue >= 50_000_000:
        summary.append(
            "Revenue performance is healthy with room for further growth."
        )

    else:
        summary.append(
            "Revenue is below the desired strategic target."
        )

    # -------------------------------------------------------
    # Profit
    # -------------------------------------------------------

    if profit > 0:
        summary.append(
            f"Business generated ₦{profit:,.0f} in profit."
        )

    else:
        summary.append(
            "Business is currently operating at a loss."
        )

    # -------------------------------------------------------
    # Margin
    # -------------------------------------------------------

    if margin >= 0.35:
        summary.append(
            "Profit margin is excellent."
        )

    elif margin >= 0.25:
        summary.append(
            "Profit margin is acceptable."
        )

    else:
        summary.append(
            "Profit margin requires improvement."
        )

    # -------------------------------------------------------
    # Orders
    # -------------------------------------------------------

    summary.append(
        f"{orders:,} customer orders have been processed."
    )

    # -------------------------------------------------------
    # Customers
    # -------------------------------------------------------

    summary.append(
        f"The business currently serves {customers:,} active customers."
    )

    # -------------------------------------------------------
    # Average Order
    # -------------------------------------------------------

    summary.append(
        f"Average Order Value stands at ₦{avg_order:,.0f}."
    )

    return " ".join(summary)