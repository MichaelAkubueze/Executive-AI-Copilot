import pandas as pd
import plotly.express as px
from queries import run_query
import os

# ==========================================================
# MONTHLY REVENUE QUERY
# ==========================================================

query = """
SELECT

    Year,
    [Month],
    MIN([Order Date]) AS FirstOrderDate,
    SUM(Revenue) AS Revenue

FROM FactSales

GROUP BY

    Year,
    [Month]

ORDER BY

    MIN([Order Date])
"""

# Read data from SQL Server
df = run_query(query)

# ==========================================================
# CREATE MONTH-YEAR LABEL
# ==========================================================

df["Period"] = (
    df["Month"] + " " + df["Year"].astype(str)
)

# ==========================================================
# CREATE PLOTLY CHART
# ==========================================================

fig = px.line(
    df,
    x="Period",
    y="Revenue",
    color="Year",
    markers=True,
    title="Enterprise Monthly Revenue Trend"
)

fig.update_traces(
    line_width=4,
    marker_size=8
)

fig.update_layout(
    template="plotly_white",
    title_font_size=26,
    font=dict(size=14),
    
    xaxis=dict(
    tickangle=-45,
    nticks=20
),
    
    yaxis=dict(
    title="Revenue (₦)",
    tickprefix="₦",
    tickformat=",.0f"
),
    
    hovermode="x unified",
    legend_title="Year",
    width=1600,
    height=800
)

# ==========================================================
# SHOW CHART
# ==========================================================

fig.show()

# ==========================================================
# SAVE IMAGE FOR PORTFOLIO
# ==========================================================

os.makedirs("charts", exist_ok=True)

fig.write_image(
    "charts/monthly_revenue_trend.png",
    width=1920,
    height=1080,
    scale=2
)

fig.update_traces(
    hovertemplate=
    "<b>%{x}</b><br>" +
    "Revenue: ₦%{y:,.0f}<extra></extra>"
)

fig.update_layout(

    xaxis=dict(
        rangeslider=dict(visible=True)
    )

)

print("=" * 60)
print("SUCCESS!")
print("=" * 60)
print("Chart displayed successfully.")
print("Image saved to:")
print("charts/monthly_revenue_trend.png")