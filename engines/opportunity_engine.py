import pandas as pd

from ai_config import (
    CONFIDENCE_REGION,
    CONFIDENCE_CATEGORY,
    CONFIDENCE_MARGIN,
    REGION_GROWTH_FACTOR,
    CATEGORY_GROWTH_FACTOR,
)


# =====================================================
# TOP REGION OPPORTUNITY
# =====================================================

def best_region(df):

    if df is None or df.empty:
        return {
            "Region": "N/A",
            "Revenue": 0,
            "Potential": 0,
            "Confidence": 0,
        }

    required = {"Region", "Revenue"}

    if not required.issubset(df.columns):
        return {
            "Region": "N/A",
            "Revenue": 0,
            "Potential": 0,
            "Confidence": 0,
        }

    region = (
        df.groupby("Region", dropna=False)["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    if region.empty:
        return {
            "Region": "N/A",
            "Revenue": 0,
            "Potential": 0,
            "Confidence": 0,
        }

    top = region.iloc[0]

    return {
        "Region": top["Region"],
        "Revenue": float(top["Revenue"]),
        "Potential": float(top["Revenue"]) * REGION_GROWTH_FACTOR,
        "Confidence": CONFIDENCE_REGION,
    }


# =====================================================
# BEST CATEGORY
# =====================================================

def best_category(df):

    if df is None or df.empty:
        return {
            "Category": "N/A",
            "Revenue": 0,
            "Potential": 0,
            "Confidence": 0,
        }

    required = {"Category", "Revenue"}

    if not required.issubset(df.columns):
        return {
            "Category": "N/A",
            "Revenue": 0,
            "Potential": 0,
            "Confidence": 0,
        }

    category = (
        df.groupby("Category", dropna=False)["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    if category.empty:
        return {
            "Category": "N/A",
            "Revenue": 0,
            "Potential": 0,
            "Confidence": 0,
        }

    top = category.iloc[0]

    return {
        "Category": top["Category"],
        "Revenue": float(top["Revenue"]),
        "Potential": float(top["Revenue"]) * CATEGORY_GROWTH_FACTOR,
        "Confidence": CONFIDENCE_CATEGORY,
    }


# =====================================================
# HIGHEST PROFIT MARGIN
# =====================================================

def highest_margin(df):

    if df is None or df.empty:
        return {
            "Category": "N/A",
            "Margin": 0,
            "Confidence": 0,
        }

    required = {"Category", "Revenue", "Profit"}

    if not required.issubset(df.columns):
        return {
            "Category": "N/A",
            "Margin": 0,
            "Confidence": 0,
        }

    margin = (
        df.groupby("Category", dropna=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
        )
        .reset_index()
    )

    margin["Margin"] = (
        margin["Profit"]
        .div(margin["Revenue"].replace(0, pd.NA))
        .fillna(0)
        * 100
    )

    margin = margin.sort_values(
        "Margin",
        ascending=False,
    )

    if margin.empty:
        return {
            "Category": "N/A",
            "Margin": 0,
            "Confidence": 0,
        }

    top = margin.iloc[0]

    return {
        "Category": top["Category"],
        "Margin": round(float(top["Margin"]), 2),
        "Confidence": CONFIDENCE_MARGIN,
    }


# =====================================================
# LOWEST CATEGORY
# =====================================================

def weakest_category(df):

    if df is None or df.empty:
        return {
            "Category": "N/A",
            "Revenue": 0,
        }

    required = {"Category", "Revenue"}

    if not required.issubset(df.columns):
        return {
            "Category": "N/A",
            "Revenue": 0,
        }

    category = (
        df.groupby("Category", dropna=False)["Revenue"]
        .sum()
        .sort_values()
        .reset_index()
    )

    if category.empty:
        return {
            "Category": "N/A",
            "Revenue": 0,
        }

    low = category.iloc[0]

    return {
        "Category": low["Category"],
        "Revenue": float(low["Revenue"]),
    }