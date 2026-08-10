import streamlit as st

from services.report_service import (
    executive_report,
    export_pdf,
)


def render_board_report(df):

    st.subheader("📄 Executive Board Report")

    report = executive_report(df)

    # ==========================================================
    # FORMAT REPORT PREVIEW
    # ==========================================================

    summary = report["summary"]

    preview = f"""
ENTERPRISE SALES ANALYTICS

EXECUTIVE BOARD REPORT

Generated:
{summary["Generated"]}

==================================================

EXECUTIVE SUMMARY

Revenue:
{summary["Revenue"]}

Profit:
{summary["Profit"]}

Orders:
{summary["Orders"]}

Customers:
{summary["Customers"]}

Gross Margin:
{summary["Gross Margin"]}

==================================================

AI EXECUTIVE NARRATIVE

{report["narrative"]}

==================================================
"""

    st.text_area(
        "Board Report Preview",
        preview,
        height=420,
    )

    # ==========================================================
    # PDF GENERATION
    # ==========================================================

    if st.button("📄 Generate PDF Report"):

        filename = export_pdf(df)

        st.success("✅ PDF generated successfully!")

        with open(filename, "rb") as pdf_file:

            pdf_bytes = pdf_file.read()

        st.download_button(
            label="⬇ Download Executive PDF",
            data=pdf_bytes,
            file_name="Executive_Board_Report.pdf",
            mime="application/pdf",
        )