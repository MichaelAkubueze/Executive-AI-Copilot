import streamlit as st


def render_footer():

    st.divider()

    st.markdown(

        """
        <div style="text-align:center;color:gray;font-size:13px;">

        Enterprise Sales Analytics Dashboard

        <br>

        Developed with Python • Streamlit • SQL Server • Plotly

        </div>

        """,

        unsafe_allow_html=True

    )