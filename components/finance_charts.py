import plotly.express as px


# ==========================================================
# FINANCE CHART LAYOUT
# ==========================================================

def finance_chart_layout(fig):

    fig.update_layout(
        template="plotly_white",
        margin=dict(
            l=40,
            r=40,
            t=60,
            b=40
        ),
        title_x=0.02,
        hovermode="x unified",
        legend_title_text=""
    )

    return fig


# ==========================================================
# MONTHLY REVENUE, COST & PROFIT
# ==========================================================

def monthly_financial_chart(df):

    summary = (
        df.groupby("Month", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum")
        )
    )

    fig = px.line(
        summary,
        x="Month",
        y=[
            "Revenue",
            "Cost",
            "Profit"
        ],
        markers=True,
        title="Monthly Revenue, Cost & Profit"
    )

    fig.update_layout(
        yaxis_title="Amount (₦)",
        xaxis_title="Month"
    )

    return finance_chart_layout(fig)


# ==========================================================
# REVENUE VS PROFIT
# ==========================================================

def revenue_vs_profit_chart(df):

    summary = (
        df.groupby("Month", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
    )

    fig = px.bar(
        summary,
        x="Month",
        y=[
            "Revenue",
            "Profit"
        ],
        barmode="group",
        title="Revenue vs Profit"
    )

    fig.update_layout(
        yaxis_title="Amount (₦)",
        xaxis_title="Month"
    )

    return finance_chart_layout(fig)


# ==========================================================
# PROFIT MARGIN BY MONTH
# ==========================================================

def monthly_profit_margin_chart(df):

    summary = (
        df.groupby("Month", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    fig = px.line(
        summary,
        x="Month",
        y="Profit Margin",
        markers=True,
        title="Monthly Profit Margin"
    )

    fig.update_layout(
        yaxis_title="Profit Margin (%)",
        xaxis_title="Month"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    return finance_chart_layout(fig)


# ==========================================================
# REGIONAL FINANCIAL PERFORMANCE
# ==========================================================

def regional_financial_chart(df):

    summary = (
        df.groupby("Region", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

    fig = px.bar(
        summary,
        x="Region",
        y=[
            "Revenue",
            "Profit"
        ],
        barmode="group",
        title="Regional Revenue & Profit"
    )

    fig.update_layout(
        yaxis_title="Amount (₦)",
        xaxis_title="Region"
    )

    return finance_chart_layout(fig)


# ==========================================================
# REGIONAL PROFIT MARGIN
# ==========================================================

def regional_profit_margin_chart(df):

    summary = (
        df.groupby("Region", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    summary = summary.sort_values(
        "Profit Margin",
        ascending=False
    )

    fig = px.bar(
        summary,
        x="Region",
        y="Profit Margin",
        title="Regional Profit Margin"
    )

    fig.update_layout(
        yaxis_title="Profit Margin (%)",
        xaxis_title="Region"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    return finance_chart_layout(fig)


# ==========================================================
# CATEGORY FINANCIAL PERFORMANCE
# ==========================================================

def category_financial_chart(df):

    summary = (
        df.groupby("Category", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

    fig = px.bar(
        summary,
        x="Category",
        y=[
            "Revenue",
            "Profit"
        ],
        barmode="group",
        title="Category Revenue & Profit"
    )

    fig.update_layout(
        yaxis_title="Amount (₦)",
        xaxis_title="Category"
    )

    return finance_chart_layout(fig)


# ==========================================================
# PAYMENT METHOD PERFORMANCE
# ==========================================================

def payment_method_chart(df):

    summary = (
        df.groupby(
            "Payment Method",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
    )

    fig = px.bar(
        summary,
        x="Payment Method",
        y="Revenue",
        title="Revenue by Payment Method"
    )

    fig.update_layout(
        yaxis_title="Revenue (₦)",
        xaxis_title="Payment Method"
    )

    return finance_chart_layout(fig)


# ==========================================================
# SALES CHANNEL PERFORMANCE
# ==========================================================

def sales_channel_financial_chart(df):

    summary = (
        df.groupby(
            "Sales Channel",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
    )

    fig = px.bar(
        summary,
        x="Sales Channel",
        y=[
            "Revenue",
            "Profit"
        ],
        barmode="group",
        title="Sales Channel Revenue & Profit"
    )

    fig.update_layout(
        yaxis_title="Amount (₦)",
        xaxis_title="Sales Channel"
    )

    return finance_chart_layout(fig)


# ==========================================================
# TOP PROFITABLE PRODUCTS
# ==========================================================

def top_profitable_products_chart(
    df,
    limit=10
):

    summary = (
        df.groupby(
            "Product Name",
            as_index=False
        )
        .agg(
            Profit=("Profit", "sum")
        )
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(limit)
    )

    fig = px.bar(
        summary,
        x="Profit",
        y="Product Name",
        orientation="h",
        title="Top Profitable Products"
    )

    fig.update_layout(
        xaxis_title="Profit (₦)",
        yaxis_title="Product"
    )

    return finance_chart_layout(fig)


# ==========================================================
# COST STRUCTURE
# ==========================================================

def cost_structure_chart(df):

    total_cost = df["Cost"].sum()

    shipping_cost = (
        df["Shipping Cost"].sum()
        if "Shipping Cost" in df.columns
        else 0
    )

    profit = df["Profit"].sum()

    summary = {
        "Cost": total_cost,
        "Shipping Cost": shipping_cost,
        "Profit": profit
    }

    chart_df = (
        __import__("pandas")
        .DataFrame(
            list(summary.items()),
            columns=[
                "Metric",
                "Amount"
            ]
        )
    )

    fig = px.pie(
        chart_df,
        names="Metric",
        values="Amount",
        hole=0.5,
        title="Financial Structure"
    )

    return finance_chart_layout(fig)
