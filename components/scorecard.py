import streamlit as st

from analytics import (
    get_mom_growth,
    get_yoy_growth,
    customer_growth,
    order_growth,
)


# ----------------------------------------------------------
# Progress Bar
# ----------------------------------------------------------

def progress(label, value):

    pct = max(min(value * 100, 100), 0)

    if pct >= 75:
        colour = "🟢"

    elif pct >= 40:
        colour = "🟡"

    else:
        colour = "🔴"

    st.write(f"**{label}**")

    st.progress(pct / 100)

    st.caption(f"{colour} {pct:.2f}%")

    st.write("")


# ----------------------------------------------------------
# Executive Scorecard
# ----------------------------------------------------------

def render_scorecard(df):

    progress(
        "Revenue Growth",
        get_mom_growth(df),
    )

    progress(
        "Profit Growth",
        get_yoy_growth(df),
    )

    progress(
        "Order Growth",
        order_growth(df),
    )

    progress(
        "Customer Growth",
        customer_growth(df),
    )