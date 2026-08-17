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

CALIBRI_PATH = (
    r"C:\Windows\Fonts\calibri.ttf"
)

CALIBRI_BOLD_PATH = (
    r"C:\Windows\Fonts\calibrib.ttf"
)


# ==========================================================
# REGISTER FONTS
# ==========================================================

pdfmetrics.registerFont(
    TTFont(
        "Calibri",
        CALIBRI_PATH
    )
)

pdfmetrics.registerFont(
    TTFont(
        "Calibri-Bold",
        CALIBRI_BOLD_PATH
    )
)


# ==========================================================
# REPORT STYLES
# ==========================================================

TITLE_STYLE = ParagraphStyle(
    "FinanceTitle",
    fontName="Calibri-Bold",
    fontSize=18,
    leading=22,
    alignment=TA_CENTER,
    spaceAfter=8,
)

SUBTITLE_STYLE = ParagraphStyle(
    "FinanceSubtitle",
    fontName="Calibri",
    fontSize=11,
    leading=14,
    alignment=TA_CENTER,
    spaceAfter=8,
)

HEADING_STYLE = ParagraphStyle(
    "FinanceHeading",
    fontName="Calibri-Bold",
    fontSize=13,
    leading=16,
    alignment=TA_LEFT,
    spaceBefore=4,
    spaceAfter=8,
)

BODY_STYLE = ParagraphStyle(
    "FinanceBody",
    fontName="Calibri",
    fontSize=9.5,
    leading=13,
    alignment=TA_LEFT,
)

TABLE_HEADER_STYLE = ParagraphStyle(
    "FinanceTableHeader",
    fontName="Calibri-Bold",
    fontSize=8,
    leading=10,
    textColor=colors.white,
)

TABLE_BODY_STYLE = ParagraphStyle(
    "FinanceTableBody",
    fontName="Calibri",
    fontSize=8,
    leading=10,
)


# ==========================================================
# FOOTER
# ==========================================================

def add_footer(canvas, doc):

    canvas.saveState()

    width, height = A4

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
        "MICT E-LEARNING SERVICES LTD"
    )

    canvas.drawRightString(
        width - 36,
        22,
        f"Page {doc.page}"
    )

    canvas.restoreState()


# ==========================================================
# FINANCE EXECUTIVE REPORT
# ==========================================================

def create_finance_report(
    insight,
    df
):

    filename = (
        "Enterprise_Finance_Report.pdf"
    )

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

    if os.path.exists(LOGO_PATH):

        logo = Image(
            LOGO_PATH,
            width=110,
            height=55,
            kind="proportional"
        )

        logo.hAlign = "CENTER"

        story.append(
            logo
        )

        story.append(
            Spacer(1, 8)
        )

    # ======================================================
    # REPORT HEADER
    # ======================================================

    story.append(
        Paragraph(
            "MICT E-LEARNING SERVICES LTD",
            TITLE_STYLE
        )
    )

    story.append(
        Paragraph(
            "Enterprise Financial Analytics Platform",
            SUBTITLE_STYLE
        )
    )

    story.append(
        Paragraph(
            "FINANCIAL EXECUTIVE BOARD REPORT",
            HEADING_STYLE
        )
    )

    story.append(
        Spacer(1, 5)
    )

    story.append(
        Paragraph(
            f"Generated: "
            f"{report_date()} "
            f"{report_time()}",
            BODY_STYLE
        )
    )

    story.append(
        Spacer(1, 18)
    )

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    story.append(
        Paragraph(
            "Executive Financial Summary",
            HEADING_STYLE
        )
    )

    summary_data = [

        [
            Paragraph(
                "Financial Metric",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Value",
                TABLE_HEADER_STYLE
            ),
        ],

        [
            Paragraph(
                "Revenue",
                TABLE_BODY_STYLE
            ),
            Paragraph(
                f"₦{insight['Revenue']:,.2f}",
                TABLE_BODY_STYLE
            ),
        ],

        [
            Paragraph(
                "Cost",
                TABLE_BODY_STYLE
            ),
            Paragraph(
                f"₦{insight['Cost']:,.2f}",
                TABLE_BODY_STYLE
            ),
        ],

        [
            Paragraph(
                "Profit",
                TABLE_BODY_STYLE
            ),
            Paragraph(
                f"₦{insight['Profit']:,.2f}",
                TABLE_BODY_STYLE
            ),
        ],

        [
            Paragraph(
                "Profit Margin",
                TABLE_BODY_STYLE
            ),
            Paragraph(
                f"{insight['Margin']:.2f}%",
                TABLE_BODY_STYLE
            ),
        ],

        [
            Paragraph(
                "Shipping Cost",
                TABLE_BODY_STYLE
            ),
            Paragraph(
                f"₦{insight['Shipping Cost']:,.2f}",
                TABLE_BODY_STYLE
            ),
        ],

        [
            Paragraph(
                "Average Order Value",
                TABLE_BODY_STYLE
            ),
            Paragraph(
                f"₦{insight['Average Order Value']:,.2f}",
                TABLE_BODY_STYLE
            ),
        ],

        [
            Paragraph(
                "Financial Status",
                TABLE_BODY_STYLE
            ),
            Paragraph(
                insight["Status"],
                TABLE_BODY_STYLE
            ),
        ],
    ]

    summary_table = Table(
        summary_data,
        colWidths=[
            230,
            250
        ]
    )

    summary_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#1F4E78"
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
    # FINANCIAL HIGHLIGHTS
    # ======================================================

    story.append(
        Paragraph(
            "Financial Business Highlights",
            HEADING_STYLE
        )
    )

    highlights = [

        f"Best Region: <b>"
        f"{insight['Best Region']}"
        f"</b>",

        f"Best Category: <b>"
        f"{insight['Best Category']}"
        f"</b>",

        f"Top Profit Product: <b>"
        f"{insight['Top Profit Product']}"
        f"</b>",

        f"Top Revenue Product: <b>"
        f"{insight['Top Revenue Product']}"
        f"</b>",

        f"Top 10 Product Revenue "
        f"Concentration: <b>"
        f"{insight['Concentration']:.2f}%"
        f"</b>",
    ]

    for item in highlights:

        story.append(
            Paragraph(
                f"• {item}",
                BODY_STYLE
            )
        )

        story.append(
            Spacer(1, 4)
        )

    story.append(
        Spacer(1, 12)
    )

    # ======================================================
    # AI RECOMMENDATIONS
    # ======================================================

    story.append(
        Paragraph(
            "AI Financial Recommendations",
            HEADING_STYLE
        )
    )

    for recommendation in insight[
        "Recommendations"
    ]:

        clean_recommendation = (
            recommendation
            .replace("**", "")
            .replace("✅", "")
            .replace("⚠️", "")
            .replace("🚨", "")
            .replace("🌍", "")
            .replace("🏷️", "")
            .replace("🏆", "")
            .replace("📊", "")
            .replace("🚚", "")
        )

        story.append(
            Paragraph(
                clean_recommendation.strip(),
                BODY_STYLE
            )
        )

        story.append(
            Spacer(1, 4)
        )

    story.append(
        Spacer(1, 15)
    )

    # ======================================================
    # REGIONAL FINANCIAL PERFORMANCE
    # ======================================================

    story.append(
        Paragraph(
            "Regional Financial Performance",
            HEADING_STYLE
        )
    )

    regional = (
        df.groupby("Region")
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
        .reset_index()
    )

    regional["Profit Margin"] = (
        regional["Profit"]
        / regional["Revenue"]
        * 100
    )

    regional_data = [

        [
            Paragraph(
                "Region",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Revenue",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Cost",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Profit",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Margin",
                TABLE_HEADER_STYLE
            ),
        ]
    ]

    for _, row in regional.iterrows():

        regional_data.append(
            [
                Paragraph(
                    str(row["Region"]),
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"₦{row['Revenue']:,.0f}",
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"₦{row['Cost']:,.0f}",
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"₦{row['Profit']:,.0f}",
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"{row['Profit Margin']:.2f}%",
                    TABLE_BODY_STYLE
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
            65
        ],
        repeatRows=1
    )

    regional_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#1F4E78"
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
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
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
                    5,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
            ]
        )
    )

    story.append(
        regional_table
    )

    story.append(
        Spacer(1, 18)
    )

    # ======================================================
    # CATEGORY FINANCIAL PERFORMANCE
    # ======================================================

    story.append(
        Paragraph(
            "Category Financial Performance",
            HEADING_STYLE
        )
    )

    category = (
        df.groupby("Category")
        .agg(
            Revenue=("Revenue", "sum"),
            Cost=("Cost", "sum"),
            Profit=("Profit", "sum"),
        )
        .reset_index()
    )

    category["Profit Margin"] = (
        category["Profit"]
        / category["Revenue"]
        * 100
    )

    category_data = [

        [
            Paragraph(
                "Category",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Revenue",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Cost",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Profit",
                TABLE_HEADER_STYLE
            ),
            Paragraph(
                "Margin",
                TABLE_HEADER_STYLE
            ),
        ]
    ]

    for _, row in category.iterrows():

        category_data.append(
            [
                Paragraph(
                    str(row["Category"]),
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"₦{row['Revenue']:,.0f}",
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"₦{row['Cost']:,.0f}",
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"₦{row['Profit']:,.0f}",
                    TABLE_BODY_STYLE
                ),

                Paragraph(
                    f"{row['Profit Margin']:.2f}%",
                    TABLE_BODY_STYLE
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
            65
        ],
        repeatRows=1
    )

    category_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#1F4E78"
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
                    "ALIGN",
                    (1, 1),
                    (-1, -1),
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
                    5,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
            ]
        )
    )

    story.append(
        category_table
    )

    # ======================================================
    # BUILD PDF
    # ======================================================

    doc.build(
        story,
        onFirstPage=add_footer,
        onLaterPages=add_footer
    )

    return filename


