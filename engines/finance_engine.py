import pandas as pd


# ==========================================================
# FINANCE KPI ENGINE
# ==========================================================

def total_revenue(df):
    """Return total revenue."""

    return df["Revenue"].sum()


def total_cost(df):
    """Return total cost."""

    return df["Cost"].sum()


def total_profit(df):
    """Return total profit."""

    return df["Profit"].sum()


def gross_margin(df):
    """Return overall gross profit margin as a percentage."""

    revenue = df["Revenue"].sum()

    if revenue == 0:
        return 0

    return (
        df["Profit"].sum()
        / revenue
        * 100
    )


def total_shipping_cost(df):
    """Return total shipping cost."""

    if "Shipping Cost" not in df.columns:
        return 0

    return df["Shipping Cost"].sum()


def average_order_value(df):
    """Return average revenue per order."""

    orders = df["Order ID"].nunique()

    if orders == 0:
        return 0

    return (
        df["Revenue"].sum()
        / orders
    )


def average_profit_per_order(df):
    """Return average profit per order."""

    orders = df["Order ID"].nunique()

    if orders == 0:
        return 0

    return (
        df["Profit"].sum()
        / orders
    )


def profit_per_order(df):
    """Return profit generated per order."""

    orders = df["Order ID"].nunique()

    if orders == 0:
        return 0

    return (
        df["Profit"].sum()
        / orders
    )


# ==========================================================
# MONTHLY FINANCIAL PERFORMANCE
# ==========================================================

def monthly_financial_summary(df):

    summary = (
        df.groupby(
            "Month",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    return summary


# ==========================================================
# REGIONAL FINANCIAL PERFORMANCE
# ==========================================================

def regional_financial_summary(df):

    summary = (
        df.groupby(
            "Region",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    return summary.sort_values(
        "Revenue",
        ascending=False
    )


# ==========================================================
# CATEGORY FINANCIAL PERFORMANCE
# ==========================================================

def category_financial_summary(df):

    summary = (
        df.groupby(
            "Category",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    return summary.sort_values(
        "Revenue",
        ascending=False
    )


# ==========================================================
# PAYMENT CHANNEL FINANCIAL PERFORMANCE
# ==========================================================

def payment_financial_summary(df):

    summary = (
        df.groupby(
            "Payment Method",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    return summary.sort_values(
        "Revenue",
        ascending=False
    )


# ==========================================================
# SALES CHANNEL FINANCIAL PERFORMANCE
# ==========================================================

def channel_financial_summary(df):

    summary = (
        df.groupby(
            "Sales Channel",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    return summary.sort_values(
        "Revenue",
        ascending=False
    )


# ==========================================================
# TOP PROFITABLE PRODUCTS
# ==========================================================

def top_profitable_products(df, limit=20):

    summary = (
        df.groupby(
            "Product Name",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    return (
        summary
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(limit)
        .reset_index(drop=True)
    )


# ==========================================================
# FINANCIAL RANKING
# ==========================================================

def financial_ranking(df):

    summary = (
        df.groupby(
            "Region",
            as_index=False
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
    )

    summary["Profit Margin"] = (
        summary["Profit"]
        / summary["Revenue"]
        * 100
    )

    summary = summary.sort_values(
        "Profit",
        ascending=False
    ).reset_index(drop=True)

    summary.insert(
        0,
        "Rank",
        range(
            1,
            len(summary) + 1
        )
    )

    return summary

