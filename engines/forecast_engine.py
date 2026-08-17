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
# ===========================================
# FORECAST TREND
# ===========================================

def forecast_growth(df):

    monthly = monthly_summary(df)

    if len(monthly) < 2:
        return 0

    previous = monthly["Revenue"].iloc[-2]
    current = monthly["Revenue"].iloc[-1]

    if previous == 0:
        return 0

    growth = (
        (current - previous)
        / previous
        * 100
    )

    return growth


# ===========================================
# FORECAST STATUS
# ===========================================

def forecast_status(df):

    growth = forecast_growth(df)

    if growth >= 10:
        return "Strong Growth"

    elif growth >= 5:
        return "Moderate Growth"

    elif growth >= 0:
        return "Stable"

    elif growth >= -5:
        return "Moderate Decline"

    else:
        return "Declining"


# ===========================================
# FORECAST DATA
# ===========================================

def forecast_data(df):

    monthly = monthly_summary(df)

    forecast = forecast_next_month(df)

    result = monthly.copy()

    next_month = pd.DataFrame(
        [{
            "Month": "Next Month",
            "Revenue": forecast["Revenue"],
            "Profit": forecast["Profit"],
            "Orders": forecast["Orders"],
        }]
    )

    result = pd.concat(
        [
            result,
            next_month
        ],
        ignore_index=True
    )

    return result

# ===========================================
# FORECAST TREND
# ===========================================

def forecast_growth(df):

    monthly = monthly_summary(df)

    if len(monthly) < 2:
        return 0

    previous = monthly["Revenue"].iloc[-2]
    current = monthly["Revenue"].iloc[-1]

    if previous == 0:
        return 0

    growth = (
        (current - previous)
        / previous
        * 100
    )

    return growth


# ===========================================
# FORECAST STATUS
# ===========================================

def forecast_status(df):

    growth = forecast_growth(df)

    if growth >= 10:
        return "Strong Growth"

    elif growth >= 5:
        return "Moderate Growth"

    elif growth >= 0:
        return "Stable"

    elif growth >= -5:
        return "Moderate Decline"

    else:
        return "Declining"


# ===========================================
# FORECAST DATA
# ===========================================

def forecast_data(df):

    monthly = monthly_summary(df)

    forecast = forecast_next_month(df)

    next_month = pd.DataFrame(
        [{
            "Month": "Next Month",
            "Revenue": forecast["Revenue"],
            "Profit": forecast["Profit"],
            "Orders": forecast["Orders"],
        }]
    )

    result = pd.concat(
        [
            monthly,
            next_month
        ],
        ignore_index=True
    )

    return result



