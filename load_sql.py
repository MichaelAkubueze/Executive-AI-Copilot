import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import time

FILE = r"data\EnterpriseSales.xlsm"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=DESKTOP-A0I0PG7\\SQLEXPRESS;"
    "DATABASE=EnterpriseSalesDB;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=%s"
    % quote_plus(connection_string)
)

try:
    start = time.time()

    print("=" * 60)
    print("READING EXCEL FILE...")
    print("=" * 60)

    sales_df = pd.read_excel(FILE, sheet_name="10_Data")

    print(f"Rows Read: {len(sales_df):,}")
    print(f"Columns : {len(sales_df.columns)}")

    print("\nLOADING DATA INTO SQL SERVER...")

    sales_df.to_sql(
        "FactSales",
        con=engine,
        if_exists="replace",
        index=False
    )

    end = time.time()

    print("\n" + "=" * 60)
    print("SUCCESS!")
    print("=" * 60)
    print(f"Table Name : FactSales")
    print(f"Rows Loaded: {len(sales_df):,}")
    print(f"Time Taken : {end-start:.2f} seconds")

except Exception as e:
    print("\nERROR:")
    print(e)