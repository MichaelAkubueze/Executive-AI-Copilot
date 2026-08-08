import streamlit as st
import pandas as pd

DATA_PATH = "data/EnterpriseSales.xlsm"

@st.cache_data
def load_sales_data():

    df = pd.read_excel(
        DATA_PATH,
        sheet_name="10_Data"
    )

    return df