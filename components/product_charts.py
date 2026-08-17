import plotly.express as px


# ==========================================================
# PRODUCT CHART LAYOUT
# ==========================================================

def product_chart_layout(fig):

    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(
            l=40,
            r=40,
            t=70,
            b=40
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    return fig


# ==========================================================
# TOP PRODUCTS — REVENUE
# ==========================================================

def top_products_revenue_chart(df, limit=10):

    summary = (
        df.groupby("Product Name", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(limit)
        .sort_values("Revenue")
    )

    fig = px.bar(
        summary,
        x="Revenue",
        y="Product Name",
        orientation="h",
        title="Top Products by Revenue",
        text_auto=".2s",
    )

    return product_chart_layout(fig)


# ==========================================================
# TOP PRODUCTS — PROFIT
# ==========================================================

def top_products_profit_chart(df, limit=10):

    summary = (
        df.groupby("Product Name", as_index=False)
        .agg(
            Profit=("Profit", "sum")
        )
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(limit)
        .sort_values("Profit")
    )

    fig = px.bar(
        summary,
        x="Profit",
        y="Product Name",
        orientation="h",
        title="Top Products by Profit",
        text_auto=".2s",
    )

    return product_chart_layout(fig)


# ==========================================================
# CATEGORY REVENUE
# ==========================================================

def product_category_revenue_chart(df):

    summary = (
        df.groupby("Category", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

    fig = px.bar(
        summary,
        x="Category",
        y="Revenue",
        title="Revenue by Product Category",
        text_auto=".2s",
    )

    return product_chart_layout(fig)


# ==========================================================
# CATEGORY PROFIT
# ==========================================================

def product_category_profit_chart(df):

    summary = (
        df.groupby("Category", as_index=False)
        .agg(
            Profit=("Profit", "sum")
        )
        .sort_values(
            "Profit",
            ascending=False
        )
    )

    fig = px.bar(
        summary,
        x="Category",
        y="Profit",
        title="Profit by Product Category",
        text_auto=".2s",
    )

    return product_chart_layout(fig)


# ==========================================================
# SUBCATEGORY REVENUE
# ==========================================================

def product_subcategory_chart(df, limit=15):

    summary = (
        df.groupby("Subcategory", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(limit)
        .sort_values("Revenue")
    )

    fig = px.bar(
        summary,
        x="Revenue",
        y="Subcategory",
        orientation="h",
        title="Top Subcategories by Revenue",
        text_auto=".2s",
    )

    return product_chart_layout(fig)


# ==========================================================
# PRODUCT UNITS SOLD
# ==========================================================

def product_units_chart(df, limit=10):

    summary = (
        df.groupby("Product Name", as_index=False)
        .agg(
            Units=("Quantity", "sum")
        )
        .sort_values(
            "Units",
            ascending=False
        )
        .head(limit)
        .sort_values("Units")
    )

    fig = px.bar(
        summary,
        x="Units",
        y="Product Name",
        orientation="h",
        title="Top Products by Units Sold",
        text_auto=".2s",
    )

    return product_chart_layout(fig)


# ==========================================================
# PRODUCT PROFITABILITY
# ==========================================================

def product_profitability_chart(df, limit=15):

    summary = (
        df.groupby(
            "Product Name",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    summary = (
        summary[
            summary["Revenue"] > 0
        ]
        .sort_values(
            "Profit Margin",
            ascending=False
        )
        .head(limit)
        .sort_values("Profit Margin")
    )

    fig = px.bar(
        summary,
        x="Profit Margin",
        y="Product Name",
        orientation="h",
        title="Most Profitable Products by Margin",
        text="Profit Margin",
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
    )

    return product_chart_layout(fig)


# ==========================================================
# PRODUCT REVENUE DISTRIBUTION
# ==========================================================

def product_revenue_distribution_chart(df):

    summary = (
        df.groupby(
            "Product Name",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
    )

    fig = px.histogram(
        summary,
        x="Revenue",
        nbins=20,
        title="Product Revenue Distribution",
    )

    return product_chart_layout(fig)