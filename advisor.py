from kpi import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)


def generate_recommendation(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    margin = get_gross_margin(df)
    customers = get_total_customers(df)
    orders = get_total_orders(df)

    recommendations = []

    if margin < 0.25:
        recommendations.append(
            "⚠ Gross margin is below 25%. Review pricing strategy and operating costs."
        )

    if revenue < 50_000_000:
        recommendations.append(
            "📈 Revenue is below the strategic target. Increase sales campaigns and customer acquisition."
        )

    if customers < 1000:
        recommendations.append(
            "👥 Customer base is relatively small. Invest in retention and acquisition programs."
        )

    if orders < 5000:
        recommendations.append(
            "🛒 Order volume is below expectation. Consider promotional offers to drive demand."
        )

    if profit > revenue * 0.30:
        recommendations.append(
            "✅ Profitability is strong. Continue scaling high-margin products."
        )

    if not recommendations:
        recommendations.append(
            "✅ Business performance is healthy across major KPIs. Maintain current strategy while monitoring trends."
        )

    return "\n\n".join(recommendations)