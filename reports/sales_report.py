from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from pathlib import Path

from reportlab.platypus import Image

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
)

from charts import (
    monthly_revenue_chart,
    sales_by_region,
    sales_by_category,
    top_products,
    top_salespersons,
)
from reportlab.platypus import Image

from reportlab.lib import colors
from reportlab.pdfgen import canvas

from reports.report_styles import (
    TITLE_STYLE,
    HEADING_STYLE,
    BODY_STYLE,
)

from reports.report_tables import executive_kpi_table

from reports.report_utils import (
    report_date,
    report_time,
)

def add_footer(canvas, doc):

    canvas.saveState()

    width, height = doc.pagesize

    # Footer line
    canvas.setStrokeColor(colors.HexColor("#1F4E79"))
    canvas.setLineWidth(0.7)

    canvas.line(
        40,
        35,
        width - 40,
        35
    )

    # Left footer
    canvas.setFont(
        "Helvetica",
        8
    )

    canvas.setFillColor(
        colors.HexColor("#64748B")
    )

    canvas.drawString(
        40,
        22,
        "Enterprise Sales Analytics Platform"
    )

    # Center footer
    canvas.drawCentredString(
        width / 2,
        22,
        "CONFIDENTIAL"
    )

    # Right footer
    canvas.drawRightString(
        width - 40,
        22,
        f"Page {doc.page}"
    )

    canvas.restoreState()


from pathlib import Path


def save_chart(fig, filename):

    project_root = Path(__file__).resolve().parent.parent

    chart_dir = project_root / "reports" / "generated_charts"

    chart_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    chart_path = chart_dir / filename

    fig.write_image(
    str(chart_path),
    width=900,
    height=450,
    scale=1
    )

    return chart_path

def management_action_table(insight):

    recommendations = insight.get(
        "Recommendations",
        []
    )

    rows = [
        [
            "Priority",
            "Management Area",
            "Recommended Action",
        ]
    ]

    for recommendation in recommendations:

        if "margin" in recommendation.lower():
            priority = "High"
            area = "Profitability"

        elif "marketing" in recommendation.lower():
            priority = "High"
            area = "Regional Growth"

        elif "inventory" in recommendation.lower():
            priority = "High"
            area = "Inventory"

        elif "salesperson" in recommendation.lower():
            priority = "Medium"
            area = "Sales Performance"

        elif "customer" in recommendation.lower():
            priority = "Medium"
            area = "Customer Management"

        else:
            priority = "Medium"
            area = "Business Performance"

        rows.append(
            [
                priority,
                area,
                recommendation,
            ]
        )

    table = Table(
        rows,
        colWidths=[
            65,
            110,
            325,
        ],
        repeatRows=1,
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#1F4E79"),
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#CBD5E1"),
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor("#F8FAFC"),
                    ],
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
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


#def create_sales_report(insight):
# because the charts need dataframe

def create_sales_report(insight, df):

    filename = "Enterprise_Sales_Report.pdf"

    doc = SimpleDocTemplate(filename)

    story = []
    
    # -------------------------------------------------
# Company Logo
# -------------------------------------------------

    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    LOGO_PATH = PROJECT_ROOT / "assets" / "company_logo.png"

    logo = Image(
    str(LOGO_PATH),
    width=120,
    height=120,
)

    logo.hAlign = "CENTER"

    story.append(logo)

    story.append(Spacer(1,20))

    # -------------------------------------------------
    # Cover Page
    # -------------------------------------------------

    story.append(
        Paragraph(
            "MICT E-LEARNING SERVICES LTD",
            TITLE_STYLE,
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            "Enterprise Sales Analytics Platform",
            HEADING_STYLE,
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            "<b>EXECUTIVE BOARD REPORT</b>",
            HEADING_STYLE,
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Generated: {report_date()}  {report_time()}",
            BODY_STYLE,
        )
    )

    story.append(Spacer(1, 30))

    # -------------------------------------------------
    # KPI Summary
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Executive KPI Summary",
            HEADING_STYLE,
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        executive_kpi_table(insight)
    )

    story.append(Spacer(1, 25))

    # -------------------------------------------------
    # Executive Narrative
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Executive Narrative",
            HEADING_STYLE,
        )
    )

    story.append(Spacer(1, 8))

    narrative = f"""
    The organization generated revenue of
    <b>₦{insight['Revenue']:,.2f}</b>
    while earning a profit of
    <b>₦{insight['Profit']:,.2f}</b>.

    Overall profit margin stands at
    <b>{insight['Margin']:.2f}%</b>.

    The <b>{insight['Best Region']}</b> region delivered the
    highest revenue while
    <b>{insight['Best Category']}</b>
    remains the strongest performing category.

    <b>{insight['Top Salesperson']}</b>
    was the leading salesperson during the reporting period.
    """

    story.append(
        Paragraph(
            narrative,
            BODY_STYLE,
        )
    )

    story.append(Spacer(1, 20))
    
    # -------------------------------------------------
# Revenue Trend
# -------------------------------------------------

    story.append(
    Paragraph(
        "Revenue Performance",
        HEADING_STYLE,
    )
)

    story.append(Spacer(1, 10))

    revenue_fig = monthly_revenue_chart(df)

    revenue_chart = save_chart(
    revenue_fig,
    "sales_revenue_trend.png"
)

    story.append(
    Image(
        str(revenue_chart),
        width=500,
        height=250,
    )
)

    story.append(Spacer(1, 20))
    
    # -------------------------------------------------
# Regional Performance
# -------------------------------------------------

    story.append(
    Paragraph(
        "Regional Sales Performance",
        HEADING_STYLE,
    )
)

    story.append(Spacer(1, 10))

    region_fig = sales_by_region(df)

    region_chart = save_chart(
    region_fig,
    "sales_by_region.png"
)

    story.append(
    Image(
        str(region_chart),
        width=500,
        height=250,
    )
)

    story.append(Spacer(1, 20))
    
    # -------------------------------------------------
# Category Performance
# -------------------------------------------------

    story.append(
    Paragraph(
        "Category Sales Performance",
        HEADING_STYLE,
    )
)

    story.append(Spacer(1, 10))

    category_fig = sales_by_category(df)

    category_chart = save_chart(
    category_fig,
    "sales_by_category.png"
)

    story.append(
    Image(
        str(category_chart),
        width=500,
        height=250,
    )
)

    story.append(Spacer(1, 20))
    
    # -------------------------------------------------
# Top Products
# -------------------------------------------------

    story.append(
    Paragraph(
        "Top Product Performance",
        HEADING_STYLE,
    )
)

    story.append(Spacer(1, 10))

    product_fig = top_products(df)

    product_chart = save_chart(
    product_fig,
    "sales_top_products.png"
)

    story.append(
    Image(
        str(product_chart),
        width=500,
        height=250,
    )
)

    story.append(Spacer(1, 20))
    
    # -------------------------------------------------
# Salesperson Performance
# -------------------------------------------------

    story.append(
    Paragraph(
        "Salesperson Performance",
        HEADING_STYLE,
    )
)

    story.append(Spacer(1, 10))

    salesperson_fig = top_salespersons(df)

    salesperson_chart = save_chart(
    salesperson_fig,
    "sales_top_salespersons.png"
)

    story.append(
    Image(
        str(salesperson_chart),
        width=500,
        height=250,
    )
)

    story.append(Spacer(1, 20))


    # -------------------------------------------------
    # Recommendations
    # -------------------------------------------------

    story.append(
        Paragraph(
            "Executive Recommendations",
            HEADING_STYLE,
        )
    )

    story.append(Spacer(1, 10))

    for rec in insight["Recommendations"]:
        story.append(
            Paragraph(rec, BODY_STYLE)
        )
        
        
# -------------------------------------------------
# Management Action Plan
# -------------------------------------------------

    story.append(
    Paragraph(
        "Management Action Plan",
        HEADING_STYLE,
    )
)

    story.append(Spacer(1, 10))

    story.append(
    management_action_table(insight)
)

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Build PDF
    # -------------------------------------------------

    doc.build(
    story,
    onFirstPage=add_footer,
    onLaterPages=add_footer,
)

    return filename