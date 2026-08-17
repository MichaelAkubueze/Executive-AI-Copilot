import pandas as pd


# ==========================================================
# CUSTOMER AI INTELLIGENCE
# ==========================================================

def generate_customer_insights(df):

    if df.empty:

        return {
            "Customers": 0,
            "Revenue": 0,
            "Profit": 0,
            "Margin": 0,
            "Repeat Rate": 0,
            "Best Region": "N/A",
            "Top Customer": "N/A",
            "Top Customer Revenue": 0,
            "Top Profit Customer": "N/A",
            "Recommendations": [],
        }


    # ======================================================
    # BASIC METRICS
    # ======================================================

    revenue = df["Revenue"].sum()

    profit = df["Profit"].sum()

    customers = df["Customer ID"].nunique()

    margin = (
        profit / revenue * 100
        if revenue != 0
        else 0
    )


    # ======================================================
    # CUSTOMER ORDER ANALYSIS
    # ======================================================

    customer_orders = (
        df.groupby("Customer ID")
        .agg(
            Orders=("Order ID", "nunique")
        )
        .reset_index()
    )


    returning_customers = (
        customer_orders["Orders"] > 1
    ).sum()


    repeat_rate = (
        returning_customers / customers * 100
        if customers != 0
        else 0
    )


    # ======================================================
    # BEST REGION
    # ======================================================

    region_revenue = (
        df.groupby("Region")["Revenue"]
        .sum()
    )


    if not region_revenue.empty:

        best_region = region_revenue.idxmax()

    else:

        best_region = "N/A"


    # ======================================================
    # TOP CUSTOMER
    # ======================================================

    customer_revenue = (
        df.groupby("Customer Name")["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


    if not customer_revenue.empty:

        top_customer = customer_revenue.index[0]

        top_customer_revenue = customer_revenue.iloc[0]

    else:

        top_customer = "N/A"

        top_customer_revenue = 0


    # ======================================================
    # TOP PROFIT CUSTOMER
    # ======================================================

    customer_profit = (
        df.groupby("Customer Name")["Profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


    if not customer_profit.empty:

        top_profit_customer = customer_profit.index[0]

    else:

        top_profit_customer = "N/A"


    # ======================================================
    # CUSTOMER CONCENTRATION
    # ======================================================

    if revenue != 0 and not customer_revenue.empty:

        top_10_revenue = (
            customer_revenue
            .head(10)
            .sum()
        )

        concentration = (
            top_10_revenue
            / revenue
            * 100
        )

    else:

        concentration = 0


    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    recommendations = []


    # ------------------------------------------------------
    # Retention
    # ------------------------------------------------------

    if repeat_rate < 30:

        recommendations.append(
            "🔄 Customer repeat rate is relatively low. "
            "Strengthen retention campaigns and repeat-purchase programs."
        )

    elif repeat_rate < 60:

        recommendations.append(
            "🔄 There is room to improve customer retention. "
            "Introduce targeted loyalty and re-engagement campaigns."
        )

    else:

        recommendations.append(
            "✅ Customer retention is strong. "
            "Maintain current loyalty and relationship strategies."
        )


    # ------------------------------------------------------
    # Customer Concentration
    # ------------------------------------------------------

    if concentration >= 50:

        recommendations.append(
            "⚠️ Customer revenue is highly concentrated among "
            "the top 10 customers. Diversify the customer base "
            "to reduce concentration risk."
        )

    elif concentration >= 30:

        recommendations.append(
            "📊 A significant share of revenue comes from the "
            "top 10 customers. Monitor customer concentration risk."
        )

    else:

        recommendations.append(
            "✅ Customer revenue is reasonably diversified "
            "across the customer base."
        )


    # ------------------------------------------------------
    # Regional Opportunity
    # ------------------------------------------------------

    if best_region != "N/A":

        recommendations.append(
            f"🌍 Prioritize customer acquisition and retention "
            f"activities in the **{best_region}** region."
        )


    # ------------------------------------------------------
    # High Value Customer
    # ------------------------------------------------------

    if top_customer != "N/A":

        recommendations.append(
            f"🏆 Strengthen the relationship with **{top_customer}** "
            f"to protect high-value revenue."
        )


    # ------------------------------------------------------
    # Profitability
    # ------------------------------------------------------

    if margin < 20:

        recommendations.append(
            "⚠️ Customer profitability is relatively low. "
            "Review pricing, discounts, and servicing costs."
        )

    elif margin >= 30:

        recommendations.append(
            "💰 Customer profitability is healthy. "
            "Maintain pricing discipline and cost controls."
        )


    # ======================================================
    # RETURN STRUCTURED RESULT
    # ======================================================

    return {

        "Customers": customers,

        "Revenue": revenue,

        "Profit": profit,

        "Margin": margin,

        "Repeat Rate": repeat_rate,

        "Best Region": best_region,

        "Top Customer": top_customer,

        "Top Customer Revenue": top_customer_revenue,

        "Top Profit Customer": top_profit_customer,

        "Concentration": concentration,

        "Recommendations": recommendations,
    }