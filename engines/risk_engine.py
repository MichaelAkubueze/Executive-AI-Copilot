import pandas as pd

from ai_config import (
    DEFAULT_REVENUE_TARGET,
    HIGH_MARGIN,
    MEDIUM_MARGIN,
)


# =====================================================
# REVENUE RISK
# =====================================================

def revenue_risk(df):

    if df is None or df.empty or "Revenue" not in df.columns:
        return ("⚪ Unknown", 0)

    revenue = df["Revenue"].sum()

    achievement = (
        revenue / DEFAULT_REVENUE_TARGET
        if DEFAULT_REVENUE_TARGET > 0
        else 0
    )

    if achievement >= 0.90:
        return ("🟢 Low", achievement)

    elif achievement >= 0.75:
        return ("🟠 Medium", achievement)

    else:
        return ("🔴 High", achievement)


# =====================================================
# PROFIT MARGIN RISK
# =====================================================

def margin_risk(df):

    required = {"Revenue", "Profit"}

    if df is None or df.empty or not required.issubset(df.columns):
        return ("⚪ Unknown", 0)

    revenue = df["Revenue"].sum()
    profit = df["Profit"].sum()

    margin = (profit / revenue * 100) if revenue else 0

    if margin >= HIGH_MARGIN:
        return ("🟢 Low", margin)

    elif margin >= MEDIUM_MARGIN:
        return ("🟠 Medium", margin)

    else:
        return ("🔴 High", margin)


# =====================================================
# CUSTOMER CONCENTRATION RISK
# =====================================================

def customer_risk(df):

    required = {"Customer Name", "Revenue"}

    if df is None or df.empty or not required.issubset(df.columns):
        return ("⚪ Unknown", 0)

    revenue = (
        df.groupby("Customer Name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    if revenue.empty or revenue.sum() == 0:
        return ("⚪ Unknown", 0)

    concentration = revenue.iloc[0] / revenue.sum()

    if concentration < 0.10:
        return ("🟢 Low", concentration)

    elif concentration < 0.20:
        return ("🟠 Medium", concentration)

    else:
        return ("🔴 High", concentration)


# =====================================================
# CATEGORY RISK
# =====================================================

def category_risk(df):

    required = {"Category", "Revenue"}

    if df is None or df.empty or not required.issubset(df.columns):
        return {
            "Category": "N/A",
            "Revenue": 0,
            "Risk": "⚪ Unknown",
        }

    category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values()
        .reset_index()
    )

    if category.empty:
        return {
            "Category": "N/A",
            "Revenue": 0,
            "Risk": "⚪ Unknown",
        }

    lowest = category.iloc[0]

    return {
        "Category": lowest["Category"],
        "Revenue": float(lowest["Revenue"]),
        "Risk": "🔴 High",
    }