import streamlit as st
from datetime import datetime


def render_header():

    now = datetime.now().strftime("%d %B %Y  |  %I:%M %p")

    st.markdown("""
    <style>

    .header{

        background:linear-gradient(90deg,#2563EB,#0EA5E9);

        padding:22px;

        border-radius:12px;

        color:white;

        box-shadow:0px 5px 20px rgba(0,0,0,.15);

        margin-bottom:15px;

    }

    .header h1{

        margin:0;

        font-size:34px;

    }

    .header h4{

        margin-top:6px;

        font-weight:400;

        opacity:.9;

    }

    </style>

    """, unsafe_allow_html=True)

    st.markdown(f"""

    <div class="header">

    <h1>📊 Enterprise Sales Analytics Dashboard</h1>

    <h4>Executive Decision Support System</h4>

    <hr>

    <b>{now}</b>

    </div>

    """, unsafe_allow_html=True)