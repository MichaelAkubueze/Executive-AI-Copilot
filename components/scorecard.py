import streamlit as st

from analytics import *

from targets import *

from utils.currency import format_currency

from utils.numbers import format_number

from components.scorecard_row import scorecard_row


def render_scorecard(df):

    st.markdown("## 🎯 Executive Performance Scorecard")

    metrics=[

        (

            "Revenue",

            get_total_revenue(df),

            get_target("Revenue"),

            get_mom_growth(df)

        ),

        (

            "Profit",

            get_total_profit(df),

            get_target("Profit"),

            get_yoy_growth(df)

        ),

        (

            "Orders",

            get_total_orders(df),

            get_target("Orders"),

            order_growth(df)

        ),

        (

            "Customers",

            get_total_customers(df),

            get_target("Customers"),

            customer_growth(df)

        ),

    ]

    for name,actual,target,growth in metrics:

        scorecard_row(

            metric=name,

            actual=format_currency(actual) if "Revenue" in name or "Profit" in name else format_number(actual),

            target=format_currency(target) if "Revenue" in name or "Profit" in name else format_number(target),

            variance=format_currency(variance(actual,target)) if "Revenue" in name or "Profit" in name else format_number(variance(actual,target)),

            achievement=achievement(actual,target),

            status=status(actual,target),

            trend=f"{growth*100:.2f}%"

        )
        