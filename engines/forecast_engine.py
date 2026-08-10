import pandas as pd

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
)


# ===========================================
# MONTHLY AGGREGATION
# ===========================================

def monthly_summary(df):

    summary = (
        df.groupby("Month", as_index=False)
          .agg(
              Revenue=("Revenue", "sum"),
              Profit=("Profit", "sum"),
              Orders=("Order ID", "count"),
          )
    )

    return summary


# ===========================================
# SIMPLE MOVING AVERAGE FORECAST
# ===========================================

def forecast_next_month(df):

    monthly = monthly_summary(df)

    revenue = monthly["Revenue"].tail(3).mean()

    profit = monthly["Profit"].tail(3).mean()

    orders = monthly["Orders"].tail(3).mean()

    return {

        "Revenue": revenue,

        "Profit": profit,

        "Orders": orders,

    }


# ===========================================
# EXECUTIVE FORECAST SUMMARY
# ===========================================

def executive_forecast(df):

    forecast = forecast_next_month(df)

    return f"""
### 🔮 Next Month Forecast

Expected Revenue

₦{forecast['Revenue']:,.2f}

Expected Profit

₦{forecast['Profit']:,.2f}

Expected Orders

{forecast['Orders']:,.0f}

Forecast generated using a 3-month moving average.
"""

