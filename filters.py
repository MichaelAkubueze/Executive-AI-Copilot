import streamlit as st


def build_filters(df):

    # ==========================================
    # SIDEBAR HEADER
    # ==========================================

    st.sidebar.title("📊 Dashboard Filters")
    st.sidebar.markdown("---")

    # ==========================================
    # YEAR FILTER
    # ==========================================

    years = ["All"] + sorted(df["Year"].dropna().unique().tolist())

    selected_year = st.sidebar.selectbox(
        "Select Year",
        years
    )

    if selected_year != "All":
        df = df[df["Year"] == selected_year]

    # ==========================================
    # QUARTER FILTER
    # ==========================================

    quarters = ["All"] + sorted(df["Quarter"].dropna().unique().tolist())

    selected_quarter = st.sidebar.selectbox(
        "Select Quarter",
        quarters
    )

    if selected_quarter != "All":
        df = df[df["Quarter"] == selected_quarter]

    # ==========================================
    # MONTH FILTER
    # ==========================================

    months = ["All"] + list(df["Month"].dropna().unique())

    selected_month = st.sidebar.selectbox(
        "Select Month",
        months
    )

    if selected_month != "All":
        df = df[df["Month"] == selected_month]

    # ==========================================
    # REGION FILTER
    # ==========================================

    regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())

    selected_region = st.sidebar.selectbox(
        "Select Region",
        regions
    )

    if selected_region != "All":
        df = df[df["Region"] == selected_region]

    # ==========================================
    # CATEGORY FILTER
    # ==========================================

    categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())

    selected_category = st.sidebar.selectbox(
        "Select Category",
        categories
    )

    if selected_category != "All":
        df = df[df["Category"] == selected_category]

    # ==========================================
    # CUSTOMER SEGMENT
    # ==========================================

    segments = ["All"] + sorted(df["Customer Segment"].dropna().unique().tolist())

    selected_segment = st.sidebar.selectbox(
        "Customer Segment",
        segments
    )

    if selected_segment != "All":
        df = df[df["Customer Segment"] == selected_segment]

    # ==========================================
    # SALES CHANNEL
    # ==========================================

    channels = ["All"] + sorted(df["Sales Channel"].dropna().unique().tolist())

    selected_channel = st.sidebar.selectbox(
        "Sales Channel",
        channels
    )

    if selected_channel != "All":
        df = df[df["Sales Channel"] == selected_channel]

    # ==========================================
    # PAYMENT METHOD
    # ==========================================

    payments = ["All"] + sorted(df["Payment Method"].dropna().unique().tolist())

    selected_payment = st.sidebar.selectbox(
        "Payment Method",
        payments
    )

    if selected_payment != "All":
        df = df[df["Payment Method"] == selected_payment]

    # ==========================================
    # DELIVERY STATUS
    # ==========================================

    delivery = ["All"] + sorted(df["Delivery Status"].dropna().unique().tolist())

    selected_delivery = st.sidebar.selectbox(
        "Delivery Status",
        delivery
    )

    if selected_delivery != "All":
        df = df[df["Delivery Status"] == selected_delivery]

    # ==========================================
    # SIDEBAR SUMMARY
    # ==========================================

    st.sidebar.markdown("---")

    st.sidebar.success(
        f"Showing **{len(df):,}** records"
    )

    return df