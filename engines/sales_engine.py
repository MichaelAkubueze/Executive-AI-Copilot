import pandas as pd



# ==========================================================
# KPI FUNCTIONS
# ==========================================================

def total_revenue(df):
    return df["Revenue"].sum()


def total_profit(df):
    return df["Profit"].sum()


def total_orders(df):
    return len(df)


def total_customers(df):
    return df["Customer ID"].nunique()


def gross_margin(df):

    revenue = total_revenue(df)

    if revenue == 0:
        return 0

    return total_profit(df) / revenue


# ==========================================================
# BUSINESS RANKINGS
# ==========================================================

def best_region(df):

    return (
        df.groupby("Region")["Revenue"]
        .sum()
        .idxmax()
    )


def best_category(df):

    return (
        df.groupby("Category")["Revenue"]
        .sum()
        .idxmax()
    )


def top_customer(df):

    return (
        df.groupby("Customer Name")["Revenue"]
        .sum()
        .idxmax()
    )


def top_salesperson(df):

    return (
        df.groupby("Salesperson")["Revenue"]
        .sum()
        .idxmax()
    )
    
    