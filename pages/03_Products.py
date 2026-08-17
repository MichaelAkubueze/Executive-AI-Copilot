import streamlit as st

from database import load_sales_data
from components.sidebar import render_sidebar

from engines.product_engine import (
    total_products,
    total_product_revenue,
    total_product_profit,
    average_product_revenue,
    product_profit_margin,
    total_units_sold,
    product_category_summary,
    product_drilldown,
    product_ranking,
)

from engines.product_ai import generate_product_insights

from components.product_charts import (
    top_products_revenue_chart,
    top_products_profit_chart,
    product_category_revenue_chart,
    product_category_profit_chart,
    product_subcategory_chart,
    product_units_chart,
    product_profitability_chart,
    product_revenue_distribution_chart,
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Product Analytics",
    page_icon="📦",
    layout="wide",
)


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📦 Product Analytics")

st.caption(
    "Enterprise Product Performance Intelligence"
)


# ==========================================================
# LOAD DATA
# ==========================================================

df = load_sales_data()

df = render_sidebar(df)


# ==========================================================
# PRODUCT KPI CARDS
# ==========================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Total Products",
        f"{total_products(df):,}"
    )

with k2:
    st.metric(
        "Product Revenue",
        f"₦{total_product_revenue(df):,.0f}"
    )

with k3:
    st.metric(
        "Product Profit",
        f"₦{total_product_profit(df):,.0f}"
    )

with k4:
    st.metric(
        "Profit Margin",
        f"{product_profit_margin(df):.2f}%"
    )


# ==========================================================
# PRODUCT PERFORMANCE
# ==========================================================

st.divider()

st.subheader("📈 Product Performance")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        top_products_revenue_chart(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        top_products_profit_chart(df),
        use_container_width=True
    )


# ==========================================================
# CATEGORY ANALYSIS
# ==========================================================

st.divider()

st.subheader("🏷️ Category Analysis")

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        product_category_revenue_chart(df),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        product_category_profit_chart(df),
        use_container_width=True
    )


# ==========================================================
# PRODUCT VOLUME
# ==========================================================

st.divider()

st.subheader("📊 Product Volume Analysis")

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(
        product_subcategory_chart(df),
        use_container_width=True
    )

with col6:
    st.plotly_chart(
        product_units_chart(df),
        use_container_width=True
    )


# ==========================================================
# PRODUCT PROFITABILITY
# ==========================================================

st.divider()

st.subheader("💰 Product Profitability")

col7, col8 = st.columns(2)

with col7:
    st.plotly_chart(
        product_profitability_chart(df),
        use_container_width=True
    )

with col8:
    st.plotly_chart(
        product_revenue_distribution_chart(df),
        use_container_width=True
    )


# ==========================================================
# PRODUCT DRILL-DOWN
# ==========================================================

st.divider()

st.subheader("🔎 Product Drill-Down")

product_list = (
    df["Product Name"]
    .dropna()
    .unique()
    .tolist()
)

product_list = sorted(product_list)

selected_product = st.selectbox(
    "Select Product",
    product_list
)

product_detail = product_drilldown(
    df,
    selected_product
)

if product_detail:

    d1, d2, d3, d4 = st.columns(4)

    with d1:
        st.metric(
            "Revenue",
            f"₦{product_detail['Revenue']:,.0f}"
        )

    with d2:
        st.metric(
            "Profit",
            f"₦{product_detail['Profit']:,.0f}"
        )

    with d3:
        st.metric(
            "Units Sold",
            f"{product_detail['Units']:,}"
        )

    with d4:
        st.metric(
            "Profit Margin",
            f"{product_detail['Margin']:.2f}%"
        )

    d5, d6, d7 = st.columns(3)

    with d5:
        st.metric(
            "Orders",
            f"{product_detail['Orders']:,}"
        )

    with d6:
        st.metric(
            "Customers",
            f"{product_detail['Customers']:,}"
        )

    with d7:
        st.metric(
            "Regions",
            f"{product_detail['Regions']:,}"
        )


# ==========================================================
# PRODUCT RANKING
# ==========================================================

st.divider()

st.subheader("🏆 Product Ranking")

ranking = product_ranking(df)

st.dataframe(
    ranking.head(20),
    use_container_width=True,
    hide_index=True,
    column_config={

        "Rank": st.column_config.NumberColumn(
            "Rank",
            width="small"
        ),

        "Product ID": st.column_config.TextColumn(
            "Product ID",
            width="small"
        ),

        "Product Name": st.column_config.TextColumn(
            "Product Name",
            width="medium"
        ),

        "Units": st.column_config.NumberColumn(
            "Units",
            format="%d",
            width="small"
        ),

        "Orders": st.column_config.NumberColumn(
            "Orders",
            format="%d",
            width="small"
        ),

        "Customers": st.column_config.NumberColumn(
            "Customers",
            format="%d",
            width="small"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₦%,.2f",
            width="medium"
        ),

        "Profit": st.column_config.NumberColumn(
            "Profit",
            format="₦%,.2f",
            width="medium"
        ),

        "Profit Margin": st.column_config.NumberColumn(
            "Profit Margin",
            format="%.2f%%",
            width="medium"
        ),
    }
)


# ==========================================================
# PRODUCT EXECUTIVE SUMMARY
# ==========================================================

st.divider()

st.subheader("📋 Product Executive Summary")

product_revenue = total_product_revenue(df)
product_profit = total_product_profit(df)
product_count = total_products(df)
units = total_units_sold(df)

best_product = (
    df.groupby("Product Name")["Revenue"]
    .sum()
    .idxmax()
)

best_product_revenue = (
    df.groupby("Product Name")["Revenue"]
    .sum()
    .max()
)

best_profit_product = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .idxmax()
)

best_category = (
    df.groupby("Category")["Revenue"]
    .sum()
    .idxmax()
)

st.info(
    f"""
### Product Overview

- **Total Products:** {product_count:,}
- **Total Units Sold:** {units:,}
- **Product Revenue:** ₦{product_revenue:,.0f}
- **Product Profit:** ₦{product_profit:,.0f}
- **Average Revenue per Product:** ₦{average_product_revenue(df):,.0f}

### Product Highlights

🏆 **Top Revenue Product:** {best_product}

💰 **Top Product Revenue:** ₦{best_product_revenue:,.0f}

📈 **Highest Profit Product:** {best_profit_product}

🏷️ **Best Performing Category:** {best_category}

The product portfolio is generating revenue across multiple
categories. High-performing products should receive continued
commercial attention while low-margin products should be reviewed
for pricing, cost, and inventory efficiency.
"""
)


# ==========================================================
# AI PRODUCT INTELLIGENCE
# ==========================================================

st.divider()

st.subheader("🧠 AI Product Intelligence")

product_insight = generate_product_insights(df)

ai_left, ai_right = st.columns(
    [1, 1],
    gap="large"
)


# ==========================================================
# AI EXECUTIVE SUMMARY
# ==========================================================

with ai_left:

    with st.container(border=True):

        st.markdown(
            """
            <h3 style="
                color:#16823b;
                margin-top:0;
                margin-bottom:20px;
            ">
            Product Executive Summary
            </h3>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                line-height:2.15;
                color:#16823b;
            ">

            📦 <b>Total Products:</b>
            {product_insight['Products']:,}

            <br>

            💰 <b>Product Revenue:</b>
            ₦{product_insight['Revenue']:,.0f}

            <br>

            📈 <b>Product Profit:</b>
            ₦{product_insight['Profit']:,.0f}

            <br>

            🎯 <b>Profit Margin:</b>
            {product_insight['Margin']:.2f}%

            <br>

            🏆 <b>Best Product:</b>
            {product_insight['Best Product']}

            <br>

            💵 <b>Best Product Revenue:</b>
            ₦{product_insight['Best Product Revenue']:,.0f}

            <br>

            🥇 <b>Top Profit Product:</b>
            {product_insight['Top Profit Product']}

            <br>

            🏷️ <b>Best Category:</b>
            {product_insight['Best Category']}

            <br>

            📊 <b>Top Product Revenue Concentration:</b>
            {product_insight['Concentration']:.2f}%

            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================================
# AI PRODUCT RECOMMENDATIONS
# ==========================================================

with ai_right:

    with st.container(border=True):

        st.markdown(
            """
            <h3 style="
                margin-top:0;
                margin-bottom:20px;
            ">
            🎯 Product Recommendations
            </h3>
            """,
            unsafe_allow_html=True
        )

        for recommendation in product_insight[
            "Recommendations"
        ]:

            st.markdown(
                f"""
                <div style="
                    margin-bottom:18px;
                    line-height:1.65;
                ">
                {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )


# ==========================================================
# CATEGORY PERFORMANCE
# ==========================================================

st.divider()

st.subheader("🏷️ Category Performance")

category_summary = product_category_summary(df)

st.dataframe(
    category_summary,
    use_container_width=True,
    hide_index=True,
    column_config={

        "Category": st.column_config.TextColumn(
            "Category",
            width="medium"
        ),

        "Products": st.column_config.NumberColumn(
            "Products",
            format="%d",
            width="small"
        ),

        "Units": st.column_config.NumberColumn(
            "Units",
            format="%d",
            width="small"
        ),

        "Orders": st.column_config.NumberColumn(
            "Orders",
            format="%d",
            width="small"
        ),

        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₦%,.2f",
            width="medium"
        ),

        "Profit": st.column_config.NumberColumn(
            "Profit",
            format="₦%,.2f",
            width="medium"
        ),
    }
)


# ==========================================================
# DOWNLOAD PRODUCT DATA
# ==========================================================

st.divider()

st.subheader("⬇ Export Product Data")

product_csv = ranking.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇ Download Product Analysis",
    product_csv,
    "product_analysis.csv",
    "text/csv"
)
