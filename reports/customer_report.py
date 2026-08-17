from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
)

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

from reports.report_styles import (
    TITLE_STYLE,
    HEADING_STYLE,
    BODY_STYLE,
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
# FOOTER
# ==========================================================

def add_footer(canvas, doc):

    canvas.saveState()

    width, height = doc.pagesize

    # ------------------------------------------------------
    # Footer line
    # ------------------------------------------------------

    canvas.setStrokeColor(
        colors.HexColor("#1F4E79")
    )

    canvas.setLineWidth(0.7)

    canvas.line(
        40,
        35,
        width - 40,
        35,
    )

    # ------------------------------------------------------
    # Footer text
    # ------------------------------------------------------

    canvas.setFont(
        "Helvetica",
        8,
    )

    canvas.setFillColor(
        colors.HexColor("#64748B")
    )

    canvas.drawString(
        40,
        22,
        "Enterprise Customer Analytics Platform",
    )

    canvas.drawCentredString(
        width / 2,
        22,
        "CONFIDENTIAL",
    )

    canvas.drawRightString(
        width - 40,
        22,
        f"Page {doc.page}",
    )

    canvas.restoreState()


# ==========================================================
# CUSTOMER EXECUTIVE PDF REPORT
# ==========================================================

def create_customer_report(
    insight,
    df,
):

    filename = (
        "Enterprise_Customer_Report.pdf"
    )

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=50,
        title="Enterprise Customer Executive Board Report",
        author="MICT E-LEARNING SERVICES LTD",
    )

    story = []


    # ======================================================
    # COMPANY LOGO
    # ======================================================

    if LOGO_PATH.exists():

        logo = Image(
            str(LOGO_PATH),
            width=110,
            height=110,
            kind="proportional",
        )

        logo.hAlign = "CENTER"

        story.append(
            logo
        )

        story.append(
            Spacer(1, 15)
        )


    # ======================================================
    # REPORT TITLE
    # ======================================================

    story.append(
        Paragraph(
            "MICT E-LEARNING SERVICES LTD",
            TITLE_STYLE,
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Enterprise Customer Analytics Platform",
            HEADING_STYLE,
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "<b>CUSTOMER EXECUTIVE BOARD REPORT</b>",
            HEADING_STYLE,
        )
    )

    story.append(
        Spacer(1, 15)
    )


    # ======================================================
    # REPORT DATE
    # ======================================================

    story.append(
        Paragraph(
            f"Generated: "
            f"{report_date()} "
            f"{report_time()}",
            BODY_STYLE,
        )
    )

    story.append(
        Spacer(1, 20)
    )


    # ======================================================
    # EXECUTIVE CUSTOMER OVERVIEW
    # ======================================================

    story.append(
        Paragraph(
            "Executive Customer Overview",
            HEADING_STYLE,
        )
    )

    story.append(
        Spacer(1, 10)
    )

    overview = f"""
    <b>Total Customers:</b> {insight['Customers']:,}<br/>
    <b>Customer Revenue:</b> ₦{insight['Revenue']:,.2f}<br/>
    <b>Customer Profit:</b> ₦{insight['Profit']:,.2f}<br/>
    <b>Profit Margin:</b> {insight['Margin']:.2f}%<br/>
    <b>Repeat Customer Rate:</b> {insight['Repeat Rate']:.2f}%<br/>
    <b>Best Region:</b> {insight['Best Region']}<br/>
    <b>Top Customer:</b> {insight['Top Customer']}<br/>
    <b>Top Customer Revenue:</b> ₦{insight['Top Customer Revenue']:,.2f}<br/>
    <b>Top Profit Customer:</b> {insight['Top Profit Customer']}<br/>
    <b>Top 10 Revenue Concentration:</b> {insight['Concentration']:.2f}%
    """

    story.append(
        Paragraph(
            overview,
            BODY_STYLE,
        )
    )

    story.append(
        Spacer(1, 20)
    )


    # ======================================================
    # CUSTOMER RECOMMENDATIONS
    # ======================================================

    story.append(
        Paragraph(
            "Customer Recommendations",
            HEADING_STYLE,
        )
    )

    story.append(
        Spacer(1, 10)
    )

    for recommendation in insight.get(
        "Recommendations",
        [],
    ):

        story.append(
            Paragraph(
                f"• {recommendation}",
                BODY_STYLE,
            )
        )

        story.append(
            Spacer(1, 6)
        )

    story.append(
        Spacer(1, 15)
    )


    # ======================================================
    # REPORT CONCLUSION
    # ======================================================

    story.append(
        Paragraph(
            "Management Conclusion",
            HEADING_STYLE,
        )
    )

    story.append(
        Spacer(1, 10)
    )

    conclusion = f"""
    Customer performance generated
    ₦{insight['Revenue']:,.2f}
    in revenue with a profit margin of
    {insight['Margin']:.2f}%.
    The {insight['Best Region']} region represents
    the strongest revenue contribution, while
    {insight['Top Customer']} is the highest-value
    customer in the current analysis.

    Management should focus on customer retention,
    protection of high-value relationships, revenue
    diversification, and opportunities to increase
    repeat purchases.
    """

    story.append(
        Paragraph(
            conclusion,
            BODY_STYLE,
        )
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

