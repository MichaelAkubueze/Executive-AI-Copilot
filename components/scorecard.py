import streamlit as st


def score_row(title, actual, target):

    pct = 0

    if target > 0:
        pct = min(actual / target * 100, 100)

    if pct >= 80:
        colour = "#10B981"

    elif pct >= 60:
        colour = "#F59E0B"

    else:
        colour = "#EF4444"

    st.markdown(
        f"""
<div style="margin-bottom:18px;">

<div style="
display:flex;
justify-content:space-between;
font-weight:600;
font-size:15px;
">

<span>{title}</span>

<span>{pct:.0f}%</span>

</div>

<div style="
background:#E5E7EB;
height:10px;
border-radius:12px;
overflow:hidden;
margin-top:6px;
">

<div style="
width:{pct:.0f}%;
background:{colour};
height:10px;
">
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def render_scorecard(df):

    st.markdown("### 🎯 Executive Performance")

    score_row("Revenue", 74, 100)

    score_row("Profit", 81, 100)

    score_row("Orders", 96, 100)

    score_row("Customers", 68, 100)

    score_row("Gross Margin", 87, 100)
    
    