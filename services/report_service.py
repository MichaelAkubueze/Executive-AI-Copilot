from services.chart_service import (
    revenue_chart,
    profit_chart,
)


from datetime import datetime

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)

from engines.target_engine import get_target
from engines.narrative_engine import generate_narrative

from reports.board_report import build_pdf


# ==========================================================
# EXECUTIVE KPI TABLE
# ==========================================================

def executive_kpi_table(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)

    revenue_target = get_target("Revenue")
    profit_target = get_target("Profit")

    # Default targets (used if target workbook has no values)
    orders_target = 12000
    customers_target = 1200

    return [

        ["KPI", "Actual", "Target", "Achievement"],

        [
            "Revenue",
            f"₦{revenue:,.0f}",
            f"₦{revenue_target:,.0f}",
            f"{(revenue/revenue_target):.1%}" if revenue_target else "N/A",
        ],

        [
            "Profit",
            f"₦{profit:,.0f}",
            f"₦{profit_target:,.0f}",
            f"{(profit/profit_target):.1%}" if profit_target else "N/A",
        ],

        [
            "Orders",
            f"{orders:,}",
            f"{orders_target:,}",
            f"{(orders/orders_target):.1%}",
        ],

        [
            "Customers",
            f"{customers:,}",
            f"{customers_target:,}",
            f"{(customers/customers_target):.1%}",
        ],

    ]


# ==========================================================
# EXECUTIVE REPORT DATA
# ==========================================================

def executive_report(df):

    narrative = generate_narrative(df)

    summary = {

        "Revenue": f"₦{get_total_revenue(df):,.2f}",

        "Profit": f"₦{get_total_profit(df):,.2f}",

        "Orders": f"{get_total_orders(df):,}",

        "Customers": f"{get_total_customers(df):,}",

        "Gross Margin": f"{get_gross_margin(df):.2%}",

        "Generated": datetime.now().strftime("%d %B %Y %I:%M %p"),

    }

    return {

        "summary": summary,

        "narrative": narrative,

    }


# ==========================================================
# EXPORT PDF
# ==========================================================

def export_pdf(df):

    report = executive_report(df)

    kpi_table = executive_kpi_table(df)

    revenue_image = revenue_chart(df)

    profit_image = profit_chart(df)

    filename = "Executive_Board_Report.pdf"

    build_pdf(

        report=report,

        filename=filename,

        kpi_table=kpi_table,

        revenue_chart_path=revenue_image,

        profit_chart_path=profit_image,

    )

    return filename