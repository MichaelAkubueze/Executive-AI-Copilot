from database import load_sales_data
from analytics import *

df = load_sales_data()

print("MoM:", get_mom_growth(df))
print("YoY:", get_yoy_growth(df))
print("Customer Growth:", customer_growth(df))
print("Order Growth:", order_growth(df))