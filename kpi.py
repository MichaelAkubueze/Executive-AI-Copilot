# ==========================================================
# kpi.py
# Enterprise Sales Analytics KPI Engine
# MICT E-LEARNING SERVICES LTD
# ==========================================================

import pandas as pd

# ==========================================================
# TOTAL REVENUE
# ==========================================================

def get_total_revenue(df):
    if df.empty:
        return 0

    return float(df["Revenue"].sum())


# ==========================================================
# TOTAL PROFIT
# ==========================================================

def get_total_profit(df):
    if df.empty:
        return 0

    return float(df["Profit"].sum())


# ==========================================================
# TOTAL ORDERS
# ==========================================================

def get_total_orders(df):
    if df.empty:
        return 0

    return int(len(df))


# ==========================================================
# TOTAL CUSTOMERS
# ==========================================================

def get_total_customers(df):
    if df.empty:
        return 0

    return int(df["Customer ID"].nunique())


# ==========================================================
# AVERAGE ORDER VALUE
# ==========================================================

def get_average_order(df):
    if df.empty:
        return 0

    return float(df["Revenue"].mean())


# ==========================================================
# GROSS MARGIN
# ==========================================================

def get_gross_margin(df):
    """
    Returns the overall gross profit margin (%).

    Uses the existing 'Profit Margin %' column if available.
    Otherwise calculates it from Revenue and Profit.
    """

    if df is None or df.empty:
        return 0.0

    # Use existing margin column if available
    if "Profit Margin %" in df.columns:
        return float(df["Profit Margin %"].fillna(0).mean())

    # Calculate margin if the column does not exist
    if "Revenue" not in df.columns or "Profit" not in df.columns:
        return 0.0

    revenue = df["Revenue"].sum()
    profit = df["Profit"].sum()

    if revenue == 0:
        return 0.0

    return round((profit / revenue) * 100, 2)


# ==========================================================
# MONTHLY REVENUE
# ==========================================================

def get_monthly_revenue(df):

    if df.empty:
        return pd.DataFrame()

    monthly = (
        df.groupby(["Year", "Month"], as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "count"),
            SortDate=("Order Date", "min")
        )
        .sort_values("SortDate")
    )

    return monthly


# ==========================================================
# SALES BY REGION
# ==========================================================

def get_sales_by_region(df):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Region", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values("Revenue", ascending=False)
    )


# ==========================================================
# SALES BY CATEGORY
# ==========================================================

def get_sales_by_category(df):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Category", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values("Revenue", ascending=False)
    )


# ==========================================================
# SALES BY CHANNEL
# ==========================================================

def get_sales_by_channel(df):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Sales Channel", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values("Revenue", ascending=False)
    )


# ==========================================================
# CUSTOMER SEGMENTS
# ==========================================================

def get_customer_segments(df):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Customer Segment", as_index=False)
        .agg(
            Customers=("Customer ID", "count")
        )
        .sort_values("Customers", ascending=False)
    )


# ==========================================================
# TOP PRODUCTS
# ==========================================================

def get_top_products(df, top_n=10):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Product Name", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values("Revenue", ascending=False)
        .head(top_n)
    )


# ==========================================================
# TOP CUSTOMERS
# ==========================================================

def get_top_customers(df, top_n=10):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Customer Name", as_index=False)
        .agg(
            Revenue=("Revenue", "sum")
        )
        .sort_values("Revenue", ascending=False)
        .head(top_n)
    )


# ==========================================================
# SALES BY SALESPERSON
# ==========================================================

def get_salesperson_performance(df):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Salesperson", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "count")
        )
        .sort_values("Revenue", ascending=False)
    )