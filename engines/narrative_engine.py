from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)

from engines.target_engine import get_target


def generate_narrative(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)
    margin = get_gross_margin(df)

    revenue_target = get_target("Revenue")

    achievement = 0

    if revenue_target > 0:
        achievement = revenue / revenue_target * 100

    # Revenue Status
    if achievement >= 90:
        revenue_comment = (
            "Revenue performance is excellent and is approaching target."
        )

    elif achievement >= 70:
        revenue_comment = (
            "Revenue performance is healthy but remains below target."
        )

    else:
        revenue_comment = (
            "Revenue requires immediate management attention."
        )

    # Margin Status
    if margin >= 0.30:
        margin_comment = (
            "Profit margin remains strong."
        )
    else:
        margin_comment = (
            "Profit margin should be improved."
        )

    narrative = f"""
Revenue reached ₦{revenue:,.2f},
representing {achievement:.1f}% achievement
against the planned target.

Profit currently stands at
₦{profit:,.2f}.

The organisation processed
{orders:,} customer orders
while serving
{customers:,} customers.

Gross margin is currently
{margin:.2%}.

{revenue_comment}

{margin_comment}

Overall business outlook remains positive.
"""

    return narrative.strip()