from analytics import (
    get_sales_by_region,
    get_sales_by_category,
)


# =====================================================
# REGION INSIGHTS
# =====================================================

def region_insight(df):

    region_df = get_sales_by_region(df)

    if region_df is None or region_df.empty:
        return {
            "best": {
                "Region": "N/A",
                "Revenue": 0,
            },
            "worst": {
                "Region": "N/A",
                "Revenue": 0,
            },
        }

    return {
        "best": region_df.iloc[0].to_dict(),
        "worst": region_df.iloc[-1].to_dict(),
    }


# =====================================================
# CATEGORY INSIGHTS
# =====================================================

def category_insight(df):

    category_df = get_sales_by_category(df)

    if category_df is None or category_df.empty:
        return {
            "best": {
                "Category": "N/A",
                "Revenue": 0,
            },
            "worst": {
                "Category": "N/A",
                "Revenue": 0,
            },
        }

    return {
        "best": category_df.iloc[0].to_dict(),
        "worst": category_df.iloc[-1].to_dict(),
    }