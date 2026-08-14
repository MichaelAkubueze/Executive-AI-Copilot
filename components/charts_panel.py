import streamlit as st

from charts import (
    monthly_revenue_chart,
    sales_by_region,
    sales_by_category,
    sales_channel,
    top_products,
    top_customers,
    top_salespersons,
    sales_by_country,
)

def render_charts(df, page="home"):

    st.subheader("📊 Executive Analytics")

    # ==========================================
    # HOME / SALES DASHBOARD
    # ==========================================

    if page in ["home", "sales"]:

        row1_col1, row1_col2 = st.columns(2)

        with row1_col1:
            st.plotly_chart(
                monthly_revenue_chart(df),
                use_container_width=True
            )

        with row1_col2:
            st.plotly_chart(
                sales_by_region(df),
                use_container_width=True
            )

        row2_col1, row2_col2 = st.columns(2)

        with row2_col1:
            st.plotly_chart(
                sales_by_category(df),
                use_container_width=True
            )

        with row2_col2:
            st.plotly_chart(
                sales_channel(df),
                use_container_width=True
            )

        row3_col1, row3_col2 = st.columns(2)

        with row3_col1:
            st.plotly_chart(
                top_products(df),
                use_container_width=True
            )

        with row3_col2:
            st.plotly_chart(
                top_customers(df),
                use_container_width=True
            )
                        
# ---------------------------
# ROW 4
# ---------------------------

        col7, col8 = st.columns(2)

        with col7:
             st.plotly_chart(
                top_salespersons(df),
                use_container_width=True
            )

        with col8:
            st.plotly_chart(
                sales_by_country(df),
                use_container_width=True
            )
