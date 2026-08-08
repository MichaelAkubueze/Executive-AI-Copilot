import pandas as pd

excel = pd.ExcelFile("data/EnterpriseSales.xlsm")

print("=" * 80)
print("WORKSHEETS")
print("=" * 80)

for sheet in excel.sheet_names:

    print(f"\nSheet: {sheet}")

    df = pd.read_excel(excel, sheet_name=sheet)

    print(df.head())

    print("\nColumns:")

    print(df.columns.tolist())

    print("-" * 80)