import streamlit as st


def render_sidebar(df):

    st.sidebar.title("Dashboard Filters")

    years = ["All"] + sorted(df["Year"].unique().tolist())

    selected_year = st.sidebar.selectbox(

        "Year",

        years

    )

    if selected_year != "All":

        df = df[df["Year"] == selected_year]

    months = ["All"] + sorted(df["Month"].unique().tolist())

    selected_month = st.sidebar.selectbox(

        "Month",

        months

    )

    if selected_month != "All":

        df = df[df["Month"] == selected_month]

    regions = ["All"] + sorted(df["Region"].unique().tolist())

    selected_region = st.sidebar.selectbox(

        "Region",

        regions

    )

    if selected_region != "All":

        df = df[df["Region"] == selected_region]

    st.sidebar.markdown("---")

    st.sidebar.success(

        f"Records Loaded : {len(df):,}"

    )

    return df