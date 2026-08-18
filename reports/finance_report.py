import os

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

from reports.report_styles import (
    FONT_REGULAR,
    FONT_BOLD,
)

from reports.report_utils import (
    report_date,
    report_time,
)


# ==========================================================
# FILE PATHS
# ==========================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

LOGO_PATH = os.path.join(
    PROJECT_ROOT,
    "assets",
    "company_logo.png",
)


# ==========================================================
# REPORT STYLES
# ==========================================================

TITLE_STYLE = ParagraphStyle(
    "FinanceTitle",
    fontName=FONT_BOLD,
    fontSize=18,
    leading=22,
    alignment=TA_CENTER,
    spaceAfter=8,
)


SUBTITLE_STYLE = ParagraphStyle(
    "FinanceSubtitle",
    fontName=FONT_REGULAR,
    fontSize=11,
    leading=14,
    alignment=TA_CENTER,
    spaceAfter=8,
)


HEADING_STYLE = ParagraphStyle(
    "FinanceHeading",
    fontName=FONT_BOLD,
    fontSize=13,
    leading=16,
    alignment=TA_LEFT,
    spaceBefore=4,
    spaceAfter=8,
)


BODY_STYLE = ParagraphStyle(
    "FinanceBody",
    fontName=FONT_REGULAR,
    fontSize=9.5,
    leading=13,
    alignment=TA_LEFT,
)


TABLE_HEADER_STYLE = ParagraphStyle(
    "FinanceTableHeader",
    fontName=FONT_BOLD,
    fontSize=8,
    leading=10,
    textColor=colors.white,
)


TABLE_BODY_STYLE = ParagraphStyle(
    "FinanceTableBody",
    fontName=FONT_REGULAR,
    fontSize=8,
    leading=10,
)


# ==========================================================
# FOOTER
# ==========================================================

def add_footer(canvas, doc):

    canvas.saveState()

    width, height = A4

    # ------------------------------------------------------
    # Footer line
    # ------------------------------------------------------

    canvas.setStrokeColor(
        colors.HexColor("#D9E2F3")
    )

    canvas.setLineWidth(0.5)

    canvas.line(
        36,
        35,
        width - 36,
        35,
    )

    # ------------------------------------------------------
    # Footer text
    # ------------------------------------------------------

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
        "MICT E-LEARNING SERVICES LTD",
    )

    canvas.drawRightString(
        width - 36,
        22,
        f"Page {doc.page}",
    )

    canvas.restoreState()


# ==========================================================
# SAFE VALUE HELPERS
# ==========================================================

def safe_value(insight, key, default=0):

    value = insight.get(
        key,
        default,
    )

    if value is None:
        return default

    return value


def safe_number(value):

    try:
        return float(value)

    except (
        TypeError,
        ValueError,
    ):
        return 0.0


def safe_text(value):

    if value is None:
        return ""

    return str(value)


def clean_recommendation(text):

    text = safe_text(text)

    remove_items = [
        "**",
        "`",
        "✅",
        "⚠️",
        "🚨",
        "🌍",
        "🏷️",
        "🏆",
        "📊",
        "🚚",
        "📈",
        "💰",
        "📦",
    ]

    for item in remove_items:

        text = text.replace(
            item,
            "",
        )

    return text.strip()


# ==========================================================
# TABLE STYLE
# ==========================================================

def apply_standard_table_style(
    table,
    header_color="#1F4E78",
):

    table.setStyle(
        TableStyle(
            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        header_color
                    ),
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor(
                        "#B7C9E2"
                    ),
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
                    6,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),

            ]
        )
    )

    return table


# ==========================================================
# FINANCE EXECUTIVE REPORT
# ==========================================================

def create_finance_report(
    insight,
    df,
):

    filename = (
        "Enterprise_Finance_Report.pdf"
    )

    # ======================================================
    # PDF DOCUMENT
    # ======================================================

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=42,
        bottomMargin=50,
        title="Financial Executive Board Report",
        author="MICT E-LEARNING SERVICES LTD",
    )

    story = []


    # ======================================================
    # LOGO
    # ======================================================

    if os.path.isfile(LOGO_PATH):

        try:

            logo = Image(
                LOGO_PATH,
                width=110,
                height=55,
                kind="proportional",
            )

            logo.hAlign = "CENTER"

            story.append(
                logo
            )

            story.append(
                Spacer(
                    1,
                    8,
                )
            )

        except Exception:

            # Logo should never stop PDF generation
            pass


    # ======================================================
    # REPORT HEADER
    # ======================================================

    story.append(
        Paragraph(
            "MICT E-LEARNING SERVICES LTD",
            TITLE_STYLE,
        )
    )

    story.append(
        Paragraph(
            "Enterprise Financial Analytics Platform",
            SUBTITLE_STYLE,
        )
    )

    story.append(
        Paragraph(
            "FINANCIAL EXECUTIVE BOARD REPORT",
            HEADING_STYLE,
        )
    )

    story.append(
        Spacer(
            1,
            5,
        )
    )

    story.append(
        Paragraph(
            f"Generated: "
            f"{report_date()} "
            f"{report_time()}",
            BODY_STYLE,
        )
    )

    story.append(
        Spacer(
            1,
            18,
        )
    )


    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    story.append(
        Paragraph(
            "Executive Financial Summary",
            HEADING_STYLE,
        )
    )

    summary_data = [

        [
            Paragraph(
                "Financial Metric",
                TABLE_HEADER_STYLE,
            ),

            Paragraph(
                "Value",
                TABLE_HEADER_STYLE,
            ),
        ],

        [
            Paragraph(
                "Revenue",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"₦{safe_number(safe_value(insight, 'Revenue')):,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Cost",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"₦{safe_number(safe_value(insight, 'Cost')):,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Profit",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"₦{safe_number(safe_value(insight, 'Profit')):,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Profit Margin",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"{safe_number(safe_value(insight, 'Margin')):.2f}%",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Shipping Cost",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"₦{safe_number(safe_value(insight, 'Shipping Cost')):,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Average Order Value",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                f"₦{safe_number(safe_value(insight, 'Average Order Value')):,.2f}",
                TABLE_BODY_STYLE,
            ),
        ],

        [
            Paragraph(
                "Financial Status",
                TABLE_BODY_STYLE,
            ),

            Paragraph(
                safe_text(
                    safe_value(
                        insight,
                        "Status",
                        "N/A",
                    )
                ),
                TABLE_BODY_STYLE,
            ),
        ],
    ]


    summary_table = Table(
        summary_data,
        colWidths=[
            230,
            250,
        ],
    )

    apply_standard_table_style(
        summary_table
    )

    story.append(
        summary_table
    )

    story.append(
        Spacer(
            1,
            18,
        )
    )


    # ======================================================
    # FINANCIAL HIGHLIGHTS
    # ======================================================

    story.append(
        Paragraph(
            "Financial Business Highlights",
            HEADING_STYLE,
        )
    )

    highlights = [

        (
            "Best Region",
            safe_value(
                insight,
                "Best Region",
                "N/A",
            ),
        ),

        (
            "Best Category",
            safe_value(
                insight,
                "Best Category",
                "N/A",
            ),
        ),

        (
            "Top Profit Product",
            safe_value(
                insight,
                "Top Profit Product",
                "N/A",
            ),
        ),

        (
            "Top Revenue Product",
            safe_value(
                insight,
                "Top Revenue Product",
                "N/A",
            ),
        ),

    ]

    for label, value in highlights:

        story.append(
            Paragraph(
                f"• {label}: "
                f"<b>{safe_text(value)}</b>",
                BODY_STYLE,
            )
        )

        story.append(
            Spacer(
                1,
                4,
            )
        )


    concentration = safe_number(
        safe_value(
            insight,
            "Concentration",
            0,
        )
    )

    story.append(
        Paragraph(
            f"• Top 10 Product Revenue "
            f"Concentration: "
            f"<b>{concentration:.2f}%</b>",
            BODY_STYLE,
        )
    )

    story.append(
        Spacer(
            1,
            12,
        )
    )


    # ======================================================
    # AI FINANCIAL RECOMMENDATIONS
    # ======================================================

    story.append(
        Paragraph(
            "AI Financial Recommendations",
            HEADING_STYLE,
        )
    )

    recommendations = safe_value(
        insight,
        "Recommendations",
        [],
    )

    if not recommendations:

        story.append(
            Paragraph(
                "No financial recommendations "
                "were generated for this reporting period.",
                BODY_STYLE,
            )
        )

    else:

        for recommendation in recommendations:

            clean = clean_recommendation(
                recommendation
            )

            if not clean:
                continue

            story.append(
                Paragraph(
                    f"• {clean}",
                    BODY_STYLE,
                )
            )

            story.append(
                Spacer(
                    1,
                    4,
                )
            )

    story.append(
        Spacer(
            1,
            15,
        )
    )


    # ======================================================
    # REGIONAL FINANCIAL PERFORMANCE
    # ======================================================

    story.append(
        Paragraph(
            "Regional Financial Performance",
            HEADING_STYLE,
        )
    )


    # ------------------------------------------------------
    # Validate required columns
    # ------------------------------------------------------

    required_columns = {
        "Region",
        "Revenue",
        "Cost",
        "Profit",
    }

    if required_columns.issubset(
        set(df.columns)
    ):

        regional = (
            df.groupby("Region")
            .agg(
                Revenue=(
                    "Revenue",
                    "sum",
                ),
                Cost=(
                    "Cost",
                    "sum",
                ),
                Profit=(
                    "Profit",
                    "sum",
                ),
            )
            .reset_index()
        )

        regional["Profit Margin"] = (
            regional["Profit"]
            / regional["Revenue"]
            .replace(
                0,
                float("nan"),
            )
            * 100
        )

        regional_data = [

            [
                Paragraph(
                    "Region",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Revenue",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Cost",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Profit",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Margin",
                    TABLE_HEADER_STYLE,
                ),
            ]
        ]


        for _, row in regional.iterrows():

            margin = row[
                "Profit Margin"
            ]

            if margin != margin:
                margin = 0


            regional_data.append(
                [

                    Paragraph(
                        safe_text(
                            row["Region"]
                        ),
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"₦{safe_number(row['Revenue']):,.0f}",
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"₦{safe_number(row['Cost']):,.0f}",
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"₦{safe_number(row['Profit']):,.0f}",
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"{safe_number(margin):.2f}%",
                        TABLE_BODY_STYLE,
                    ),
                ]
            )


        regional_table = Table(
            regional_data,
            colWidths=[
                90,
                115,
                115,
                115,
                65,
            ],
            repeatRows=1,
        )


        apply_standard_table_style(
            regional_table
        )


        regional_table.setStyle(
            TableStyle(
                [
                    (
                        "ALIGN",
                        (1, 1),
                        (-1, -1),
                        "RIGHT",
                    ),
                ]
            )
        )


        story.append(
            regional_table
        )

    else:

        story.append(
            Paragraph(
                "Regional financial data is unavailable "
                "because the required columns were not found.",
                BODY_STYLE,
            )
        )


    story.append(
        Spacer(
            1,
            18,
        )
    )


    # ======================================================
    # CATEGORY FINANCIAL PERFORMANCE
    # ======================================================

    story.append(
        Paragraph(
            "Category Financial Performance",
            HEADING_STYLE,
        )
    )


    required_category_columns = {
        "Category",
        "Revenue",
        "Cost",
        "Profit",
    }


    if required_category_columns.issubset(
        set(df.columns)
    ):

        category = (
            df.groupby("Category")
            .agg(
                Revenue=(
                    "Revenue",
                    "sum",
                ),
                Cost=(
                    "Cost",
                    "sum",
                ),
                Profit=(
                    "Profit",
                    "sum",
                ),
            )
            .reset_index()
        )


        category["Profit Margin"] = (
            category["Profit"]
            / category["Revenue"]
            .replace(
                0,
                float("nan"),
            )
            * 100
        )


        category_data = [

            [
                Paragraph(
                    "Category",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Revenue",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Cost",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Profit",
                    TABLE_HEADER_STYLE,
                ),

                Paragraph(
                    "Margin",
                    TABLE_HEADER_STYLE,
                ),
            ]
        ]


        for _, row in category.iterrows():

            margin = row[
                "Profit Margin"
            ]

            if margin != margin:
                margin = 0


            category_data.append(
                [

                    Paragraph(
                        safe_text(
                            row["Category"]
                        ),
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"₦{safe_number(row['Revenue']):,.0f}",
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"₦{safe_number(row['Cost']):,.0f}",
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"₦{safe_number(row['Profit']):,.0f}",
                        TABLE_BODY_STYLE,
                    ),

                    Paragraph(
                        f"{safe_number(margin):.2f}%",
                        TABLE_BODY_STYLE,
                    ),
                ]
            )


        category_table = Table(
            category_data,
            colWidths=[
                90,
                115,
                115,
                115,
                65,
            ],
            repeatRows=1,
        )


        apply_standard_table_style(
            category_table
        )


        category_table.setStyle(
            TableStyle(
                [
                    (
                        "ALIGN",
                        (1, 1),
                        (-1, -1),
                        "RIGHT",
                    ),
                ]
            )
        )


        story.append(
            category_table
        )

    else:

        story.append(
            Paragraph(
                "Category financial data is unavailable "
                "because the required columns were not found.",
                BODY_STYLE,
            )
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
