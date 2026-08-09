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

    def revenue(self):

        return self.metrics["Revenue"]

    # -----------------------------------------

    def profit(self):

        return self.metrics["Profit"]

    # -----------------------------------------

    def margin(self):

        return self.metrics["Gross Margin"]

    # -----------------------------------------

    def customers(self):

        return self.metrics["Customers"]

    # -----------------------------------------

    def orders(self):

        return self.metrics["Orders"]

    # -----------------------------------------

    def best_region(self):

        return get_sales_by_region(self.df).iloc[0]

    # -----------------------------------------

    def best_category(self):

        return get_sales_by_category(self.df).iloc[0]