from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)

from engines.kpi_engine import (
    revenue_achievement,
    profit_achievement,
    orders_achievement,
    customer_achievement,
)


def executive_summary(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)
    margin = get_gross_margin(df)

    revenue_pct = revenue_achievement(df)
    profit_pct = profit_achievement(df)
    orders_pct = orders_achievement(df)
    customers_pct = customer_achievement(df)

    summary = f"""
### 📊 Executive Business Summary

Total Revenue:
₦{revenue:,.2f}

Total Profit:
₦{profit:,.2f}

Orders Processed:
{orders:,}

Customers:
{customers:,}

Gross Margin:
{margin:.2%}

---

Revenue Target Achievement:
{revenue_pct:.1f}%

Profit Target Achievement:
{profit_pct:.1f}%

Order Target Achievement:
{orders_pct:.1f}%

Customer Target Achievement:
{customers_pct:.1f}%
"""

    return summary


def answer_question(df, question):

    q = question.lower()

    if "revenue" in q:
        return (
            f"Revenue is currently ₦{get_total_revenue(df):,.2f}. "
            f"Target achievement is {revenue_achievement(df):.1f}%."
        )

    elif "profit" in q:
        return (
            f"Profit stands at ₦{get_total_profit(df):,.2f}. "
            f"Target achievement is {profit_achievement(df):.1f}%."
        )

    elif "customer" in q:
        return (
            f"The business currently serves "
            f"{get_total_customers(df):,} customers."
        )

    elif "order" in q:
        return (
            f"{get_total_orders(df):,} orders have been processed."
        )

    elif "margin" in q:
        return (
            f"Gross Margin is currently "
            f"{get_gross_margin(df):.2%}."
        )

    else:

        return executive_summary(df)
    