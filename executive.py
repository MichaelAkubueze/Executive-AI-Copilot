import pandas as pd


def executive_summary(df):

    revenue = df["Revenue"].sum()

    profit = df["Profit"].sum()

    orders = len(df)

    customers = df["Customer ID"].nunique()

    margin = df["Profit Margin %"].mean()

    best_region = (
        df.groupby("Region")["Revenue"]
        .sum()
        .idxmax()
    )

    best_category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .idxmax()
    )

    best_salesperson = (
        df.groupby("Salesperson")["Revenue"]
        .sum()
        .idxmax()
    )

    biggest_customer = (
        df.groupby("Customer Name")["Revenue"]
        .sum()
        .idxmax()
    )

    fastest_month = (
        df.groupby("Month")["Revenue"]
        .sum()
        .idxmax()
    )

    return {

        "Revenue": revenue,

        "Profit": profit,

        "Orders": orders,

        "Customers": customers,

        "Margin": margin,

        "Best Region": best_region,

        "Best Category": best_category,

        "Best Salesperson": best_salesperson,

        "Biggest Customer": biggest_customer,

        "Fastest Month": fastest_month,

    }