import streamlit as st

from database import load_sales_data
from components.sidebar import render_sidebar
from reports.customer_report import create_customer_report

from engines.customer_engine import (
    total_customers,
    total_customer_revenue,
    total_customer_profit,
    average_customer_revenue,
    repeat_customer_rate,
    customer_drilldown,
    high_value_customers,
    at_risk_customers,
)

from engines.customer_ai import (
    generate_customer_insights,
)

from components.customer_charts import (
    customer_segment_chart,
    top_customers_revenue,
    top_customers_profit,
    customer_revenue_by_region,
    customer_orders_chart,
    customer_profitability,
    customer_revenue_concentration,
    customer_revenue_distribution,
    new_vs_returning_customers_chart,
    new_vs_returning_revenue_chart,
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="👥",
    layout="wide",
)


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("👥 Customer Analytics")

st.caption(
    "Enterprise Customer Intelligence Dashboard"
)


# ==========================================================
# LOAD DATA
# ==========================================================

df = load_sales_data()

df = render_sidebar(df)


# ==========================================================
# CUSTOMER KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)


with k1:

    st.metric(
        "Total Customers",
        f"{total_customers(df):,}"
    )


with k2:

    st.metric(
        "Customer Revenue",
        f"₦{total_customer_revenue(df):,.0f}"
    )


with k3:

    st.metric(
        "Customer Profit",
        f"₦{total_customer_profit(df):,.0f}"
    )


with k4:

    st.metric(
        "Repeat Customer Rate",
        f"{repeat_customer_rate(df):.2f}%"
    )


# ==========================================================
# CUSTOMER SEGMENTATION
# ==========================================================

st.divider()

st.subheader("👥 Customer Segmentation")


col1, col2 = st.columns(2)


with col1:

    st.plotly_chart(
        customer_segment_chart(df),
        use_container_width=True
    )


with col2:

    st.plotly_chart(
        top_customers_revenue(df),
        use_container_width=True
    )


# ==========================================================
# CUSTOMER PROFITABILITY
# ==========================================================

st.divider()

st.subheader("💰 Customer Profitability")


col3, col4 = st.columns(2)


with col3:

    st.plotly_chart(
        top_customers_profit(df),
        use_container_width=True
    )


with col4:

    st.plotly_chart(
        customer_revenue_by_region(df),
        use_container_width=True
    )


# ==========================================================
# ADVANCED CUSTOMER ANALYTICS
# ==========================================================

st.divider()

st.subheader("📊 Advanced Customer Analytics")


# ----------------------------------------------------------
# ROW 1 — ORDER FREQUENCY & PROFITABILITY
# ----------------------------------------------------------

col5, col6 = st.columns(2)


with col5:

    st.plotly_chart(
        customer_orders_chart(df),
        use_container_width=True
    )


with col6:

    st.plotly_chart(
        customer_profitability(df),
        use_container_width=True
    )


# ----------------------------------------------------------
# ROW 2 — REVENUE CONCENTRATION & DISTRIBUTION
# ----------------------------------------------------------

col7, col8 = st.columns(2)


with col7:

    st.plotly_chart(
        customer_revenue_concentration(df),
        use_container_width=True
    )


with col8:

    st.plotly_chart(
        customer_revenue_distribution(df),
        use_container_width=True
    )


# ==========================================================
# CUSTOMER RETENTION ANALYSIS
# ==========================================================

st.divider()

st.subheader("🔄 Customer Retention Analysis")


col9, col10 = st.columns(2)


with col9:

    st.plotly_chart(
        new_vs_returning_customers_chart(df),
        use_container_width=True
    )


with col10:

    st.plotly_chart(
        new_vs_returning_revenue_chart(df),
        use_container_width=True
    )


# ==========================================================
# CUSTOMER EXECUTIVE SUMMARY
# ==========================================================

st.divider()

st.subheader("📋 Customer Executive Summary")


top_customer = (
    df.groupby("Customer Name")["Revenue"]
    .sum()
    .idxmax()
)


top_customer_revenue_value = (
    df.groupby("Customer Name")["Revenue"]
    .sum()
    .max()
)


top_customer_profit = (
    df.groupby("Customer Name")["Profit"]
    .sum()
    .idxmax()
)


st.info(
    f"""
### Customer Overview

- **Total Customers:** {total_customers(df):,}
- **Customer Revenue:** ₦{total_customer_revenue(df):,.0f}
- **Customer Profit:** ₦{total_customer_profit(df):,.0f}
- **Average Revenue per Customer:** ₦{average_customer_revenue(df):,.0f}

### Customer Highlights

🏆 **Top Revenue Customer:** {top_customer}

💰 **Top Customer Revenue:** ₦{top_customer_revenue_value:,.0f}

📈 **Highest Profit Customer:** {top_customer_profit}

The customer base is generating significant revenue across the
business regions. The highest-value customers should be prioritized
for retention, relationship management, and repeat-purchase
opportunities.
"""
)

# ==========================================================
# CUSTOMER DRILL-DOWN
# ==========================================================

st.divider()

st.subheader("🔎 Customer Drill-Down")

customer_list = (
    df["Customer Name"]
    .dropna()
    .unique()
    .tolist()
)

customer_list = sorted(customer_list)

selected_customer = st.selectbox(
    "Select Customer",
    customer_list
)

customer_detail = customer_drilldown(
    df,
    selected_customer
)

if customer_detail:

    d1, d2, d3, d4 = st.columns(4)

    with d1:
        st.metric(
            "Revenue",
            f"₦{customer_detail['Revenue']:,.0f}"
        )

    with d2:
        st.metric(
            "Profit",
            f"₦{customer_detail['Profit']:,.0f}"
        )

    with d3:
        st.metric(
            "Orders",
            f"{customer_detail['Orders']:,}"
        )

    with d4:
        st.metric(
            "Profit Margin",
            f"{customer_detail['Margin']:.2f}%"
        )

    st.info(
        f"""
### {selected_customer}

**Products Purchased:** {customer_detail['Products']:,}

**Regions:** {customer_detail['Regions']:,}

The selected customer's commercial performance is shown above.
"""
    )

# ==========================================================
# CUSTOMER VALUE ANALYSIS
# ==========================================================

st.divider()

st.subheader("🏆 Customer Value Analysis")

value_col1, value_col2 = st.columns(2)

with value_col1:

    st.markdown("### ⭐ High-Value Customers")

    high_value = high_value_customers(
        df,
        limit=20
    )

    st.dataframe(
        high_value,
        use_container_width=True,
        hide_index=True
    )

with value_col2:

    st.markdown("### ⚠️ Potential Retention Opportunities")

    at_risk = at_risk_customers(
        df,
        limit=20
    )

    st.dataframe(
        at_risk,
        use_container_width=True,
        hide_index=True
    )
    
    
# ==========================================================
# AI CUSTOMER INTELLIGENCE
# ==========================================================

st.divider()

st.subheader("🧠 AI Customer Intelligence")


customer_insight = generate_customer_insights(df)


left, right = st.columns([2, 1])


# ----------------------------------------------------------
# AI EXECUTIVE SUMMARY
# ----------------------------------------------------------

with left:

    st.success(
        f"""
### Customer Executive Summary

👥 Total Customers: **{customer_insight['Customers']:,}**

💰 Customer Revenue: **₦{customer_insight['Revenue']:,.0f}**

📈 Customer Profit: **₦{customer_insight['Profit']:,.0f}**

🎯 Profit Margin: **{customer_insight['Margin']:.2f}%**

🔄 Repeat Customer Rate: **{customer_insight['Repeat Rate']:.2f}%**

🌍 Best Region: **{customer_insight['Best Region']}**

🏆 Top Customer: **{customer_insight['Top Customer']}**

💵 Top Customer Revenue: **₦{customer_insight['Top Customer Revenue']:,.0f}**

🥇 Top Profit Customer: **{customer_insight['Top Profit Customer']}**

📊 Top 10 Customer Revenue Concentration:
**{customer_insight['Concentration']:.2f}%**
"""
    )


# ----------------------------------------------------------
# AI RECOMMENDATIONS
# ----------------------------------------------------------

with right:

    st.markdown(
        "### 🎯 Customer Recommendations"
    )

    for recommendation in customer_insight[
        "Recommendations"
    ]:

        st.markdown(
            f"- {recommendation}"
        )


# ==========================================================
# CUSTOMER DATA TABLE
# ==========================================================

st.divider()

# ==========================================================
# CUSTOMER EXECUTIVE REPORT
# ==========================================================

st.divider()

st.subheader("📄 Customer Executive Report")


if st.button("Generate Customer Executive Report"):

    customer_report = create_customer_report(
        customer_insight,
        df
    )

    st.success(
        "Customer Executive Report Generated Successfully!"
    )

    with open(customer_report, "rb") as pdf:

        st.download_button(
            label="⬇ Download Customer Executive Report",
            data=pdf,
            file_name=customer_report,
            mime="application/pdf",
        )

st.subheader("📊 Customer Revenue Summary")


customer_summary = (
    df.groupby(
        "Customer Name",
        as_index=False
    )
    .agg(
        Orders=("Order ID", "nunique"),
        Revenue=("Revenue", "sum"),
        Profit=("Profit", "sum"),
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
    .reset_index(drop=True)
)


# ----------------------------------------------------------
# CREATE RANK AFTER SORTING
# ----------------------------------------------------------

customer_summary.insert(
    0,
    "Rank",
    range(
        1,
        len(customer_summary) + 1
    )
)


st.dataframe(
    customer_summary.head(20),
    use_container_width=True,
    hide_index=True,

    column_config={

        "Rank": st.column_config.NumberColumn(
            "Rank",
            width="small"
        ),

        "Orders": st.column_config.NumberColumn(
            "Orders",
            format="%d"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₦%,.2f"
        ),

        "Profit": st.column_config.NumberColumn(
            "Profit",
            format="₦%,.2f"
        ),
    }
)


# ==========================================================
# DOWNLOAD CUSTOMER DATA
# ==========================================================

st.divider()

st.subheader("⬇ Export Customer Data")


customer_csv = (
    customer_summary
    .to_csv(index=False)
    .encode("utf-8")
)


st.download_button(
    "⬇ Download Customer Data",
    customer_csv,
    "customer_analysis.csv",
    "text/csv"
)