from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors


def executive_kpi_table(insight):

    data = [

        ["Metric", "Value"],

        ["Revenue", f"₦{insight['Revenue']:,.2f}"],

        ["Profit", f"₦{insight['Profit']:,.2f}"],

        ["Profit Margin", f"{insight['Margin']:.2f}%"],

        ["Best Region", insight["Best Region"]],

        ["Best Category", insight["Best Category"]],

        ["Top Customer", insight["Top Customer"]],

        ["Top Salesperson", insight["Top Salesperson"]],

    ]

    table = Table(data)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E79")),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

                ("TOPPADDING", (0, 0), (-1, 0), 10),

            ]

        )

    )

    return table