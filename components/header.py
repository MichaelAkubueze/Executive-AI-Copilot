import streamlit as st
from datetime import datetime

def render_header():

    now = datetime.now().strftime("%d %B %Y | %I:%M %p")

    st.markdown(
        f"""
<div style="
background:linear-gradient(90deg,#2563EB,#0EA5E9);
padding:24px;
border-radius:16px;
box-shadow:0 8px 20px rgba(0,0,0,.15);
margin-bottom:20px;
color:white;
">

<h1 style="margin:0;color:white;">
📊 Enterprise Sales Analytics Dashboard
</h1>

<h4 style="margin-top:8px;color:#EAF4FF;">
Executive Decision Support System
</h4>

<hr style="border:none;border-top:1px solid rgba(255,255,255,.25);margin:15px 0;">

<div style="font-weight:600;color:white;">
🕒 {now}
</div>

</div>
""",
        unsafe_allow_html=True,
    )