import pandas as pd

# ==========================================================
# IMPORT KPI ENGINE
# ==========================================================

from kpi import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_average_order,
    get_gross_margin,
    get_monthly_revenue,
    get_sales_by_region,
    get_sales_by_category,
    get_sales_by_channel,
    get_customer_segments,
    get_top_products,
    get_top_customers,
    get_salesperson_performance,
)

# ==========================================================
# MONTH OVER MONTH GROWTH
# ==========================================================

def get_mom_growth(df):

    monthly = (
        df.groupby(["Year", "Month"], as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Date=("Order Date", "min")
        )
        .sort_values("Date")
    )

    if len(monthly) < 2:
        return 0

    previous = monthly.iloc[-2]["Revenue"]
    current = monthly.iloc[-1]["Revenue"]

    if previous == 0:
        return 0

    return (current - previous) / previous


# ==========================================================
# YEAR OVER YEAR GROWTH
# ==========================================================

def get_yoy_growth(df):

    yearly = (
        df.groupby("Year", as_index=False)
        .agg(Revenue=("Revenue", "sum"))
        .sort_values("Year")
    )

    if len(yearly) < 2:
        return 0

    previous = yearly.iloc[-2]["Revenue"]
    current = yearly.iloc[-1]["Revenue"]

    if previous == 0:
        return 0

    return (current - previous) / previous


# ==========================================================
# CUSTOMER GROWTH
# ==========================================================

def customer_growth(df):

    yearly = (
        df.groupby("Year", as_index=False)
        .agg(Customers=("Customer ID", "nunique"))
        .sort_values("Year")
    )

    if len(yearly) < 2:
        return 0

    previous = yearly.iloc[-2]["Customers"]
    current = yearly.iloc[-1]["Customers"]

    if previous == 0:
        return 0

    return (current - previous) / previous


# ==========================================================
# ORDER GROWTH
# ==========================================================

def order_growth(df):

    yearly = (
        df.groupby("Year", as_index=False)
        .agg(Orders=("Order ID", "count"))
        .sort_values("Year")
    )

    if len(yearly) < 2:
        return 0

    previous = yearly.iloc[-2]["Orders"]
    current = yearly.iloc[-1]["Orders"]

    if previous == 0:
        return 0

    return (current - previous) / previous


# ==========================================================
# REVENUE TREND
# ==========================================================

def revenue_trend(df):

    return (
        df.groupby(["Year", "Month"], as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Date=("Order Date", "min")
        )
        .sort_values("Date")
    )


# ==========================================================
# PROFIT TREND
# ==========================================================

def profit_trend(df):

    return (
        df.groupby(["Year", "Month"], as_index=False)
        .agg(
            Profit=("Profit", "sum"),
            Date=("Order Date", "min")
        )
        .sort_values("Date")
    )
    
    