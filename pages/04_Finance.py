import streamlit as st

from database import load_sales_data
from components.sidebar import render_sidebar
from engines.finance_ai import generate_finance_insights
from reports.finance_report import create_finance_report

from engines.finance_engine import (
    total_revenue,
    total_cost,
    total_profit,
    gross_margin,
    total_shipping_cost,
    average_order_value,
    average_profit_per_order,
    monthly_financial_summary,
    regional_financial_summary,
    category_financial_summary,
    payment_financial_summary,
    channel_financial_summary,
    top_profitable_products,
    financial_ranking,
)

from components.finance_charts import (
    monthly_financial_chart,
    revenue_vs_profit_chart,
    monthly_profit_margin_chart,
    regional_financial_chart,
    regional_profit_margin_chart,
    category_financial_chart,
    payment_method_chart,
    sales_channel_financial_chart,
    top_profitable_products_chart,
    cost_structure_chart,
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Finance Analytics",
    page_icon="💰",
    layout="wide",
)


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("💰 Finance Analytics")

st.caption(
    "Enterprise Financial Performance Intelligence"
)


# ==========================================================
# LOAD DATA
# ==========================================================

df = load_sales_data()

df = render_sidebar(df)


# ==========================================================
# FINANCE KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Revenue",
        f"₦{total_revenue(df):,.0f}"
    )

with k2:
    st.metric(
        "Cost",
        f"₦{total_cost(df):,.0f}"
    )

with k3:
    st.metric(
        "Profit",
        f"₦{total_profit(df):,.0f}"
    )

with k4:
    st.metric(
        "Profit Margin",
        f"{gross_margin(df):.2f}%"
    )


# ==========================================================
# FINANCIAL PERFORMANCE
# ==========================================================

st.divider()

st.subheader("📈 Financial Performance")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        monthly_financial_chart(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        revenue_vs_profit_chart(df),
        use_container_width=True
    )


# ==========================================================
# PROFITABILITY TREND
# ==========================================================

st.divider()

st.subheader("🎯 Profitability Analysis")

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        monthly_profit_margin_chart(df),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        cost_structure_chart(df),
        use_container_width=True
    )


# ==========================================================
# REGIONAL FINANCIAL ANALYSIS
# ==========================================================

st.divider()

st.subheader("🌍 Regional Financial Analysis")

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(
        regional_financial_chart(df),
        use_container_width=True
    )

with col6:
    st.plotly_chart(
        regional_profit_margin_chart(df),
        use_container_width=True
    )


# ==========================================================
# CATEGORY FINANCIAL ANALYSIS
# ==========================================================

st.divider()

st.subheader("🏷️ Category Financial Analysis")

st.plotly_chart(
    category_financial_chart(df),
    use_container_width=True
)


# ==========================================================
# SALES CHANNEL & PAYMENT ANALYSIS
# ==========================================================

st.divider()

st.subheader("💳 Commercial Financial Analysis")

col7, col8 = st.columns(2)

with col7:
    st.plotly_chart(
        payment_method_chart(df),
        use_container_width=True
    )

with col8:
    st.plotly_chart(
        sales_channel_financial_chart(df),
        use_container_width=True
    )


# ==========================================================
# TOP PROFITABLE PRODUCTS
# ==========================================================

st.divider()

st.subheader("🏆 Top Profitable Products")

st.plotly_chart(
    top_profitable_products_chart(df),
    use_container_width=True
)


# ==========================================================
# FINANCIAL EXECUTIVE SUMMARY
# ==========================================================

st.divider()

st.subheader("📋 Financial Executive Summary")

revenue = total_revenue(df)
cost = total_cost(df)
profit = total_profit(df)
margin = gross_margin(df)

best_region = (
    df.groupby("Region")["Profit"]
    .sum()
    .idxmax()
)

best_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .idxmax()
)

best_product = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .idxmax()
)

st.info(
    f"""
### Financial Overview

- **Total Revenue:** ₦{revenue:,.0f}
- **Total Cost:** ₦{cost:,.0f}
- **Total Profit:** ₦{profit:,.0f}
- **Profit Margin:** {margin:.2f}%
- **Shipping Cost:** ₦{total_shipping_cost(df):,.0f}
- **Average Order Value:** ₦{average_order_value(df):,.0f}
- **Average Profit per Order:** ₦{average_profit_per_order(df):,.0f}

### Financial Highlights

🌍 **Most Profitable Region:** {best_region}

🏷️ **Most Profitable Category:** {best_category}

🏆 **Most Profitable Product:** {best_product}

The financial position reflects the relationship between revenue,
cost, and profit across the enterprise. Continued monitoring of
regional, category, and product profitability will support stronger
financial decision-making.
"""
)


# ==========================================================
# REGIONAL FINANCIAL TABLE
# ==========================================================

st.divider()

st.subheader("🌍 Regional Financial Summary")

regional_summary = regional_financial_summary(df)

st.dataframe(
    regional_summary,
    use_container_width=True,
    hide_index=True,
    column_config={

        "Region": st.column_config.TextColumn(
            "Region",
            width="medium"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₦%,.2f"
        ),

        "Cost": st.column_config.NumberColumn(
            "Cost",
            format="₦%,.2f"
        ),

        "Profit": st.column_config.NumberColumn(
            "Profit",
            format="₦%,.2f"
        ),

        "Profit Margin": st.column_config.NumberColumn(
            "Profit Margin",
            format="%.2f%%"
        ),
    }
)


# ==========================================================
# CATEGORY FINANCIAL TABLE
# ==========================================================

st.divider()

st.subheader("🏷️ Category Financial Summary")

category_summary = category_financial_summary(df)

st.dataframe(
    category_summary,
    use_container_width=True,
    hide_index=True,
    column_config={

        "Category": st.column_config.TextColumn(
            "Category",
            width="medium"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₦%,.2f"
        ),

        "Cost": st.column_config.NumberColumn(
            "Cost",
            format="₦%,.2f"
        ),

        "Profit": st.column_config.NumberColumn(
            "Profit",
            format="₦%,.2f"
        ),

        "Profit Margin": st.column_config.NumberColumn(
            "Profit Margin",
            format="%.2f%%"
        ),
    }
)


# ==========================================================
# FINANCIAL RANKING
# ==========================================================

st.divider()

st.subheader("🏆 Regional Profitability Ranking")

ranking = financial_ranking(df)

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True,
    column_config={

        "Rank": st.column_config.NumberColumn(
            "Rank",
            width="small"
        ),

        "Region": st.column_config.TextColumn(
            "Region",
            width="medium"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₦%,.2f"
        ),

        "Cost": st.column_config.NumberColumn(
            "Cost",
            format="₦%,.2f"
        ),

        "Profit": st.column_config.NumberColumn(
            "Profit",
            format="₦%,.2f"
        ),

        "Profit Margin": st.column_config.NumberColumn(
            "Profit Margin",
            format="%.2f%%"
        ),
    }
)

# ==========================================================
# AI FINANCIAL INTELLIGENCE
# ==========================================================

st.divider()

st.subheader("🧠 AI Financial Intelligence")

finance_insight = generate_finance_insights(df)

left, right = st.columns([2, 1])


# ==========================================================
# EXECUTIVE FINANCIAL SUMMARY
# ==========================================================

with left:

    st.success(
        f"""
### Financial Executive Summary

💰 Revenue: **₦{finance_insight['Revenue']:,.0f}**

💵 Cost: **₦{finance_insight['Cost']:,.0f}**

📈 Profit: **₦{finance_insight['Profit']:,.0f}**

🎯 Profit Margin: **{finance_insight['Margin']:.2f}%**

📊 Financial Status: **{finance_insight['Status']}**

🌍 Best Region: **{finance_insight['Best Region']}**

🏷️ Best Category: **{finance_insight['Best Category']}**

🏆 Top Profit Product:
**{finance_insight['Top Profit Product']}**

💵 Top Profit Product Value:
**₦{finance_insight['Top Profit Product Value']:,.0f}**

🥇 Top Revenue Product:
**{finance_insight['Top Revenue Product']}**

💰 Top Revenue Product Value:
**₦{finance_insight['Top Revenue Product Value']:,.0f}**

🚚 Shipping Cost:
**₦{finance_insight['Shipping Cost']:,.0f}**

🧾 Average Order Value:
**₦{finance_insight['Average Order Value']:,.0f}**

📊 Top 10 Product Revenue Concentration:
**{finance_insight['Concentration']:.2f}%**
"""
    )


# ==========================================================
# EXECUTIVE FINANCIAL RECOMMENDATIONS
# ==========================================================

with right:

    st.markdown(
        "### 🎯 Financial Recommendations"
    )

    for recommendation in finance_insight[
        "Recommendations"
    ]:

        st.markdown(
            f"- {recommendation}"
        )
        

# ==========================================================
# FINANCE EXECUTIVE REPORT
# ==========================================================

st.divider()

st.subheader("📄 Finance Executive Report")

if st.button("Generate Finance Executive Report"):

    report = create_finance_report(
        finance_insight,
        df
    )

    st.success(
        "Finance Executive Report Generated Successfully!"
    )

    with open(report, "rb") as pdf:

        st.download_button(
            label="⬇ Download Finance Executive Report",
            data=pdf,
            file_name=report,
            mime="application/pdf",
        )
        
                
# ==========================================================
# DOWNLOAD FINANCIAL DATA
# ==========================================================

st.divider()

st.subheader("⬇ Export Financial Data")

finance_csv = ranking.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇ Download Financial Analysis",
    finance_csv,
    "financial_analysis.csv",
    "text/csv"
)

