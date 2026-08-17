import plotly.express as px


# ==========================================================
# DASHBOARD CHART LAYOUT
# ==========================================================

def dashboard_chart_layout(fig):

    fig.update_layout(
        template="plotly_white",
        height=400,
        margin=dict(
            l=40,
            r=40,
            t=70,
            b=40,
        ),
        legend_title_text="",
    )

    return fig


# ==========================================================
# MONTHLY REVENUE TREND
# ==========================================================

def monthly_revenue_chart(df):

    from engines.dashboard_engine import (
        monthly_performance,
    )

    data = monthly_performance(df)

    fig = px.line(
        data,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return dashboard_chart_layout(fig)


# ==========================================================
# MONTHLY PROFIT TREND
# ==========================================================

def monthly_profit_chart(df):

    from engines.dashboard_engine import (
        monthly_performance,
    )

    data = monthly_performance(df)

    fig = px.line(
        data,
        x="Month",
        y="Profit",
        markers=True,
        title="Monthly Profit Trend",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return dashboard_chart_layout(fig)


# ==========================================================
# REGIONAL REVENUE
# ==========================================================

def regional_revenue_chart(df):

    from engines.dashboard_engine import (
        regional_performance,
    )

    data = regional_performance(df)

    fig = px.bar(
        data,
        x="Region",
        y="Revenue",
        title="Revenue by Region",
        text_auto=".2s",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return dashboard_chart_layout(fig)


# ==========================================================
# CATEGORY REVENUE
# ==========================================================

def category_revenue_chart(df):

    from engines.dashboard_engine import (
        category_performance,
    )

    data = category_performance(df)

    fig = px.bar(
        data,
        x="Category",
        y="Revenue",
        title="Revenue by Category",
        text_auto=".2s",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return dashboard_chart_layout(fig)


# ==========================================================
# CATEGORY PROFIT
# ==========================================================

def category_profit_chart(df):

    from engines.dashboard_engine import (
        category_performance,
    )

    data = category_performance(df)

    fig = px.bar(
        data,
        x="Category",
        y="Profit",
        title="Profit by Category",
        text_auto=".2s",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return dashboard_chart_layout(fig)


# ==========================================================
# REGIONAL PROFIT
# ==========================================================

def regional_profit_chart(df):

    from engines.dashboard_engine import (
        regional_performance,
    )

    data = regional_performance(df)

    fig = px.bar(
        data,
        x="Region",
        y="Profit",
        title="Profit by Region",
        text_auto=".2s",
    )

    fig.update_yaxes(
        tickprefix="₦",
        tickformat=",.0f",
    )

    return dashboard_chart_layout(fig)
