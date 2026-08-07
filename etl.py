import pandas as pd

FILE = r"data\EnterpriseSales.xlsm"

# Read the main sales sheet
sales_df = pd.read_excel(
    FILE,
    sheet_name="10_Data"
)

print("=" * 60)
print("DATA IMPORTED SUCCESSFULLY")
print("=" * 60)

print(sales_df.head())

print()

print("Rows :", len(sales_df))

print("Columns :", len(sales_df.columns))

print("\nRows:", len(sales_df))
print("Columns:", len(sales_df.columns))
print("\nMissing Values")
print("=" * 60)

print(sales_df.isnull().sum())