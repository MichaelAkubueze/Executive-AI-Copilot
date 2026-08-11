import streamlit as st

from engines.executive_engine import business_health


def render_business_health(df):

    health = business_health(df)

    score = health["score"]

    status = health["status"]

    revenue = health["revenue_score"]

    margin = health["margin_score"]

    customers = health["customer_score"]

    orders = health["order_score"]

    # ------------------------------------------------------
    # Score Colour
    # ------------------------------------------------------

    if score >= 90:
        score_color = "#10B981"

    elif score >= 75:
        score_color = "#F59E0B"

    else:
        score_color = "#EF4444"

    st.markdown("## 🏢 Business Health")

    st.markdown(
        f"""
<div style="
background:white;
padding:25px;
border-radius:18px;
box-shadow:0px 3px 12px rgba(0,0,0,0.12);
border-left:8px solid {score_color};
">

<h1 style="
text-align:center;
font-size:48px;
margin-bottom:0px;
color:{score_color};
">
{score:.1f}%
</h1>

<h3 style="
text-align:center;
margin-top:5px;
margin-bottom:25px;
">
{status}
</h3>

<b>Revenue Achievement ({revenue:.1f}%)</b>

<progress
value="{revenue}"
max="100"
style="width:100%;height:18px;">
</progress>

<br><br>

<b>Profit Margin ({margin:.1f}%)</b>

<progress
value="{margin}"
max="100"
style="width:100%;height:18px;">
</progress>

<br><br>

<b>Customer Achievement ({customers:.1f}%)</b>

<progress
value="{customers}"
max="100"
style="width:100%;height:18px;">
</progress>

<br><br>

<b>Order Achievement ({orders:.1f}%)</b>

<progress
value="{orders}"
max="100"
style="width:100%;height:18px;">
</progress>

</div>
""",
        unsafe_allow_html=True,
    )