import streamlit as st


def load_theme():

    st.markdown(
        """
        <style>

        .stApp{

            background:#F5F7FB;

        }

        div[data-testid="stMetric"]{

            background:white;

            border-radius:18px;

            padding:15px;

            box-shadow:0px 4px 12px rgba(0,0,0,.06);

        }

        h1,h2,h3{

            color:#111827;

            font-weight:700;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )