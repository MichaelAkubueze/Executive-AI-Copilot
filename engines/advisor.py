from analytics import (
    get_total_revenue,
    get_gross_margin,
)

from engines.executive_engine import business_health
from engines.target_engine import get_target

from engines.insight_engine import (
    region_insight,
    category_insight,
)   

def generate_recommendation(df):
    recommendations = []
#executive inteligence
    health = business_health(df)

    if health["score"] < 75:
        recommendations.append(
        "Strengthen weaker KPI areas to improve overall business health."
    )

    revenue = get_total_revenue(df)
    target = get_target("Revenue")

    if revenue < target:
        recommendations.append(
        "Accelerate revenue growth through stronger sales execution and expansion into high-performing markets."
    )

    margin = get_gross_margin(df)

    if margin < 15:
        recommendations.append(
        "Review pricing strategy, procurement costs and operating expenses to improve profitability."
    )



    region = region_insight(df)

    category = category_insight(df)

    recommendations = []

    recommendations.append(
        f"Increase investment in {region['best']['Region']} region where revenue performance is strongest."
    )

    recommendations.append(
        f"Review strategy for {region['worst']['Region']} region due to lower sales contribution."
    )

    recommendations.append(
        f"Expand inventory for {category['best']['Category']} category."
    )

    recommendations.append(
        f"Launch targeted promotions for {category['worst']['Category']} category."
    )
    
    if not recommendations:
        recommendations.append(
        "Maintain current business strategy while continuously monitoring key performance indicators."
    )
    
    # Remove duplicate recommendations while preserving order
    recommendations = list(dict.fromkeys(recommendations))

    return "\n\n".join(
        f"• {r}" for r in recommendations
    )