from analytics import (
    get_total_revenue,
    get_total_profit,
    get_gross_margin,
    get_sales_by_region,
    get_sales_by_category,
)


def generate_insights(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    margin = get_gross_margin(df)

    region_df = get_sales_by_region(df)
    category_df = get_sales_by_category(df)

    best_region = region_df.iloc[0]
    worst_region = region_df.iloc[-1]

    best_category = category_df.iloc[0]
    worst_category = category_df.iloc[-1]

    insights = [

        (
            "💰 Revenue",
            f"Current revenue is ₦{revenue:,.2f}."
        ),

        (
            "📈 Profit",
            f"Current profit is ₦{profit:,.2f}."
        ),

        (
            "📊 Gross Margin",
            f"Gross margin is {margin:.2%}."
        ),

        (
            "🏆 Best Performing Region",
            f"{best_region['Region']} generated ₦{best_region['Revenue']:,.2f}."
        ),

        (
            "⚠ Lowest Performing Region",
            f"{worst_region['Region']} generated ₦{worst_region['Revenue']:,.2f}."
        ),

        (
            "🥇 Best Product Category",
            f"{best_category['Category']} generated ₦{best_category['Revenue']:,.2f}."
        ),

        (
            "📉 Lowest Product Category",
            f"{worst_category['Category']} generated ₦{worst_category['Revenue']:,.2f}."
        ),

    ]

    return insights