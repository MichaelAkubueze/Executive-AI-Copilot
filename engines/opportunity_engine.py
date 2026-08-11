import pandas as pd


# =====================================================
# TOP REGION OPPORTUNITY
# =====================================================

def best_region(df):

    region = (
        df.groupby("Region")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    top = region.iloc[0]

    return {
        "Region": top["Region"],
        "Revenue": top["Revenue"],
        "Potential": top["Revenue"] * 0.20,
        "Confidence": 95,
    }


# =====================================================
# BEST CATEGORY
# =====================================================

def best_category(df):

    category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    top = category.iloc[0]

    return {

        "Category": top["Category"],

        "Revenue": top["Revenue"],

        "Potential": top["Revenue"] * 0.15,

        "Confidence": 94,

    }


# =====================================================
# HIGHEST PROFIT MARGIN
# =====================================================

def highest_margin(df):

    margin = (

        df.groupby("Category")

        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum"),
        )

        .reset_index()

    )

    margin["Margin"] = (

        margin["Profit"]

        / margin["Revenue"]

        * 100

    )

    margin = margin.sort_values(

        "Margin",

        ascending=False,

    )

    top = margin.iloc[0]

    return {

        "Category": top["Category"],

        "Margin": top["Margin"],

    }


# =====================================================
# LOWEST CATEGORY
# =====================================================

def weakest_category(df):

    category = (

        df.groupby("Category")["Revenue"]

        .sum()

        .sort_values()

        .reset_index()

    )

    low = category.iloc[0]

    return {

        "Category": low["Category"],

        "Revenue": low["Revenue"],

    }