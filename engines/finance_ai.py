import pandas as pd


# ==========================================================
# AI FINANCE INTELLIGENCE
# ==========================================================

def generate_finance_insights(df):
    """
    Generate executive-level financial intelligence
    from the current filtered sales dataset.
    """

    # ======================================================
    # CORE FINANCIAL METRICS
    # ======================================================

    revenue = df["Revenue"].sum()

    cost = df["Cost"].sum()

    profit = df["Profit"].sum()

    if revenue == 0:
        margin = 0
    else:
        margin = (
            profit
            / revenue
            * 100
        )

    # ======================================================
    # BEST REGION
    # ======================================================

    region_profit = (
        df.groupby("Region")["Profit"]
        .sum()
    )

    if not region_profit.empty:
        best_region = region_profit.idxmax()
    else:
        best_region = "N/A"

    # ======================================================
    # BEST CATEGORY
    # ======================================================

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
    )

    if not category_profit.empty:
        best_category = category_profit.idxmax()
    else:
        best_category = "N/A"

    # ======================================================
    # TOP PROFIT PRODUCT
    # ======================================================

    product_profit = (
        df.groupby("Product Name")["Profit"]
        .sum()
    )

    if not product_profit.empty:

        top_profit_product = (
            product_profit.idxmax()
        )

        top_profit_value = (
            product_profit.max()
        )

    else:

        top_profit_product = "N/A"

        top_profit_value = 0

    # ======================================================
    # TOP REVENUE PRODUCT
    # ======================================================

    product_revenue = (
        df.groupby("Product Name")["Revenue"]
        .sum()
    )

    if not product_revenue.empty:

        top_revenue_product = (
            product_revenue.idxmax()
        )

        top_revenue_value = (
            product_revenue.max()
        )

    else:

        top_revenue_product = "N/A"

        top_revenue_value = 0

    # ======================================================
    # REVENUE CONCENTRATION
    # ======================================================

    if not product_revenue.empty:

        top_products = (
            product_revenue
            .sort_values(
                ascending=False
            )
            .head(10)
        )

        concentration = (
            top_products.sum()
            / revenue
            * 100
            if revenue != 0
            else 0
        )

    else:

        concentration = 0

    # ======================================================
    # SHIPPING COST
    # ======================================================

    if "Shipping Cost" in df.columns:

        shipping_cost = (
            df["Shipping Cost"].sum()
        )

    else:

        shipping_cost = 0

    # ======================================================
    # AVERAGE ORDER VALUE
    # ======================================================

    orders = df["Order ID"].nunique()

    if orders == 0:

        average_order_value = 0

    else:

        average_order_value = (
            revenue / orders
        )

    # ======================================================
    # FINANCIAL STATUS
    # ======================================================

    if margin >= 30:

        financial_status = "Strong"

    elif margin >= 20:

        financial_status = "Healthy"

    elif margin >= 10:

        financial_status = "Watch"

    else:

        financial_status = "At Risk"

    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    recommendations = []

    # Profitability recommendation

    if margin >= 25:

        recommendations.append(
            "✅ Profitability is strong. "
            "Maintain current pricing and cost controls."
        )

    elif margin >= 15:

        recommendations.append(
            "⚠️ Profitability is moderate. "
            "Review operating costs and pricing opportunities."
        )

    else:

        recommendations.append(
            "🚨 Profitability requires attention. "
            "Prioritize cost reduction and margin improvement."
        )

    # Region recommendation

    if best_region != "N/A":

        recommendations.append(
            f"🌍 Prioritize profitable growth in "
            f"**{best_region}**."
        )

    # Category recommendation

    if best_category != "N/A":

        recommendations.append(
            f"🏷️ Strengthen commercial investment in "
            f"**{best_category}**."
        )

    # Product recommendation

    if top_profit_product != "N/A":

        recommendations.append(
            f"🏆 Protect the profitability of "
            f"**{top_profit_product}** through continued "
            f"cost and pricing discipline."
        )

    # Concentration recommendation

    if concentration >= 80:

        recommendations.append(
            "⚠️ Financial performance is highly concentrated "
            "among the top products. Diversify the portfolio "
            "to reduce dependency risk."
        )

    elif concentration >= 60:

        recommendations.append(
            "📊 Product revenue concentration is significant. "
            "Monitor dependency on the highest-performing products."
        )

    # Shipping recommendation

    if revenue > 0:

        shipping_ratio = (
            shipping_cost
            / revenue
            * 100
        )

        if shipping_ratio >= 10:

            recommendations.append(
                "🚚 Shipping costs are significant relative "
                "to revenue. Review logistics efficiency."
            )

    # ======================================================
    # RETURN AI INSIGHT PACKAGE
    # ======================================================

    return {

        "Revenue": revenue,

        "Cost": cost,

        "Profit": profit,

        "Margin": margin,

        "Status": financial_status,

        "Best Region": best_region,

        "Best Category": best_category,

        "Top Profit Product": top_profit_product,

        "Top Profit Product Value": top_profit_value,

        "Top Revenue Product": top_revenue_product,

        "Top Revenue Product Value": top_revenue_value,

        "Concentration": concentration,

        "Shipping Cost": shipping_cost,

        "Average Order Value": average_order_value,

        "Orders": orders,

        "Recommendations": recommendations,
    }
    