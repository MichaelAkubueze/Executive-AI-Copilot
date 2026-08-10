from engines.kpi_engine import (
    revenue_achievement,
    profit_achievement,
    orders_achievement,
    customer_achievement,
    margin_achievement,
)


def generate_recommendations(df):

    recommendations = []

    revenue = revenue_achievement(df)
    profit = profit_achievement(df)
    orders = orders_achievement(df)
    customers = customer_achievement(df)
    margin = margin_achievement(df)

    if revenue < 75:
        recommendations.append(
            {
                "priority": "High",
                "title": "Increase Revenue",
                "action": "Focus marketing campaigns on high-performing products and regions."
            }
        )

    if profit < 75:
        recommendations.append(
            {
                "priority": "High",
                "title": "Improve Profitability",
                "action": "Review discounts, operating costs and low-margin products."
            }
        )

    if orders < 80:
        recommendations.append(
            {
                "priority": "Medium",
                "title": "Increase Sales Orders",
                "action": "Launch promotions and strengthen sales follow-up."
            }
        )

    if customers < 80:
        recommendations.append(
            {
                "priority": "Medium",
                "title": "Customer Acquisition",
                "action": "Increase customer acquisition campaigns and retention programmes."
            }
        )

    if margin < 80:
        recommendations.append(
            {
                "priority": "Medium",
                "title": "Protect Margin",
                "action": "Reduce excessive discounts and optimise product pricing."
            }
        )

    if not recommendations:

        recommendations.append(
            {
                "priority": "Excellent",
                "title": "Business Performing Well",
                "action": "Maintain current strategy while monitoring key performance indicators."
            }
        )

    return recommendations