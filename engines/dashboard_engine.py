import pandas as pd


# ==========================================================
# EXECUTIVE DASHBOARD ENGINE
# ==========================================================


def dashboard_kpis(df):
    """
    Return the core executive dashboard KPIs.
    """

    revenue = df["Revenue"].sum()

    profit = df["Profit"].sum()

    orders = df["Order ID"].nunique()

    customers = df["Customer ID"].nunique()

    margin = (
        profit / revenue * 100
        if revenue != 0
        else 0
    )

    return {
        "Revenue": revenue,
        "Profit": profit,
        "Orders": orders,
        "Customers": customers,
        "Margin": margin,
    }


# ==========================================================
# BEST REGION
# ==========================================================

def best_region(df):

    if df.empty:
        return "N/A"

    region = (
        df.groupby("Region")["Revenue"]
        .sum()
        .idxmax()
    )

    return region


# ==========================================================
# BEST CATEGORY
# ==========================================================

def best_category(df):

    if df.empty:
        return "N/A"

    category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .idxmax()
    )

    return category


# ==========================================================
# TOP PRODUCT
# ==========================================================

def top_product(df):

    if df.empty:
        return "N/A"

    product = (
        df.groupby("Product Name")["Revenue"]
        .sum()
        .idxmax()
    )

    return product


# ==========================================================
# TOP CUSTOMER
# ==========================================================

def top_customer(df):

    if df.empty:
        return "N/A"

    customer = (
        df.groupby("Customer Name")["Revenue"]
        .sum()
        .idxmax()
    )

    return customer


# ==========================================================
# TOP SALESPERSON
# ==========================================================

def top_salesperson(df):

    if df.empty:
        return "N/A"

    salesperson = (
        df.groupby("Salesperson")["Revenue"]
        .sum()
        .idxmax()
    )

    return salesperson


# ==========================================================
# REGIONAL PERFORMANCE
# ==========================================================

def regional_performance(df):

    summary = (
        df.groupby("Region", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
        )
        .sort_values(
            "Revenue",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    return summary


# ==========================================================
# CATEGORY PERFORMANCE
# ==========================================================

def category_performance(df):

    summary = (
        df.groupby("Category", as_index=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
        )
        .sort_values(
            "Revenue",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    return summary


# ==========================================================
# MONTHLY PERFORMANCE
# ==========================================================

def monthly_performance(df):

    data = df.copy()

    data["Order Date"] = pd.to_datetime(
        data["Order Date"]
    )

    summary = (
        data.groupby(
            data["Order Date"].dt.to_period("M")
        )
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
        )
        .reset_index()
    )

    summary["Month"] = (
        summary["Order Date"]
        .astype(str)
    )

    summary = summary.drop(
        columns=["Order Date"]
    )

    return summary


# ==========================================================
# EXECUTIVE HIGHLIGHTS
# ==========================================================

def executive_highlights(df):

    kpis = dashboard_kpis(df)

    return {
        "Revenue": kpis["Revenue"],
        "Profit": kpis["Profit"],
        "Orders": kpis["Orders"],
        "Customers": kpis["Customers"],
        "Margin": kpis["Margin"],
        "Best Region": best_region(df),
        "Best Category": best_category(df),
        "Top Product": top_product(df),
        "Top Customer": top_customer(df),
        "Top Salesperson": top_salesperson(df),
    }
    
    