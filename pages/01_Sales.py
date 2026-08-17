import streamlit as st

from database import load_sales_data
from components.sidebar import render_sidebar
from components.charts_panel import render_charts

from charts import (
    top_sales_transactions,
    generate_sales_insights,
    customer_segments,
    get_sales_by_region,
    get_sales_by_category,
)

from reports.sales_report import create_sales_report

from engines.sales_engine import (
    total_revenue,
    total_profit,
    total_orders,
    total_customers,
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📈",
    layout="wide",
)


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📈 Sales Analytics")

st.caption(
    "Enterprise Sales Performance Dashboard"
)


# ==========================================================
# LOAD DATA
# ==========================================================

df = load_sales_data()

df = render_sidebar(df)


# ==========================================================
# KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)


with k1:

    st.metric(
        "Revenue",
        f"₦{total_revenue(df):,.0f}"
    )


with k2:

    st.metric(
        "Profit",
        f"₦{total_profit(df):,.0f}"
    )


with k3:

    st.metric(
        "Orders",
        f"{total_orders(df):,}"
    )


with k4:

    st.metric(
        "Customers",
        f"{total_customers(df):,}"
    )


# ==========================================================
# EXECUTIVE ANALYTICS
# ==========================================================

st.divider()

render_charts(df)


# ==========================================================
# EXECUTIVE SALES SUMMARY
# ==========================================================

st.divider()

st.subheader("📋 Executive Sales Summary")


best_region = (
    df.groupby("Region")["Revenue"]
    .sum()
    .idxmax()
)


best_category = (
    df.groupby("Category")["Revenue"]
    .sum()
    .idxmax()
)


top_product = (
    df.groupby("Product Name")["Revenue"]
    .sum()
    .idxmax()
)


st.info(
    f"""
### Executive Overview

- **Revenue Generated:** ₦{total_revenue(df):,.0f}
- **Profit Earned:** ₦{total_profit(df):,.0f}
- **Orders Processed:** {total_orders(df):,}
- **Customers Served:** {total_customers(df):,}

### Business Highlights

✅ Highest Performing Region: **{best_region}**

✅ Best Selling Category: **{best_category}**

✅ Top Product: **{top_product}**

The business is generating strong revenue across multiple regions
with the highest contribution coming from **{best_region}**.
Continued investment in the **{best_category}** category is likely
to improve overall profitability.
"""
)


# ==========================================================
# CUSTOMER SEGMENTS
# ==========================================================

st.divider()

st.subheader("👥 Customer Analysis")

st.plotly_chart(
    customer_segments(df),
    use_container_width=True
)


# ==========================================================
# REGIONAL SALES
# ==========================================================

st.divider()

st.subheader("🌍 Regional Sales")

st.dataframe(
    get_sales_by_region(df),
    use_container_width=True,
    hide_index=True
)


# ==========================================================
# CATEGORY SALES
# ==========================================================

st.subheader("📦 Category Sales")

st.dataframe(
    get_sales_by_category(df),
    use_container_width=True,
    hide_index=True
)


# ==========================================================
# TOP 20 SALES TRANSACTIONS
# ==========================================================

st.divider()

st.subheader("🏆 Top 20 Sales Transactions")


top_transactions = top_sales_transactions(df).copy()


# ----------------------------------------------------------
# Ensure correct ranking after sorting
# ----------------------------------------------------------

top_transactions = (
    top_transactions
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(20)
    .reset_index(drop=True)
)


# ----------------------------------------------------------
# Remove an existing Rank column if the chart function
# already provides one
# ----------------------------------------------------------

if "Rank" in top_transactions.columns:

    top_transactions = top_transactions.drop(
        columns=["Rank"]
    )


# ----------------------------------------------------------
# Insert dynamic Rank AFTER sorting
# ----------------------------------------------------------

top_transactions.insert(
    0,
    "Rank",
    range(
        1,
        len(top_transactions) + 1
    )
)


# ----------------------------------------------------------
# Display transaction table
# ----------------------------------------------------------

st.dataframe(
    top_transactions,
    use_container_width=True,
    hide_index=True,
    column_config={

        "Rank": st.column_config.NumberColumn(
            "Rank",
            width="small"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₦%,.2f"
        ),

        "Profit": st.column_config.NumberColumn(
            "Profit",
            format="₦%,.2f"
        ),

        "Profit Margin %": st.column_config.NumberColumn(
            "Margin",
            format="%.2f%%"
        ),

        "Order Date": st.column_config.DateColumn(
            "Order Date",
            format="DD-MMM-YYYY"
        ),
    }
)


# ==========================================================
# AI EXECUTIVE INSIGHTS
# ==========================================================

st.divider()

st.subheader("🧠 AI Executive Insights")


insight = generate_sales_insights(df)


left, right = st.columns([2, 1])


# ----------------------------------------------------------
# Executive Summary
# ----------------------------------------------------------

with left:

    st.success(
        f"""
### Executive Summary

💰 Total Revenue: **₦{insight['Revenue']:,.0f}**

📈 Total Profit: **₦{insight['Profit']:,.0f}**

🎯 Profit Margin: **{insight['Margin']:.2f}%**

🌍 Highest Revenue Region: **{insight['Best Region']}**

🏆 Best Performing Category: **{insight['Best Category']}**

👤 Top Customer: **{insight['Top Customer']}**

🥇 Top Salesperson: **{insight['Top Salesperson']}**
"""
    )


# ----------------------------------------------------------
# Executive Recommendations
# ----------------------------------------------------------

with right:

    st.markdown(
        "### 🎯 Executive Recommendations"
    )

    recommendations = insight.get(
        "Recommendations",
        []
    )

    if recommendations:

        for recommendation in recommendations:

            st.markdown(
                f"- {recommendation}"
            )

    else:

        st.info(
            "No executive recommendations available "
            "for the current filter selection."
        )


# ==========================================================
# EXECUTIVE REPORT
# ==========================================================

st.divider()

st.subheader("📄 Executive Report")


if st.button(
    "Generate Executive Report",
    type="primary"
):

    try:

        report = create_sales_report(
            insight,
            df
        )

        st.success(
            "Executive Report Generated Successfully!"
        )

        with open(
            report,
            "rb"
        ) as pdf:

            st.download_button(
                label="⬇ Download Executive Report",
                data=pdf,
                file_name=report,
                mime="application/pdf",
            )

    except Exception as e:

        st.error(
            "Unable to generate the Executive Report."
        )

        st.exception(e)


# ==========================================================
# DOWNLOAD SALES DATA
# ==========================================================

st.divider()

st.subheader("⬇ Export Sales Data")


csv = df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    "⬇ Download Sales Data",
    csv,
    "sales.csv",
    "text/csv"
)