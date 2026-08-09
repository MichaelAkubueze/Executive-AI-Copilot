import pandas as pd


# ==========================================================
# MONTH OVER MONTH (MoM) REVENUE
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

    current = monthly.iloc[-1]["Revenue"]
    previous = monthly.iloc[-2]["Revenue"]

    if previous == 0:
        return 0

    return ((current - previous) / previous)


# ==========================================================
# YEAR OVER YEAR (YoY)
# ==========================================================

def get_yoy_growth(df):

    yearly = (
        df.groupby("Year", as_index=False)
          .agg(
              Revenue=("Revenue", "sum")
          )
          .sort_values("Year")
    )

    if len(yearly) < 2:
        return 0

    current = yearly.iloc[-1]["Revenue"]
    previous = yearly.iloc[-2]["Revenue"]

    if previous == 0:
        return 0

    return ((current - previous) / previous)


# ==========================================================
# REVENUE TREND
# ==========================================================

def revenue_trend(df):

    monthly = (
        df.groupby(["Year", "Month"], as_index=False)
          .agg(
              Revenue=("Revenue", "sum"),
              Date=("Order Date", "min")
          )
          .sort_values("Date")
    )

    return monthly


# ==========================================================
# PROFIT TREND
# ==========================================================

def profit_trend(df):

    monthly = (
        df.groupby(["Year", "Month"], as_index=False)
          .agg(
              Profit=("Profit", "sum"),
              Date=("Order Date", "min")
          )
          .sort_values("Date")
    )

    return monthly


# ==========================================================
# CUSTOMER GROWTH
# ==========================================================

def customer_growth(df):

    customers = (
        df.groupby("Year", as_index=False)
          .agg(
              Customers=("Customer ID", "nunique")
          )
          .sort_values("Year")
    )

    if len(customers) < 2:
        return 0

    current = customers.iloc[-1]["Customers"]
    previous = customers.iloc[-2]["Customers"]

    if previous == 0:
        return 0

    return ((current - previous) / previous)


# ==========================================================
# ORDER GROWTH
# ==========================================================

def order_growth(df):

    orders = (
        df.groupby("Year", as_index=False)
          .agg(
              Orders=("Order ID", "count")
          )
          .sort_values("Year")
    )

    if len(orders) < 2:
        return 0

    current = orders.iloc[-1]["Orders"]
    previous = orders.iloc[-2]["Orders"]

    if previous == 0:
        return 0

    return ((current - previous) / previous)

# ==========================================================
# SALES BY REGION (RAW DATA)
# ==========================================================

def get_sales_by_region(df):

    return (
        df.groupby("Region", as_index=False)
          .agg(
              Revenue=("Revenue", "sum")
          )
          .sort_values("Revenue", ascending=False)
    )


# ==========================================================
# SALES BY CATEGORY (RAW DATA)
# ==========================================================

def get_sales_by_category(df):

    return (
        df.groupby("Category", as_index=False)
          .agg(
              Revenue=("Revenue", "sum")
          )
          .sort_values("Revenue", ascending=False)
    )