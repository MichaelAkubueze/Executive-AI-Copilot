import streamlit as st

from charts import (

    monthly_revenue_chart,

    sales_by_region,

    sales_by_category,

    customer_segments,

    sales_channel,

    top_products,

    top_customers,

)


def render_charts(df):

    st.markdown("## 📈 Executive Analytics")

    left, right = st.columns(2)

    with left:

        st.plotly_chart(

            monthly_revenue_chart(df),

            use_container_width=True

        )

    with right:

        st.plotly_chart(

            sales_by_region(df),

            use_container_width=True

        )

    left, right = st.columns(2)

    with left:

        st.plotly_chart(

            sales_by_category(df),

            use_container_width=True

        )

    with right:

        st.plotly_chart(

            customer_segments(df),

            use_container_width=True

        )

    left, right = st.columns(2)

    with left:

        st.plotly_chart(

            sales_channel(df),

            use_container_width=True

        )

    with right:

        st.plotly_chart(

            top_products(df),

            use_container_width=True

        )

    st.plotly_chart(

        top_customers(df),

        use_container_width=True

    )