from engines.insight_engine import (
    region_insight,
    category_insight,
)


def generate_recommendation(df):

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

    return "\n\n".join(
        f"• {r}" for r in recommendations
    )