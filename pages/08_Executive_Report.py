import os
import streamlit as st

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reports.report_utils import (
    report_date,
    report_time,
)

from engines.settings_engine import (
    get_setting,
    currency_symbol,
)

from database import load_sales_data
from components.sidebar import render_sidebar

from executive import executive_metrics


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Executive Report",
    page_icon="📊",
    layout="wide",
)


# ==========================================================
# FILE PATHS
# ==========================================================

LOGO_PATH = (
    r"C:\Data Analytics Portfolio"
    r"\03_Python_SQL_Analytics"
    r"\assets\company_logo.png"
)

CALIBRI_PATH = r"C:\Windows\Fonts\calibri.ttf"

CALIBRI_BOLD_PATH = r"C:\Windows\Fonts\calibrib.ttf"


# ==========================================================
# REGISTER PDF FONTS
# ==========================================================

if (
    os.path.exists(CALIBRI_PATH)
    and "Calibri" not in pdfmetrics.getRegisteredFontNames()
):

    pdfmetrics.registerFont(
        TTFont(
            "Calibri",
            CALIBRI_PATH,
        )
    )


if (
    os.path.exists(CALIBRI_BOLD_PATH)
    and "Calibri-Bold" not in pdfmetrics.getRegisteredFontNames()
):

    pdfmetrics.registerFont(
        TTFont(
            "Calibri-Bold",
            CALIBRI_BOLD_PATH,
        )
    )


# ==========================================================
# PDF STYLES
# ==========================================================

PDF_TITLE = ParagraphStyle(
    "ExecutivePDFTitle",
    fontName="Calibri-Bold",
    fontSize=18,
    leading=22,
    alignment=TA_CENTER,
    spaceAfter=8,
)


PDF_SUBTITLE = ParagraphStyle(
    "ExecutivePDFSubtitle",
    fontName="Calibri",
    fontSize=10,
    leading=13,
    alignment=TA_CENTER,
    spaceAfter=10,
)


PDF_HEADING = ParagraphStyle(
    "ExecutivePDFHeading",
    fontName="Calibri-Bold",
    fontSize=13,
    leading=16,
    alignment=TA_LEFT,
    spaceBefore=5,
    spaceAfter=8,
)


PDF_BODY = ParagraphStyle(
    "ExecutivePDFBody",
    fontName="Calibri",
    fontSize=9,
    leading=13,
    alignment=TA_LEFT,
)


PDF_HEADER = ParagraphStyle(
    "ExecutivePDFHeader",
    fontName="Calibri-Bold",
    fontSize=8,
    leading=10,
    textColor=colors.white,
)


PDF_TABLE_BODY = ParagraphStyle(
    "ExecutivePDFTableBody",
    fontName="Calibri",
    fontSize=8,
    leading=10,
)


# ==========================================================
# PDF FOOTER
# ==========================================================

def executive_pdf_footer(canvas, doc):

    include_footer = get_setting(
        "include_footer",
        True,
    )

    include_page_numbers = get_setting(
        "include_page_numbers",
        True,
    )

    if not include_footer and not include_page_numbers:
        return

    canvas.saveState()

    width, height = A4

    # ------------------------------------------------------
    # FOOTER
    # ------------------------------------------------------

    if include_footer:

        canvas.setStrokeColor(
            colors.HexColor("#D9E2F3")
        )

        canvas.line(
            36,
            35,
            width - 36,
            35,
        )

        canvas.setFont(
            "Calibri",
            8,
        )

        canvas.setFillColor(
            colors.HexColor("#666666")
        )

        canvas.drawString(
            36,
            22,
            get_setting(
                "company_name",
                "MICT E-LEARNING SERVICES LTD",
            ),
        )

    # ------------------------------------------------------
    # PAGE NUMBER
    # ------------------------------------------------------

    if include_page_numbers:

        canvas.setFont(
            "Calibri",
            8,
        )

        canvas.setFillColor(
            colors.HexColor("#666666")
        )

        canvas.drawRightString(
            width - 36,
            22,
            f"Page {doc.page}",
        )

    canvas.restoreState()


# ==========================================================
# CREATE EXECUTIVE PDF
# ==========================================================

def create_executive_pdf(metrics):

    company_name = get_setting(
        "company_name",
        "MICT E-LEARNING SERVICES LTD",
    )

    symbol = currency_symbol()

    filename = "Enterprise_Executive_Report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=42,
        bottomMargin=50,
        title="Executive Board Report",
        author=company_name,
    )

    story = []

    # ======================================================
    # LOGO
    # ======================================================

    include_logo = get_setting(
        "include_logo",
        True,
    )

    if (
        include_logo
        and os.path.exists(LOGO_PATH)
    ):

        logo = Image(
            LOGO_PATH,
            width=110,
            height=55,
            kind="proportional",
        )

        logo.hAlign = "CENTER"

        story.append(logo)

        story.append(
            Spacer(1, 8)
        )

    # ======================================================
    # HEADER
    # ======================================================

    story.append(
        Paragraph(
            company_name,
            PDF_TITLE,
        )
    )

    story.append(
        Paragraph(
            "Enterprise Sales Analytics Platform",
            PDF_SUBTITLE,
        )
    )

    story.append(
        Paragraph(
            "EXECUTIVE BOARD REPORT",
            PDF_HEADING,
        )
    )

    # ======================================================
    # GENERATION DATE
    # ======================================================

    include_generation_date = get_setting(
        "include_generation_date",
        True,
    )

    if include_generation_date:

        story.append(
            Paragraph(
                f"Generated: "
                f"{report_date()} "
                f"{report_time()}",
                PDF_BODY,
            )
        )

        story.append(
            Spacer(1, 15)
        )

    # ======================================================
    # EXECUTIVE PERFORMANCE SUMMARY
    # ======================================================

    story.append(
        Paragraph(
            "Executive Performance Summary",
            PDF_HEADING,
        )
    )

    revenue_achievement = (
        (
            metrics["Revenue"]
            / metrics["Revenue Target"]
        ) * 100
        if metrics["Revenue Target"]
        else 0
    )

    profit_achievement = (
        (
            metrics["Profit"]
            / metrics["Profit Target"]
        ) * 100
        if metrics["Profit Target"]
        else 0
    )

    order_achievement = (
        (
            metrics["Orders"]
            / metrics["Order Target"]
        ) * 100
        if metrics["Order Target"]
        else 0
    )

    customer_achievement = (
        (
            metrics["Customers"]
            / metrics["Customer Target"]
        ) * 100
        if metrics["Customer Target"]
        else 0
    )

    summary_data = [

        [
            Paragraph(
                "Metric",
                PDF_HEADER,
            ),

            Paragraph(
                "Actual",
                PDF_HEADER,
            ),

            Paragraph(
                "Target",
                PDF_HEADER,
            ),

            Paragraph(
                "Achievement",
                PDF_HEADER,
            ),
        ],

        [
            Paragraph(
                "Revenue",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{symbol}"
                f"{metrics['Revenue']:,.2f}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{symbol}"
                f"{metrics['Revenue Target']:,.2f}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{revenue_achievement:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Profit",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{symbol}"
                f"{metrics['Profit']:,.2f}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{symbol}"
                f"{metrics['Profit Target']:,.2f}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{profit_achievement:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Orders",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['Orders']:,}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['Order Target']:,}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{order_achievement:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Customers",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['Customers']:,}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['Customer Target']:,}",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{customer_achievement:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],
    ]

    summary_table = Table(
        summary_data,
        colWidths=[
            150,
            115,
            115,
            100,
        ],
    )

    summary_table.setStyle(
        TableStyle(
            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#1F4E78"),
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#B7C9E2"),
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),

                (
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
                    "RIGHT",
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),

            ]
        )
    )

    story.append(
        summary_table
    )

    story.append(
        Spacer(1, 18)
    )

    # ======================================================
    # BUSINESS PERFORMANCE
    # ======================================================

    story.append(
        Paragraph(
            "Business Performance",
            PDF_HEADING,
        )
    )

    performance_data = [

        [
            Paragraph(
                "Metric",
                PDF_HEADER,
            ),

            Paragraph(
                "Value",
                PDF_HEADER,
            ),
        ],

        [
            Paragraph(
                "Average Order",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{symbol}"
                f"{metrics['Average Order']:,.2f}",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Gross Margin",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['Gross Margin']:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Month-over-Month Growth",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['MoM Growth']:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Year-over-Year Growth",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['YoY Growth']:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Customer Growth",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['Customer Growth']:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],

        [
            Paragraph(
                "Order Growth",
                PDF_TABLE_BODY,
            ),

            Paragraph(
                f"{metrics['Order Growth']:.2f}%",
                PDF_TABLE_BODY,
            ),
        ],
    ]

    performance_table = Table(
        performance_data,
        colWidths=[
            250,
            230,
        ],
    )

    performance_table.setStyle(
        TableStyle(
            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#1F4E78"),
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#B7C9E2"),
                ),

                (
                    "ALIGN",
                    (1, 1),
                    (1, -1),
                    "RIGHT",
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),

            ]
        )
    )

    story.append(
        performance_table
    )

    story.append(
        Spacer(1, 18)
    )

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    story.append(
        Paragraph(
            "Executive Summary",
            PDF_HEADING,
        )
    )

    if metrics["Gross Margin"] >= 30:

        margin_message = (
            "Gross margin is currently at a healthy level."
        )

    else:

        margin_message = (
            "Gross margin requires management attention."
        )

    if (
        metrics["MoM Growth"] >= 0
        and metrics["YoY Growth"] >= 0
    ):

        growth_message = (
            "Overall growth indicators are positive."
        )

    else:

        growth_message = (
            "One or more growth indicators "
            "require management attention."
        )

    summary_text = (

        f"Revenue performance stands at "
        f"{symbol}{metrics['Revenue']:,.2f}, while "
        f"profit stands at "
        f"{symbol}{metrics['Profit']:,.2f}. "

        f"The current gross margin is "
        f"{metrics['Gross Margin']:.2f}%. "

        f"{margin_message} "

        f"{growth_message}"
    )

    story.append(
        Paragraph(
            summary_text,
            PDF_BODY,
        )
    )

    story.append(
        Spacer(1, 12)
    )

    # ======================================================
    # TARGET PERFORMANCE SUMMARY
    # ======================================================

    story.append(
        Paragraph(
            "Target Performance Summary",
            PDF_HEADING,
        )
    )

    target_summary = (

        f"Revenue achievement is "
        f"{revenue_achievement:.2f}%. "

        f"Profit achievement is "
        f"{profit_achievement:.2f}%. "

        f"Order achievement is "
        f"{order_achievement:.2f}%. "

        f"Customer achievement is "
        f"{customer_achievement:.2f}%."
    )

    story.append(
        Paragraph(
            target_summary,
            PDF_BODY,
        )
    )

    # ======================================================
    # BUILD PDF
    # ======================================================

    doc.build(
        story,
        onFirstPage=executive_pdf_footer,
        onLaterPages=executive_pdf_footer,
    )

    return filename


# ==========================================================
# LOAD DATA
# ==========================================================

df = load_sales_data()

df = render_sidebar(df)


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title(
    "📊 Executive Report"
)

st.caption(
    "Enterprise Executive Performance Intelligence"
)


# ==========================================================
# EXECUTIVE METRICS
# ==========================================================

metrics = executive_metrics(df)

symbol = currency_symbol()


# ==========================================================
# PRIMARY KPI ROW
# ==========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Revenue",
        f"{symbol}{metrics['Revenue']:,.2f}",
    )


with col2:

    st.metric(
        "Total Profit",
        f"{symbol}{metrics['Profit']:,.2f}",
    )


with col3:

    st.metric(
        "Total Orders",
        f"{metrics['Orders']:,}",
    )


with col4:

    st.metric(
        "Total Customers",
        f"{metrics['Customers']:,}",
    )


# ==========================================================
# SECONDARY KPI ROW
# ==========================================================

col5, col6, col7, col8 = st.columns(4)


with col5:

    st.metric(
        "Average Order",
        f"{symbol}{metrics['Average Order']:,.2f}",
    )


with col6:

    st.metric(
        "Gross Margin",
        f"{metrics['Gross Margin']:.2f}%",
    )


with col7:

    st.metric(
        "MoM Growth",
        f"{metrics['MoM Growth']:.2f}%",
    )


with col8:

    st.metric(
        "YoY Growth",
        f"{metrics['YoY Growth']:.2f}%",
    )


# ==========================================================
# GROWTH ANALYSIS
# ==========================================================

st.divider()

st.subheader(
    "📈 Growth Analysis"
)

growth_col1, growth_col2 = st.columns(2)


with growth_col1:

    st.metric(
        "Customer Growth",
        f"{metrics['Customer Growth']:.2f}%",
    )


with growth_col2:

    st.metric(
        "Order Growth",
        f"{metrics['Order Growth']:.2f}%",
    )


# ==========================================================
# TARGET PERFORMANCE
# ==========================================================

st.divider()

st.subheader(
    "🎯 Target Performance"
)


# ----------------------------------------------------------
# REVENUE
# ----------------------------------------------------------

target_col1, target_col2 = st.columns(2)


with target_col1:

    st.markdown(
        "### Revenue"
    )

    st.metric(
        "Revenue Actual",
        f"{symbol}{metrics['Revenue']:,.2f}",
    )

    st.metric(
        "Revenue Target",
        f"{symbol}{metrics['Revenue Target']:,.2f}",
    )

    if metrics["Revenue Target"]:

        revenue_achievement = (
            metrics["Revenue"]
            / metrics["Revenue Target"]
        ) * 100

        st.progress(
            min(
                revenue_achievement / 100,
                1.0,
            )
        )

        st.caption(
            f"Achievement: "
            f"{revenue_achievement:.2f}%"
        )


# ----------------------------------------------------------
# PROFIT
# ----------------------------------------------------------

with target_col2:

    st.markdown(
        "### Profit"
    )

    st.metric(
        "Profit Actual",
        f"{symbol}{metrics['Profit']:,.2f}",
    )

    st.metric(
        "Profit Target",
        f"{symbol}{metrics['Profit Target']:,.2f}",
    )

    if metrics["Profit Target"]:

        profit_achievement = (
            metrics["Profit"]
            / metrics["Profit Target"]
        ) * 100

        st.progress(
            min(
                profit_achievement / 100,
                1.0,
            )
        )

        st.caption(
            f"Achievement: "
            f"{profit_achievement:.2f}%"
        )


# ----------------------------------------------------------
# ORDERS
# ----------------------------------------------------------

target_col3, target_col4 = st.columns(2)


with target_col3:

    st.markdown(
        "### Orders"
    )

    st.metric(
        "Orders Actual",
        f"{metrics['Orders']:,}",
    )

    st.metric(
        "Orders Target",
        f"{metrics['Order Target']:,}",
    )

    if metrics["Order Target"]:

        order_achievement = (
            metrics["Orders"]
            / metrics["Order Target"]
        ) * 100

        st.progress(
            min(
                order_achievement / 100,
                1.0,
            )
        )

        st.caption(
            f"Achievement: "
            f"{order_achievement:.2f}%"
        )


# ----------------------------------------------------------
# CUSTOMERS
# ----------------------------------------------------------

with target_col4:

    st.markdown(
        "### Customers"
    )

    st.metric(
        "Customers Actual",
        f"{metrics['Customers']:,}",
    )

    st.metric(
        "Customers Target",
        f"{metrics['Customer Target']:,}",
    )

    if metrics["Customer Target"]:

        customer_achievement = (
            metrics["Customers"]
            / metrics["Customer Target"]
        ) * 100

        st.progress(
            min(
                customer_achievement / 100,
                1.0,
            )
        )

        st.caption(
            f"Achievement: "
            f"{customer_achievement:.2f}%"
        )


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

st.divider()

st.subheader(
    "🧠 Executive Summary"
)

st.info(
    f"""
**Revenue:** {symbol}{metrics['Revenue']:,.2f}

**Profit:** {symbol}{metrics['Profit']:,.2f}

**Gross Margin:** {metrics['Gross Margin']:.2f}%

**MoM Growth:** {metrics['MoM Growth']:.2f}%

**YoY Growth:** {metrics['YoY Growth']:.2f}%

The Executive Report presents enterprise performance
using the existing executive metrics engine.
"""
)


# ==========================================================
# EXECUTIVE PDF EXPORT
# ==========================================================

st.divider()

st.subheader(
    "📄 Executive Report PDF"
)

if st.button(
    "Generate Executive PDF",
    type="primary",
):

    try:

        pdf_file = create_executive_pdf(
            metrics
        )

        with open(
            pdf_file,
            "rb",
        ) as file:

            pdf_bytes = file.read()

        st.download_button(
            label="⬇️ Download Executive Report",
            data=pdf_bytes,
            file_name="Enterprise_Executive_Report.pdf",
            mime="application/pdf",
        )

        st.success(
            "Executive PDF generated successfully."
        )

    except Exception as e:

        st.error(
            f"Unable to generate Executive PDF: {e}"
        )

