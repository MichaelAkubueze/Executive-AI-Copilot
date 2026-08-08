import streamlit as st

from database import load_sales_data

from components.header import render_header
from components.sidebar import render_sidebar
from components.kpi_cards import render_kpis
from components.gauges_panel import render_gauges
from components.recommendation_panel import render_recommendations
from components.charts_panel import render_charts
from components.footer import render_footer


st.set_page_config(

    page_title="Enterprise Sales Analytics",

    page_icon="📊",

    layout="wide"

)

sales_df = load_sales_data()

sales_df = render_sidebar(sales_df)

render_header()

render_kpis(sales_df)

render_gauges(sales_df)

render_recommendations(sales_df)

render_charts(sales_df)

render_footer()