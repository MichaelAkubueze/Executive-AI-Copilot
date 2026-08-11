import pandas as pd


def revenue_risk(df):

    revenue = df["Revenue"].sum()

    target = 100_000_000

    achievement = revenue / target

    if achievement >= 0.90:

        return ("🟢 Low", achievement)

    elif achievement >= 0.75:

        return ("🟠 Medium", achievement)

    else:

        return ("🔴 High", achievement)


def margin_risk(df):

    revenue = df["Revenue"].sum()

    profit = df["Profit"].sum()

    margin = (profit / revenue) * 100

    if margin >= 25:

        return ("🟢 Low", margin)

    elif margin >= 20:

        return ("🟠 Medium", margin)

    else:

        return ("🔴 High", margin)


def customer_risk(df):

    revenue = (

        df.groupby("Customer Name")["Revenue"]

        .sum()

        .sort_values(ascending=False)

    )

    concentration = revenue.iloc[0] / revenue.sum()

    if concentration < 0.10:

        return ("🟢 Low", concentration)

    elif concentration < 0.20:

        return ("🟠 Medium", concentration)

    else:

        return ("🔴 High", concentration)


def category_risk(df):

    category = (

        df.groupby("Category")["Revenue"]

        .sum()

        .sort_values()

    )

    return category.index[0]