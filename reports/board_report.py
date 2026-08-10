from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    HRFlowable,
)

# --------------------------------------------------------
# STYLES
# --------------------------------------------------------

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = colors.HexColor("#1E3A8A")
title_style.fontName = "Helvetica-Bold"
title_style.fontSize = 24
title_style.spaceAfter = 10

heading = styles["Heading2"]
heading.textColor = colors.HexColor("#2563EB")
heading.fontName = "Helvetica-Bold"
heading.fontSize = 15
heading.spaceBefore = 8
heading.spaceAfter = 6

normal = styles["BodyText"]
normal.fontName = "Helvetica"
normal.fontSize = 10
normal.leading = 13
normal.spaceAfter = 2


# --------------------------------------------------------
# HELPERS
# --------------------------------------------------------

def section(title):
    return Paragraph(title, heading)


def divider():
    return HRFlowable(
        width="100%",
        thickness=0.8,
        color=colors.HexColor("#2563EB"),
        spaceBefore=4,
        spaceAfter=8,
    )


# --------------------------------------------------------
# PDF BUILDER
# --------------------------------------------------------

def build_pdf(
    report,
    filename,
    kpi_table,
    revenue_chart_path=None,
    profit_chart_path=None,
):

    doc = SimpleDocTemplate(filename)

    story = []

    # ----------------------------------------------------
    # LOGO
    # ----------------------------------------------------

    logo = Path.cwd() / "assets" / "company_logo.png"

    if logo.exists():

        story.append(
            Image(
                str(logo),
                width=1.2 * inch,
                height=1.2 * inch,
            )
        )

    story.append(Spacer(1, 12))

    # ----------------------------------------------------
    # TITLE
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "ENTERPRISE SALES ANALYTICS",
            title_style,
        )
    )

    story.append(
        Paragraph(
            "Executive Board Report",
            heading,
        )
    )

    story.append(
        Paragraph(
            "MICT E-LEARNING SERVICES LIMITED",
            normal,
        )
    )

    story.append(Spacer(1, 18))

    # ----------------------------------------------------
    # EXECUTIVE SUMMARY
    # ----------------------------------------------------

    story.append(section("Executive Summary"))
    story.append(divider())

    for key, value in report["summary"].items():

        story.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                normal,
            )
        )

    story.append(Spacer(1, 16))

    # ----------------------------------------------------
    # KPI TABLE
    # ----------------------------------------------------

    story.append(section("Executive KPI Summary"))
    story.append(divider())

    table = Table(kpi_table)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563EB")),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("FONTSIZE", (0, 0), (-1, 0), 11),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

                ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("ALIGN", (1, 1), (-1, -1), "CENTER"),

            ]

        )

    )

    story.append(table)

    story.append(Spacer(1, 20))

    # ----------------------------------------------------
    # REVENUE CHART
    # ----------------------------------------------------

    if revenue_chart_path:

        story.append(section("Revenue Trend"))
        story.append(divider())

        story.append(
            Image(
                revenue_chart_path,
                width=6.4 * inch,
                height=3.2 * inch,
            )
        )

        story.append(Spacer(1, 18))

    # ----------------------------------------------------
    # PROFIT CHART
    # ----------------------------------------------------

    if profit_chart_path:

        story.append(section("Profit Trend"))
        story.append(divider())

        story.append(
            Image(
                profit_chart_path,
                width=6.4 * inch,
                height=3.2 * inch,
            )
        )

        story.append(Spacer(1, 18))

    # ----------------------------------------------------
    # AI NARRATIVE
    # ----------------------------------------------------

    story.append(section("AI Executive Narrative"))
    story.append(divider())

    narrative = report["narrative"].split("\n")

    for line in narrative:

        if line.strip():

            story.append(
                Paragraph(line, normal)
            )

    story.append(Spacer(1, 18))

    # ----------------------------------------------------
    # FOOTER
    # ----------------------------------------------------

    story.append(divider())

    story.append(
        Paragraph(
            "<b>Prepared Automatically by Enterprise Sales Analytics Platform</b>",
            normal,
        )
    )

    story.append(
        Paragraph(
            "MICT E-LEARNING SERVICES LIMITED",
            normal,
        )
    )

    story.append(
        Paragraph(
            "<font color='#777777'>Confidential • Internal Management Report</font>",
            normal,
        )
    )

    doc.build(story)