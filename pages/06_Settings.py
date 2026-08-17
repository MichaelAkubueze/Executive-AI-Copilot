import streamlit as st

from engines.settings_engine import (
    load_settings,
    save_settings,
    reset_settings,
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide",
)


# ==========================================================
# LOAD SAVED SETTINGS
# ==========================================================

settings = load_settings()


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("⚙️ Settings")

st.caption(
    "Application configuration and system preferences"
)


# ==========================================================
# GENERAL SETTINGS
# ==========================================================

st.divider()

st.subheader("⚙️ General Settings")

col1, col2 = st.columns(2)


with col1:

    company_name = st.text_input(
        "Company Name",
        value=settings["company_name"],
    )

    dashboard_title = st.text_input(
        "Dashboard Title",
        value=settings["dashboard_title"],
    )


with col2:

    currency = st.selectbox(
        "Currency",
        [
            "₦ Nigerian Naira",
            "$ US Dollar",
            "€ Euro",
            "£ British Pound",
        ],
        index=[
            "₦ Nigerian Naira",
            "$ US Dollar",
            "€ Euro",
            "£ British Pound",
        ].index(
            settings["currency"]
        )
        if settings["currency"]
        in [
            "₦ Nigerian Naira",
            "$ US Dollar",
            "€ Euro",
            "£ British Pound",
        ]
        else 0,
    )

    report_language = st.selectbox(
        "Report Language",
        [
            "English",
        ],
        index=0,
    )


# ==========================================================
# DISPLAY SETTINGS
# ==========================================================

st.divider()

st.subheader("🖥️ Display Settings")

col3, col4 = st.columns(2)


with col3:

    show_kpis = st.checkbox(
        "Show KPI Cards",
        value=settings["show_kpis"],
    )

    show_summaries = st.checkbox(
        "Show Executive Summaries",
        value=settings["show_summaries"],
    )


with col4:

    show_ai_insights = st.checkbox(
        "Show AI Insights",
        value=settings["show_ai_insights"],
    )

    show_charts = st.checkbox(
        "Show Charts",
        value=settings["show_charts"],
    )


# ==========================================================
# REPORT SETTINGS
# ==========================================================

st.divider()

st.subheader("📄 Report Settings")

col5, col6 = st.columns(2)


with col5:

    include_logo = st.checkbox(
        "Include Company Logo",
        value=settings["include_logo"],
    )

    include_footer = st.checkbox(
        "Include Report Footer",
        value=settings["include_footer"],
    )


with col6:

    include_page_numbers = st.checkbox(
        "Include Page Numbers",
        value=settings["include_page_numbers"],
    )

    include_generation_date = st.checkbox(
        "Include Generation Date",
        value=settings["include_generation_date"],
    )


# ==========================================================
# SYSTEM INFORMATION
# ==========================================================

st.divider()

st.subheader("🖥️ System Information")

info1, info2, info3 = st.columns(3)


with info1:

    st.metric(
        "Application",
        "Enterprise Sales Analytics",
    )


with info2:

    st.metric(
        "Currency",
        currency.split(" ")[0],
    )


with info3:

    st.metric(
        "Report Format",
        "PDF",
    )


# ==========================================================
# SAVE SETTINGS
# ==========================================================

st.divider()

col_save, col_reset = st.columns(2)


with col_save:

    if st.button(
        "💾 Save Settings",
        type="primary",
        use_container_width=True,
    ):

        updated_settings = {

            "company_name": company_name,

            "dashboard_title": dashboard_title,

            "currency": currency,

            "report_language": report_language,

            "show_kpis": show_kpis,

            "show_summaries": show_summaries,

            "show_ai_insights": show_ai_insights,

            "show_charts": show_charts,

            "include_logo": include_logo,

            "include_footer": include_footer,

            "include_page_numbers": include_page_numbers,

            "include_generation_date": (
                include_generation_date
            ),
        }

        save_settings(
            updated_settings
        )

        st.success(
            "Settings saved successfully."
        )


# ==========================================================
# RESET SETTINGS
# ==========================================================

with col_reset:

    if st.button(
        "↩ Reset to Defaults",
        use_container_width=True,
    ):

        reset_settings()

        st.success(
            "Settings reset to default values."
        )

        st.rerun()