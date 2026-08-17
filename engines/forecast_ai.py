from engines.forecast_engine import (
    forecast_next_month,
    forecast_growth,
    forecast_status,
)


# ==========================================================
# AI FORECAST INTELLIGENCE
# ==========================================================

def generate_forecast_insights(df):

    forecast = forecast_next_month(df)

    growth = forecast_growth(df)

    status = forecast_status(df)

    revenue = forecast["Revenue"]
    profit = forecast["Profit"]
    orders = forecast["Orders"]

    # ======================================================
    # PROFIT MARGIN
    # ======================================================

    if revenue == 0:
        margin = 0
    else:
        margin = (
            profit
            / revenue
            * 100
        )

    # ======================================================
    # FORECAST ASSESSMENT
    # ======================================================

    if status == "Strong Growth":

        outlook = (
            "The business is showing a strong "
            "positive revenue trajectory."
        )

    elif status == "Moderate Growth":

        outlook = (
            "The business is showing moderate "
            "positive revenue momentum."
        )

    elif status == "Stable":

        outlook = (
            "Revenue performance is relatively "
            "stable based on recent activity."
        )

    elif status == "Moderate Decline":

        outlook = (
            "Recent revenue performance indicates "
            "a moderate downward trend."
        )

    else:

        outlook = (
            "Recent revenue performance indicates "
            "a significant downward trend."
        )

    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    recommendations = []

    if growth > 5:

        recommendations.append(
            "📈 Maintain investment in high-performing "
            "sales channels while the positive trend continues."
        )

    elif growth >= 0:

        recommendations.append(
            "📊 Protect the current revenue base and "
            "identify opportunities to accelerate growth."
        )

    else:

        recommendations.append(
            "⚠️ Review recent sales performance and "
            "identify the causes of the revenue decline."
        )

    if margin >= 30:

        recommendations.append(
            "💰 Profitability is healthy. Maintain "
            "current pricing and cost controls."
        )

    elif margin >= 20:

        recommendations.append(
            "💰 Profitability is acceptable, but "
            "cost optimization should remain a priority."
        )

    else:

        recommendations.append(
            "⚠️ Profit margin requires attention. "
            "Review pricing, operating costs and product mix."
        )

    if orders > 0:

        recommendations.append(
            "📦 Monitor order volume alongside revenue "
            "to determine whether forecast growth is "
            "volume-driven."
        )

    if status in [
        "Moderate Decline",
        "Declining",
    ]:

        recommendations.append(
            "🚨 Consider targeted commercial interventions "
            "to reverse the negative forecast trend."
        )

    # ======================================================
    # RETURN AI INSIGHT PACKAGE
    # ======================================================

    return {

        "Revenue": revenue,

        "Profit": profit,

        "Orders": orders,

        "Growth": growth,

        "Margin": margin,

        "Status": status,

        "Outlook": outlook,

        "Recommendations": recommendations,
    }
    
    