import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# Microsoft Color Theme
# --------------------------------------------------

COLORS = [
    "#2563EB",
    "#10B981",
    "#F59E0B",
    "#EF4444",
    "#8B5CF6",
    "#06B6D4",
    "#14B8A6",
]

# --------------------------------------------------
# Common Layout
# --------------------------------------------------

def chart_layout(fig):

    fig.update_layout(

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(
            family="Segoe UI",
            color="#334155"
        ),

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),

        height=420,

        title_font_size=20,

        legend_title_text="",

        hovermode="x unified",

    )

    fig.update_xaxes(

        showgrid=False,

        zeroline=False

    )

    fig.update_yaxes(

        gridcolor="#EEF2F7",

        zeroline=False

    )

    return fig


# ==========================================================
# Monthly Revenue Trend
# ==========================================================

def monthly_revenue_chart(df):

    monthly = (

        df.groupby(

            ["Year","Month"],

            as_index=False

        )

        .agg(

            Revenue=("Revenue","sum"),

            SortDate=("Order Date","min")

        )

        .sort_values("SortDate")

    )

    fig = px.area(

        monthly,

        x="Month",

        y="Revenue",

        color="Year",

        markers=True,

        title="Monthly Revenue Trend"

    )

    fig.update_traces(

        line_width=4,

        marker_size=8

    )

    return chart_layout(fig)


# ==========================================================
# Region
# ==========================================================

def sales_by_region(df):

    region = (

        df.groupby(

            "Region",

            as_index=False

        )

        .agg(

            Revenue=("Revenue","sum")

        )

        .sort_values(

            "Revenue",

            ascending=False

        )

    )

    fig = px.bar(

        region,

        x="Revenue",

        y="Region",

        orientation="h",

        color="Revenue",

        color_continuous_scale="Blues",

        title="Sales by Region"

    )

    return chart_layout(fig)


# ==========================================================
# Category
# ==========================================================

def sales_by_category(df):

    cat = (

        df.groupby(

            "Category",

            as_index=False

        )

        .agg(

            Revenue=("Revenue","sum")

        )

        .sort_values(

            "Revenue",

            ascending=False

        )

    )

    fig = px.bar(

        cat,

        x="Category",

        y="Revenue",

        color="Category",

        title="Revenue by Category"

    )

    return chart_layout(fig)


# ==========================================================
# Customer Segments
# ==========================================================

def customer_segments(df):

    seg = (

        df.groupby(

            "Customer Segment",

            as_index=False

        )

        .agg(

            Customers=("Customer ID","count")

        )

    )

    fig = px.pie(

        seg,

        names="Customer Segment",

        values="Customers",

        hole=.65,

        title="Customer Segments"

    )

    fig.update_traces(

        textposition="inside",

        textinfo="percent+label"

    )

    return chart_layout(fig)


# ==========================================================
# Sales Channel
# ==========================================================

def sales_channel(df):

    channel = (

        df.groupby(

            "Sales Channel",

            as_index=False

        )

        .agg(

            Revenue=("Revenue","sum")

        )

    )

    fig = px.bar(

        channel,

        x="Sales Channel",

        y="Revenue",

        color="Sales Channel",

        title="Sales Channel Performance"

    )

    return chart_layout(fig)


# ==========================================================
# Top Products
# ==========================================================

def top_products(df):

    prod = (

        df.groupby(

            "Product Name",

            as_index=False

        )

        .agg(

            Revenue=("Revenue","sum")

        )

        .sort_values(

            "Revenue",

            ascending=False

        )

        .head(10)

    )

    fig = px.bar(

        prod,

        x="Revenue",

        y="Product Name",

        orientation="h",

        color="Revenue",

        color_continuous_scale="Viridis",

        title="Top 10 Products"

    )

    return chart_layout(fig)


# ==========================================================
# Top Customers
# ==========================================================

def top_customers(df):

    cust = (

        df.groupby(

            "Customer Name",

            as_index=False

        )

        .agg(

            Revenue=("Revenue","sum")

        )

        .sort_values(

            "Revenue",

            ascending=False

        )

        .head(10)

    )

    fig = px.bar(

        cust,

        x="Revenue",

        y="Customer Name",

        orientation="h",

        color="Revenue",

        color_continuous_scale="Turbo",

        title="Top 10 Customers"

    )
    

    return chart_layout(fig)

# ==========================================================
# RAW DATA - SALES BY REGION
# ==========================================================

def get_sales_by_region(df):

    return (
        df.groupby(
            "Region",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .reset_index(drop=True)
    )
    
    region.insert(0, "Rank", range(1, len(region) + 1))

    return region

# ==========================================================
# RAW DATA - SALES BY CATEGORY
# ==========================================================

def get_sales_by_category(df):

    return (
        df.groupby(
            "Category",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .reset_index(drop=True)
    )
    
    category.insert(0, "Rank", range(1, len(region) + 1))

    return category
    
    
def top_salespersons(df):

    sales = (
        df.groupby(
            "Salesperson",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        sales,
        x="Revenue",
        y="Salesperson",
        orientation="h",
        color="Profit",
        color_continuous_scale="Viridis",
        title="Top 10 Salespersons"
    )

    return chart_layout(fig)

def sales_by_country(df):

    country = (
        df.groupby(
            "Country",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

    fig = px.bar(
        country,
        x="Country",
        y="Revenue",
        color="Revenue",
        color_continuous_scale="Blues",
        title="Revenue by Country"
    )

    return chart_layout(fig)
def sales_by_city(df):

    city = (
        df.groupby(
            "City",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(15)
    )

    fig = px.bar(
        city,
        x="Revenue",
        y="City",
        orientation="h",
        color="Revenue",
        color_continuous_scale="Turbo",
        title="Top Cities"
    )

    return chart_layout(fig)
def payment_methods(df):

    pay = (
        df.groupby(
            "Payment Method",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
    )

    fig = px.pie(
        pay,
        names="Payment Method",
        values="Revenue",
        hole=.55,
        title="Payment Methods"
    )

    return chart_layout(fig)

# ==========================================================
# TOP 20 SALES TRANSACTIONS
# ==========================================================

def top_sales_transactions(df):

    transactions = (

        df[
            [
                "Invoice No",
                "Order Date",
                "Customer Name",
                "Product Name",
                "Region",
                "Revenue",
                "Profit"
            ]
        ]

        .sort_values(
            "Revenue",
            ascending=False
        )

        .head(20)

        .reset_index(drop=True)

    )

    transactions.insert(
        0,
        "Rank",
        range(1, len(transactions) + 1)
    )

    return transactions
# ==========================================================
# AI EXECUTIVE INSIGHTS
# ==========================================================
def generate_sales_insights(df):

    revenue = df["Revenue"].sum()
    profit = df["Profit"].sum()

    margin = (profit / revenue) * 100

    best_region = (
        df.groupby("Region")["Revenue"]
        .sum()
        .idxmax()
    )

    best_category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .idxmax()
    )

    top_customer = (
        df.groupby("Customer Name")["Revenue"]
        .sum()
        .idxmax()
    )

    top_salesperson = (
        df.groupby("Salesperson")["Revenue"]
        .sum()
        .idxmax()
    )

    recommendations = []

    # Margin recommendation
    if margin < 25:
        recommendations.append(
            "⚠ Profit margin is below the target of 25%. Review pricing and operating costs."
        )
    else:
        recommendations.append(
            "✅ Profit margin is healthy. Maintain current pricing and cost controls."
        )

    # Always include strategic recommendations
    recommendations.append(
        f"📈 Increase marketing investment in the **{best_region}** region."
    )

    recommendations.append(
        f"🛒 Increase inventory for the **{best_category}** category."
    )

    recommendations.append(
        f"🏆 Recognize **{top_salesperson}** for outstanding sales performance."
    )

    recommendations.append(
        f"🤝 Strengthen relationships with **{top_customer}** to encourage repeat business."
    )

    return {
        "Revenue": revenue,
        "Profit": profit,
        "Margin": margin,
        "Best Region": best_region,
        "Best Category": best_category,
        "Top Customer": top_customer,
        "Top Salesperson": top_salesperson,
        "Recommendations": recommendations,
    }