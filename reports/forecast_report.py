import os
from pathlib import Path

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
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle

from reports.report_styles import (
    TITLE_STYLE,
    HEADING_STYLE,
    BODY_STYLE,
    FONT_REGULAR,
    FONT_BOLD,
)

from reports.report_utils import (
    report_date,
    report_time,
)


# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOGO_PATH = (
    PROJECT_ROOT
    / "assets"
    / "company_logo.png"
)


# ==========================================================
# FORECAST REPORT-SPECIFIC STYLES
# ==========================================================

SUBTITLE_STYLE = ParagraphStyle(
    "ForecastSubtitle",
    fontName=FONT_REGULAR,
    fontSize=11,
    leading=14,
    alignment=TA_CENTER,
    spaceAfter=8,
)


TABLE_HEADER_STYLE = ParagraphStyle(
    "ForecastTableHeader",
    fontName=FONT_BOLD,
    fontSize=8,
    leading=10,
    textColor=colors.white,
)


TABLE_BODY_STYLE = ParagraphStyle(
    "ForecastTableBody",
    fontName=FONT_REGULAR,
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

    if (
        not include_footer
        and not include_page_numbers
    ):
        return

    canvas.saveState()

    width, height = A4

    # ------------------------------------------------------
    # FOOTER LINE
    # ------------------------------------------------------

    if include_footer:

        canvas.setStrokeColor(
            colors.HexColor("#D9E2F3")
        )

        canvas.setLineWidth(0.7)

        canvas.line(
            36,
            35,
            width - 36,
            35,
        )

        # --------------------------------------------------
        # CENTRALIZED PROJECT FONT
        # --------------------------------------------------

        canvas.setFont(
            FONT_REGULAR,
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
            FONT_REGULAR,
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
# FORECAST EXECUTIVE REPORT
# ==========================================================

def create_forecast_report(
    insight,
    df,
    forecast,
):

    company_name = get_setting(
        "company_name",
        "MICT E-LEARNING SERVICES LTD",
    )

    filename = (
        "Enterprise_Forecast_Report.pdf"
    )

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
        and LOGO_PATH.exists()
    ):

        logo = Image(
            str(LOGO_PATH),
            width=110,
            height=55,
            kind="proportional",
        )

        logo.hAlign = "CENTER"

        story.append(
            logo
        )

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
                str(insight["Status"]),
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
            str(insight["Outlook"]),
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

    for recommendation in insight.get(
        "Recommendations",
        [],
    ):

        clean_recommendation = (
            str(recommendation)
            .replace("**", "")
            .replace("`", "")
            .replace("âœ…", "")
            .replace("âš ï¸¢", "")
            .replace("ðŸš¨", "")
            .replace("ðŸ“ˆ", "")
            .replace("ðŸ’°", "")
            .replace("ðŸ“¦", "")
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
    # NEXT MONTH FORECAST
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
    # BUILD PDF
    # ======================================================

    doc.build(
        story,
        onFirstPage=add_footer,
        onLaterPages=add_footer,
    )


    return filename