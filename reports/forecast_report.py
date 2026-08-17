import os

from engines.settings_engine import (
    get_setting,
    currency_symbol,
)

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
# REGISTER FONTS
# ==========================================================

if "Calibri" not in pdfmetrics.getRegisteredFontNames():

    pdfmetrics.registerFont(
        TTFont(
            "Calibri",
            CALIBRI_PATH
        )
    )


if "Calibri-Bold" not in pdfmetrics.getRegisteredFontNames():

    pdfmetrics.registerFont(
        TTFont(
            "Calibri-Bold",
            CALIBRI_BOLD_PATH
        )
    )


# ==========================================================
# STYLES
# ==========================================================

TITLE_STYLE = ParagraphStyle(
    "ForecastTitle",
    fontName="Calibri-Bold",
    fontSize=18,
    leading=22,
    alignment=TA_CENTER,
    spaceAfter=8,
)


SUBTITLE_STYLE = ParagraphStyle(
    "ForecastSubtitle",
    fontName="Calibri",
    fontSize=11,
    leading=14,
    alignment=TA_CENTER,
    spaceAfter=8,
)


HEADING_STYLE = ParagraphStyle(
    "ForecastHeading",
    fontName="Calibri-Bold",
    fontSize=13,
    leading=16,
    alignment=TA_LEFT,
    spaceBefore=4,
    spaceAfter=8,
)


BODY_STYLE = ParagraphStyle(
    "ForecastBody",
    fontName="Calibri",
    fontSize=9.5,
    leading=13,
    alignment=TA_LEFT,
)


TABLE_HEADER_STYLE = ParagraphStyle(
    "ForecastTableHeader",
    fontName="Calibri-Bold",
    fontSize=8,
    leading=10,
    textColor=colors.white,
)


TABLE_BODY_STYLE = ParagraphStyle(
    "ForecastTableBody",
    fontName="Calibri",
    fontSize=8,
    leading=10,
)


# ==========================================================
# FOOTER
# ==========================================================

def add_footer(canvas, doc):

    include_footer = get_setting(
        "include_footer",
        True,
    )

    include_page_numbers = get_setting(
        "include_page_numbers",
        True,
    )

    # Nothing to draw
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
            35
        )

        canvas.setFont(
            "Calibri",
            8
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
            )
        )

    # ------------------------------------------------------
    # PAGE NUMBER
    # ------------------------------------------------------

    if include_page_numbers:

        canvas.setFont(
            "Calibri",
            8
        )

        canvas.setFillColor(
            colors.HexColor("#666666")
        )

        canvas.drawRightString(
            width - 36,
            22,
            f"Page {doc.page}"
        )

    canvas.restoreState()


# ==========================================================
# FORECAST EXECUTIVE REPORT
# ==========================================================

def create_forecast_report(
    insight,
    df,
    forecast
):

    company_name = get_setting(
        "company_name",
        "MICT E-LEARNING SERVICES LTD",
    )

    filename = "Enterprise_Forecast_Report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=42,
        bottomMargin=50,
        title="Forecast Executive Board Report",
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
            TITLE_STYLE,
        )
    )

    story.append(
        Paragraph(
            "Enterprise Sales Analytics Platform",
            SUBTITLE_STYLE,
        )
    )

    story.append(
        Paragraph(
            "FORECAST EXECUTIVE BOARD REPORT",
            HEADING_STYLE,
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
                BODY_STYLE,
            )
        )

        story.append(
            Spacer(1, 18)
        )


    # ======================================================
    # FORECAST SUMMARY
    # ======================================================

    story.append(
        Paragraph(
            "Forecast Executive Summary",
            HEADING_STYLE,
        )
    )

    summary_data = [

        [
            Paragraph(
                "Forecast Metric",
                TABLE_HEADER_STYLE,
            ),

            Paragraph(
                "Forecast Value",
                TABLE_HEADER_STYLE,
            ),
        ],

        [
            Paragraph(
                "Expected Revenue",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{currency_symbol()}"
                f"{insight['Revenue']:,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Expected Profit",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{currency_symbol()}"
                f"{insight['Profit']:,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Expected Orders",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{insight['Orders']:,.0f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Revenue Growth",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{insight['Growth']:.2f}%",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Forecast Profit Margin",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{insight['Margin']:.2f}%",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Forecast Status",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                insight["Status"],
                TABLE_BODY_STYLE,
            ),
        ],
    ]


    summary_table = Table(
        summary_data,
        colWidths=[
            250,
            230,
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
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    8,
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    8,
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
    # BUSINESS OUTLOOK
    # ======================================================

    story.append(
        Paragraph(
            "Business Outlook",
            HEADING_STYLE,
        )
    )

    story.append(
        Paragraph(
            insight["Outlook"],
            BODY_STYLE,
        )
    )

    story.append(
        Spacer(1, 15)
    )


    # ======================================================
    # FORECAST RECOMMENDATIONS
    # ======================================================

    story.append(
        Paragraph(
            "AI Forecast Recommendations",
            HEADING_STYLE,
        )
    )


    for recommendation in insight[
        "Recommendations"
    ]:

        clean_recommendation = (
            recommendation
            .replace("**", "")
            .replace("`", "")
            .replace("✅", "")
            .replace("⚠️", "")
            .replace("🚨", "")
            .replace("📈", "")
            .replace("💰", "")
            .replace("📦", "")
        )

        story.append(
            Paragraph(
                f"• {clean_recommendation.strip()}",
                BODY_STYLE,
            )
        )

        story.append(
            Spacer(1, 4)
        )


    story.append(
        Spacer(1, 15)
    )


    # ======================================================
    # FORECAST TABLE
    # ======================================================

    story.append(
        Paragraph(
            "Next Month Forecast",
            HEADING_STYLE,
        )
    )


    forecast_data = [

        [
            Paragraph(
                "Metric",
                TABLE_HEADER_STYLE,
            ),

            Paragraph(
                "Forecast",
                TABLE_HEADER_STYLE,
            ),
        ],

        [
            Paragraph(
                "Revenue",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{currency_symbol()}"
                f"{forecast['Revenue']:,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Profit",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{currency_symbol()}"
                f"{forecast['Profit']:,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Orders",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{forecast['Orders']:,.0f}",
                TABLE_BODY_STYLE,
            ),
        ],
    ]


    forecast_table = Table(
        forecast_data,
        colWidths=[
            250,
            230,
        ],
    )


    forecast_table.setStyle(
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
                    (1, -1),
                    "RIGHT",
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
        forecast_table
    )


    # ======================================================
    # BUILD REPORT
    # ======================================================

    doc.build(
        story,
        onFirstPage=add_footer,
        onLaterPages=add_footer,
    )


    return filename