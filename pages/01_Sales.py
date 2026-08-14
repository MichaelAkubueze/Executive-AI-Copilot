import streamlit as st

from database import load_sales_data
from components.sidebar import render_sidebar
from components.charts_panel import render_charts

from charts import (
    monthly_revenue_chart,
    sales_by_region,
    sales_by_category,
    sales_channel,
    top_products,
    top_customers,
    customer_segments,
    get_sales_by_region,
    get_sales_by_category,
)

st.set_page_config(layout="wide")

st.title("📈 Sales Analytics")

st.caption("Enterprise Sales Performance Dashboard")

# ----------------------------------
# Load Data
# ----------------------------------

df = load_sales_data()

df = render_sidebar(df)

#-------------------------------
# 4 KPI Cards
#-------------------------------

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Revenue",
        f"₦{df['Revenue'].sum():,.0f}"
    )

with k2:
    st.metric(
        "Profit",
        f"₦{df['Profit'].sum():,.0f}"
    )

with k3:
    st.metric(
        "Orders",
        f"{len(df):,}"
    )

with k4:
    st.metric(
        "Customers",
        f"{df['Customer ID'].nunique():,}"
    )

#---------------------------------------
# Charts
#---------------------------------------

st.divider()

render_charts(df)

st.divider()

st.subheader("📋 Executive Sales Summary")

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
customers = df["Customer ID"].nunique()

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

st.info(f"""
### Executive Overview

- **Revenue Generated:** ₦{total_revenue:,.0f}
- **Profit Earned:** ₦{total_profit:,.0f}
- **Orders Processed:** {total_orders:,}
- **Customers Served:** {customers:,}

### Business Highlights

✅ Highest Performing Region: **{best_region}**

✅ Best Selling Category: **{best_category}**

✅ Top Product: **{top_product}**

The business is generating strong revenue across multiple regions with the highest contribution coming from **{best_region}**. Continued investment in the **{best_category}** category is likely to improve overall profitability.
""")

#-------------------------------------------
# Customer Segments
#-------------------------------------------
st.divider()

st.subheader("Customer Analysis")

st.plotly_chart(
    customer_segments(df),
    use_container_width=True
)

#--------------------------------------
# RAW DATA
#--------------------------------------
st.divider()

st.subheader("Regional Sales")

st.dataframe(
    get_sales_by_region(df),
    use_container_width=True
)

st.subheader("Category Sales")

st.dataframe(
    get_sales_by_category(df),
    use_container_width=True
)

#-------------------------
# DOWNLOAD BUTTONS
#--------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Sales Data",
    csv,
    "sales.csv",
    "text/csv"
)
    
    