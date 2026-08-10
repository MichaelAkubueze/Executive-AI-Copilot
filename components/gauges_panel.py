import streamlit as st


def gauge(title, value, colour):

    st.markdown(
        f"""
<div style="
background:white;
padding:18px;
border-radius:18px;
box-shadow:0 6px 18px rgba(0,0,0,.08);
">

<div style="
font-weight:700;
font-size:16px;
margin-bottom:12px;
">

{title}

</div>

<div style="
background:#E5E7EB;
height:12px;
border-radius:30px;
overflow:hidden;
">

<div style="
width:{value}%;
background:{colour};
height:12px;
">

</div>

</div>

<div style="
margin-top:10px;
font-size:26px;
font-weight:700;
color:{colour};
">

{value:.0f}%

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def render_gauges(df):

    st.subheader("📈 Target Achievement")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        gauge("Revenue", 74, "#2563EB")

    with c2:
        gauge("Profit", 81, "#10B981")

    with c3:
        gauge("Orders", 87, "#F59E0B")

    with c4:
        gauge("Customers", 92, "#8B5CF6")