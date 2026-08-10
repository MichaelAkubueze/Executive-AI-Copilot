import streamlit as st
import plotly.express as px


def render_charts(df):

    st.subheader("📉 Executive Analytics")

    # ==========================
    # ROW 1
    # ==========================

    c1, c2 = st.columns(2)

    revenue = (
        df.groupby("Month", as_index=False)["Revenue"]
        .sum()
    )

    with c1:

        fig = px.line(
            revenue,
            x="Month",
            y="Revenue",
            markers=True,
            title="Monthly Revenue Trend",
        )

        fig.update_traces(
            line_color="#2563EB",
            marker_size=8,
        )

        fig.update_layout(
            template="plotly_white",
            height=420,
            margin=dict(l=10, r=10, t=45, b=10),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    profit = (
        df.groupby("Month", as_index=False)["Profit"]
        .sum()
    )

    with c2:

        fig = px.bar(
            profit,
            x="Month",
            y="Profit",
            title="Monthly Profit",
        )

        fig.update_traces(
            marker_color="#10B981"
        )

        fig.update_layout(
            template="plotly_white",
            height=420,
            margin=dict(l=10, r=10, t=45, b=10),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    # ==========================
    # ROW 2
    # ==========================

    c3, c4 = st.columns(2)

    region = (
        df.groupby("Region", as_index=False)["Revenue"]
        .sum()
    )

    with c3:

        fig = px.pie(
            region,
            values="Revenue",
            names="Region",
            title="Revenue by Region",
            hole=.55,
        )

        fig.update_layout(
            height=420,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    product = (
        df.groupby("Product Name", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
        .head(10)
    )

    with c4:

        fig = px.bar(
            product,
            x="Revenue",
            y="Product Name",
            orientation="h",
            title="Top 10 Products",
        )

        fig.update_traces(
            marker_color="#F59E0B"
        )

        fig.update_layout(
            template="plotly_white",
            height=420,
            margin=dict(l=10, r=10, t=45, b=10),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )