from analytics import (
    get_sales_by_region,
    get_sales_by_category,
)


def region_insight(df):

    region_df = get_sales_by_region(df)

    return {
        "best": region_df.iloc[0],
        "worst": region_df.iloc[-1],
    }


def category_insight(df):

    category_df = get_sales_by_category(df)

    return {
        "best": category_df.iloc[0],
        "worst": category_df.iloc[-1],
    }