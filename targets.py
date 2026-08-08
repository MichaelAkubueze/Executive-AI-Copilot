import pandas as pd


TARGET_FILE = "data/EnterpriseSales.xlsm"


def load_targets():

    df = pd.read_excel(

        TARGET_FILE,

        sheet_name="tblTargets"

    )

    return df


def revenue_target(df):

    return df["Revenue Target"].sum()


def profit_target(df):

    return df["Profit Target"].sum()


def order_target(df):

    return df["Order Target"].sum()


def customer_target(df):

    return df["Customer Target"].sum()