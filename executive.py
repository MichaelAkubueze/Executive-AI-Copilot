import pandas as pd

from kpi import *

from analytics import *

from targets import (
    load_targets,
    revenue_target,
    profit_target,
    order_target,
    customer_target,
)


def executive_metrics(df):

    targets = load_targets()

    return {

        "Revenue": get_total_revenue(df),

        "Profit": get_total_profit(df),

        "Orders": get_total_orders(df),

        "Customers": get_total_customers(df),

        "Average Order": get_average_order(df),

        "Gross Margin": get_gross_margin(df),

        "MoM Growth": get_mom_growth(df),

        "YoY Growth": get_yoy_growth(df),

        "Customer Growth": customer_growth(df),

        "Order Growth": order_growth(df),

        "Revenue Target": revenue_target(targets),

        "Profit Target": profit_target(targets),

        "Order Target": order_target(targets),

        "Customer Target": customer_target(targets),

    }