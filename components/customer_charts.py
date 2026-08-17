import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# CUSTOMER CHART THEME
# ==========================================================

def customer_chart_layout(fig):

    fig.update_layout(
        template="plotly_white",

        height=420,

        margin=dict(
            l=20,
            r=20,
            t=55,
            b=20,
        ),

        font=dict(
            family="Segoe UI",
            color="#334155",
        ),

        legend_title_text="",

        hovermode="x unified",
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
    )

    fig.update_yaxes(
        gridcolor="#EEF2F7",
        zeroline=False,
    )

    return fig


# ==========================================================
# 1. CUSTOMER SEGMENTS
# ==========================================================

def customer_segment_chart(df):

    segment = (
        df.groupby(
            "Customer Segment",
            as_index=False
        )
        .agg(
            Customers=(
                "Customer ID",
                "nunique"
            )
        )
        .sort_values(
            "Customers",
            ascending=False
        )
    )

    fig = px.pie(
        segment,

        names="Customer Segment",

        values="Customers",

        hole=0.55,

        title="Customer Segmentation",
    )

    fig.update_traces(
        textposition="inside",

        textinfo="percent+label",
    )

    return customer_chart_layout(fig)


# ==========================================================
# 2. TOP CUSTOMERS BY REVENUE
# ==========================================================

def top_customers_revenue(df):

    customers = (
        df.groupby(
            "Customer Name",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        customers,

        x="Revenue",

        y="Customer Name",

        orientation="h",

        title="Top 10 Customers by Revenue",

        color="Revenue",

        color_continuous_scale="Blues",
    )

    return customer_chart_layout(fig)


# ==========================================================
# 3. TOP CUSTOMERS BY PROFIT
# ==========================================================

def top_customers_profit(df):

    customers = (
        df.groupby(
            "Customer Name",
            as_index=False
        )
        .agg(
            Profit=("Profit", "sum")
        )
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        customers,

        x="Profit",

        y="Customer Name",

        orientation="h",

        title="Top 10 Customers by Profit",

        color="Profit",

        color_continuous_scale="Greens",
    )

    return customer_chart_layout(fig)


# ==========================================================
# 4. CUSTOMER REVENUE BY REGION
# ==========================================================

def customer_revenue_by_region(df):

    region = (
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
    )

    fig = px.bar(
        region,

        x="Region",

        y="Revenue",

        color="Revenue",

        title="Customer Revenue by Region",

        color_continuous_scale="Blues",
    )

    return customer_chart_layout(fig)


# ==========================================================
# 5. CUSTOMER ORDERS
# ==========================================================
def customer_orders_chart(df):

    orders = (
        df.groupby(
            "Customer Name",
            as_index=False
        )
        .agg(
            Orders=("Order ID", "nunique")
        )
        .sort_values(
            "Orders",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        orders,

        x="Orders",

        y="Customer Name",

        orientation="h",

        title="Top 10 Customers by Order Frequency",

        color="Orders",

        color_continuous_scale="Purples",
    )

    return customer_chart_layout(fig)


# ==========================================================
# 6. CUSTOMER PROFITABILITY
# ==========================================================

def customer_profitability(df):

    customers = (
        df.groupby(
            "Customer Name",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),

            Profit=("Profit", "sum"),
        )
    )

    customers["Margin"] = (
    customers["Profit"]
    / customers["Revenue"].replace(0, float("nan"))
    * 100
    )

    customers = (
        customers
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        customers,

        x="Profit",

        y="Customer Name",

        orientation="h",

        title="Top 10 Customers by Profitability",

        color="Margin",

        color_continuous_scale="Viridis",

        hover_data=[
            "Revenue",
            "Margin",
        ],
    )

    return customer_chart_layout(fig)


# ==========================================================
# 7. CUSTOMER REVENUE CONCENTRATION
# ==========================================================

def customer_revenue_concentration(df):

    customers = (
        df.groupby(
            "Customer Name",
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

    customers["Cumulative Revenue"] = (
        customers["Revenue"].cumsum()
    )

    total_revenue = customers["Revenue"].sum()

    if total_revenue != 0:

        customers["Cumulative %"] = (
            customers["Cumulative Revenue"]
            / total_revenue
            * 100
        )

    else:

        customers["Cumulative %"] = 0

    customers["Customer Rank"] = (
        customers.index + 1
    )

    fig = px.line(
        customers,

        x="Customer Rank",

        y="Cumulative %",

        markers=True,

        title="Customer Revenue Concentration",
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    return customer_chart_layout(fig)


# ==========================================================
# 8. CUSTOMER REVENUE DISTRIBUTION
# ==========================================================

def customer_revenue_distribution(df):

    customers = (
        df.groupby(
            "Customer Name",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
    )

    fig = px.histogram(
        customers,

        x="Revenue",

        nbins=20,

        title="Customer Revenue Distribution",
    )

    return customer_chart_layout(fig)

# ==========================================================
# NEW VS RETURNING CUSTOMERS
# ==========================================================

def new_vs_returning_customers_chart(df):

    customer_orders = (
        df.groupby("Customer ID")
        .agg(
            Orders=("Order ID", "nunique")
        )
        .reset_index()
    )

    customer_orders["Customer Type"] = customer_orders["Orders"].apply(
        lambda x: "New Customer"
        if x == 1
        else "Returning Customer"
    )

    summary = (
        customer_orders
        .groupby(
            "Customer Type",
            as_index=False
        )
        .agg(
            Customers=("Customer ID", "count")
        )
    )

    fig = px.pie(
        summary,
        names="Customer Type",
        values="Customers",
        hole=0.55,
        title="New vs Returning Customers"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    return customer_chart_layout(fig)


# ==========================================================
# NEW VS RETURNING CUSTOMER REVENUE
# ==========================================================

def new_vs_returning_revenue_chart(df):

    customer_orders = (
        df.groupby("Customer ID")
        .agg(
            Orders=("Order ID", "nunique"),
            Revenue=("Revenue", "sum")
        )
        .reset_index()
    )

    customer_orders["Customer Type"] = customer_orders["Orders"].apply(
        lambda x: "New Customer"
        if x == 1
        else "Returning Customer"
    )

    summary = (
        customer_orders
        .groupby(
            "Customer Type",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum")
        )
    )

    fig = px.bar(
        summary,
        x="Customer Type",
        y="Revenue",
        color="Customer Type",
        title="New vs Returning Customer Revenue"
    )

    return customer_chart_layout(fig)

