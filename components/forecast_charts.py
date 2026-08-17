import pandas as pd
import plotly.express as px

# ===========================================
# FORECAST CHART LAYOUT
# ===========================================

def forecast_chart_layout(fig):

    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(
            l=40,
            r=40,
            t=70,
            b=40,
        ),
        legend_title_text="",
    )

    return fig


# ===========================================
# REVENUE FORECAST CHART
# ===========================================

def revenue_forecast_chart(df):

    from engines.forecast_engine import (
        monthly_summary,
        forecast_next_month,
    )

    monthly = monthly_summary(df)

    if monthly.empty:
        return px.line(
            title="Revenue Forecast"
        )

    historical = monthly[
        ["Month", "Revenue"]
    ].copy()

    historical["Type"] = "Historical"

    forecast = forecast_next_month(df)

    next_month = pd.DataFrame(
        [{
            "Month": "Next Month",
            "Revenue": forecast["Revenue"],
            "Type": "Forecast",
        }]
    )

    chart_data = pd.concat(
        [
            historical,
            next_month,
        ],
        ignore_index=True,
    )

    fig = px.line(
        chart_data,
        x="Month",
        y="Revenue",
        color="Type",
        markers=True,
        title="Revenue — Historical vs Forecast",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return forecast_chart_layout(fig)


# ===========================================
# PROFIT FORECAST CHART
# ===========================================

def profit_forecast_chart(df):

    from engines.forecast_engine import (
        monthly_summary,
        forecast_next_month,
    )

    monthly = monthly_summary(df)

    if monthly.empty:
        return px.line(
            title="Profit Forecast"
        )

    historical = monthly[
        ["Month", "Profit"]
    ].copy()

    historical["Type"] = "Historical"

    forecast = forecast_next_month(df)

    next_month = pd.DataFrame(
        [{
            "Month": "Next Month",
            "Profit": forecast["Profit"],
            "Type": "Forecast",
        }]
    )

    chart_data = pd.concat(
        [
            historical.rename(
                columns={
                    "Profit": "Value"
                }
            )
        ],
        ignore_index=True,
    )

    forecast_data = next_month.rename(
        columns={
            "Profit": "Value"
        }
    )

    chart_data = pd.concat(
        [
            chart_data,
            forecast_data,
        ],
        ignore_index=True,
    )

    fig = px.line(
        chart_data,
        x="Month",
        y="Value",
        color="Type",
        markers=True,
        title="Profit — Historical vs Forecast",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return forecast_chart_layout(fig)


# ===========================================
# ORDERS FORECAST CHART
# ===========================================

def orders_forecast_chart(df):

    from engines.forecast_engine import (
        monthly_summary,
        forecast_next_month,
    )

    monthly = monthly_summary(df)

    if monthly.empty:
        return px.line(
            title="Orders Forecast"
        )

    historical = monthly[
        ["Month", "Orders"]
    ].copy()

    historical["Type"] = "Historical"

    forecast = forecast_next_month(df)

    next_month = pd.DataFrame(
        [{
            "Month": "Next Month",
            "Orders": forecast["Orders"],
            "Type": "Forecast",
        }]
    )

    chart_data = pd.concat(
        [
            historical,
            next_month,
        ],
        ignore_index=True,
    )

    fig = px.line(
        chart_data,
        x="Month",
        y="Orders",
        color="Type",
        markers=True,
        title="Orders — Historical vs Forecast",
    )

    fig.update_yaxes(
        tickformat=",.0f",
    )

    return forecast_chart_layout(fig)
