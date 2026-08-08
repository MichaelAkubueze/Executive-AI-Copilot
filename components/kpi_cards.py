import streamlit as st

from kpi import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_average_order,
    get_gross_margin,
)


def render_kpis(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)
    avg_order = get_average_order(df)
    margin = get_gross_margin(df)

    cards = [

        ("💰 Revenue",
         f"₦{revenue/1_000_000:,.2f}M",
         "Business Growing"),

        ("📈 Profit",
         f"₦{profit/1_000_000:,.2f}M",
         "Positive Trend"),

        ("🛒 Orders",
         f"{orders:,}",
         "Completed Orders"),

        ("👥 Customers",
         f"{customers:,}",
         "Active Customers"),

        ("💳 Avg Order",
         f"₦{avg_order:,.0f}",
         "Average Basket"),

        ("📊 Margin",
         f"{margin:.2%}",
         "Healthy"),

    ]

    st.markdown("""
    <style>

    .metric-card{

        background:white;

        border-radius:15px;

        padding:20px;

        box-shadow:0 3px 18px rgba(0,0,0,.08);

        border-left:6px solid #2563EB;

        transition:.3s;

        text-align:center;

    }

    .metric-card:hover{

        transform:translateY(-4px);

        box-shadow:0 8px 25px rgba(0,0,0,.15);

    }

    .metric-title{

        color:#777;

        font-size:14px;

        margin-bottom:10px;

    }

    .metric-value{

        font-size:28px;

        font-weight:bold;

        color:#2563EB;

    }

    .metric-sub{

        color:#10B981;

        font-size:13px;

    }

    </style>

    """, unsafe_allow_html=True)

    cols = st.columns(6)

    for col, card in zip(cols, cards):

        title, value, note = card

        with col:

            st.markdown(f"""

            <div class="metric-card">

            <div class="metric-title">

            {title}

            </div>

            <div class="metric-value">

            {value}

            </div>

            <div class="metric-sub">

            {note}

            </div>

            </div>

            """, unsafe_allow_html=True)