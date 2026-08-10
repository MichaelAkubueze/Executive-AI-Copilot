from engines.intent_engine import detect_intent

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
    get_sales_by_region,
    get_sales_by_category,
)

from engines.advisor import generate_recommendation


def executive_summary(df):

    return f"""
📊 Executive Summary

Revenue:
₦{get_total_revenue(df):,.2f}

Profit:
₦{get_total_profit(df):,.2f}

Orders:
{get_total_orders(df):,}

Customers:
{get_total_customers(df):,}

Gross Margin:
{get_gross_margin(df):.2%}
"""


def answer_question(df, question):

    intent = detect_intent(question)

    if intent == "revenue":

        return (
            f"💰 Total Revenue\n\n"
            f"₦{get_total_revenue(df):,.2f}"
        )

    elif intent == "profit":

        return (
            f"📈 Total Profit\n\n"
            f"₦{get_total_profit(df):,.2f}"
        )

    elif intent == "orders":

        return (
            f"🛒 Total Orders\n\n"
            f"{get_total_orders(df):,}"
        )

    elif intent == "customers":

        return (
            f"👥 Total Customers\n\n"
            f"{get_total_customers(df):,}"
        )

    elif intent == "margin":

        return (
            f"📊 Gross Margin\n\n"
            f"{get_gross_margin(df):.2%}"
        )

    elif intent == "best_region":

        region = get_sales_by_region(df).iloc[0]

        return (
            f"🏆 Best Performing Region\n\n"
            f"{region['Region']}\n"
            f"Revenue: ₦{region['Revenue']:,.2f}"
        )

    elif intent == "worst_region":

        region = get_sales_by_region(df).iloc[-1]

        return (
            f"⚠ Lowest Performing Region\n\n"
            f"{region['Region']}\n"
            f"Revenue: ₦{region['Revenue']:,.2f}"
        )

    elif intent == "best_category":

        category = get_sales_by_category(df).iloc[0]

        return (
            f"🥇 Best Product Category\n\n"
            f"{category['Category']}\n"
            f"Revenue: ₦{category['Revenue']:,.2f}"
        )

    elif intent == "recommendation":

        return generate_recommendation(df)

    return (
        "🤖 I couldn't understand that question.\n\n"
        "Try asking:\n"
        "• Revenue\n"
        "• Profit\n"
        "• Best Region\n"
        "• Worst Region\n"
        "• Best Category\n"
        "• Recommendation"
    )