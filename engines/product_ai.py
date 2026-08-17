import pandas as pd


# ==========================================================
# PRODUCT AI INTELLIGENCE
# ==========================================================

def generate_product_insights(df):
    """
    Generate executive-level product performance insights
    and recommendations.
    """

    # ------------------------------------------------------
    # CORE METRICS
    # ------------------------------------------------------

    revenue = df["Revenue"].sum()

    profit = df["Profit"].sum()

    margin = (
        profit / revenue * 100
        if revenue != 0
        else 0
    )

    products = df["Product ID"].nunique()

    # ------------------------------------------------------
    # BEST PRODUCT
    # ------------------------------------------------------

    product_revenue = (
        df.groupby("Product Name")["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_product = (
        product_revenue.index[0]
        if not product_revenue.empty
        else "N/A"
    )

    best_product_revenue = (
        product_revenue.iloc[0]
        if not product_revenue.empty
        else 0
    )

    # ------------------------------------------------------
    # MOST PROFITABLE PRODUCT
    # ------------------------------------------------------

    product_profit = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    top_profit_product = (
        product_profit.index[0]
        if not product_profit.empty
        else "N/A"
    )

    # ------------------------------------------------------
    # BEST CATEGORY
    # ------------------------------------------------------

    category_revenue = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_category = (
        category_revenue.index[0]
        if not category_revenue.empty
        else "N/A"
    )

    # ------------------------------------------------------
    # CATEGORY PROFIT
    # ------------------------------------------------------

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_profit_category = (
        category_profit.index[0]
        if not category_profit.empty
        else "N/A"
    )

    # ------------------------------------------------------
    # TOP 10 PRODUCT CONCENTRATION
    # ------------------------------------------------------

    top_10_revenue = (
        product_revenue
        .head(10)
        .sum()
    )

    concentration = (
        top_10_revenue / revenue * 100
        if revenue != 0
        else 0
    )

    # ------------------------------------------------------
    # RECOMMENDATIONS
    # ------------------------------------------------------

    recommendations = []

    # Margin recommendation

    if margin >= 30:

        recommendations.append(
            "✅ Product profitability is healthy. "
            "Maintain current pricing and cost controls."
        )

    elif margin >= 20:

        recommendations.append(
            "⚠️ Product margins are moderate. "
            "Review pricing and product costs for improvement."
        )

    else:

        recommendations.append(
            "🚨 Product margins are low. "
            "Prioritize pricing, cost reduction, and portfolio review."
        )

    # Best product recommendation

    if best_product != "N/A":

        recommendations.append(
            f"📈 Prioritize inventory and marketing support "
            f"for **{best_product}**."
        )

    # Category recommendation

    if best_category != "N/A":

        recommendations.append(
            f"🏷️ Strengthen commercial investment in the "
            f"**{best_category}** category."
        )

    # Profitability recommendation

    if top_profit_product != "N/A":

        recommendations.append(
            f"💰 Protect the profitability of **{top_profit_product}** "
            f"through continued cost and pricing discipline."
        )

    # Concentration recommendation

    if concentration >= 50:

        recommendations.append(
            "⚠️ Revenue concentration is high among the top "
            "10 products. Diversify the product portfolio "
            "to reduce dependency risk."
        )

    else:

        recommendations.append(
            "✅ Product revenue is reasonably diversified. "
            "Continue developing additional high-performing products."
        )

    # ------------------------------------------------------
    # RETURN INSIGHTS
    # ------------------------------------------------------

    return {
        "Products": products,
        "Revenue": revenue,
        "Profit": profit,
        "Margin": margin,
        "Best Product": best_product,
        "Best Product Revenue": best_product_revenue,
        "Top Profit Product": top_profit_product,
        "Best Category": best_category,
        "Best Profit Category": best_profit_category,
        "Concentration": concentration,
        "Recommendations": recommendations,
    }