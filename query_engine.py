from executive import executive_metrics

from analytics import (
    get_sales_by_region,
    get_sales_by_category,
)


class QueryEngine:

    def __init__(self, df):
        self.df = df
        self.metrics = executive_metrics(df)

    # -----------------------------------------
    # KPI METRICS
    # -----------------------------------------

    def revenue(self):
        return self.metrics.get("Revenue", 0)

    # -----------------------------------------

    def profit(self):
        return self.metrics.get("Profit", 0)

    # -----------------------------------------

    def margin(self):
        return self.metrics.get("Gross Margin", 0)

    # -----------------------------------------

    def customers(self):
        return self.metrics.get("Customers", 0)

    # -----------------------------------------

    def orders(self):
        return self.metrics.get("Orders", 0)

    # -----------------------------------------
    # REGION
    # -----------------------------------------

    def best_region(self):

        region = get_sales_by_region(self.df)

        if region is None or region.empty:
            return {
                "Region": "N/A",
                "Revenue": 0,
            }

        return region.iloc[0].to_dict()

    # -----------------------------------------
    # CATEGORY
    # -----------------------------------------

    def best_category(self):

        category = get_sales_by_category(self.df)

        if category is None or category.empty:
            return {
                "Category": "N/A",
                "Revenue": 0,
            }

        return category.iloc[0].to_dict()