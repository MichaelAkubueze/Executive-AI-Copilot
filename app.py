# ==========================================================
# app.py
# Enterprise Sales Analytics Engine
# ==========================================================

from kpi import *

print("=" * 65)
print("ENTERPRISE SALES KPI ENGINE")
print("=" * 65)

print(f"Revenue             : ₦{get_total_revenue():,.2f}")

print(f"Profit              : ₦{get_total_profit():,.2f}")

print(f"Orders              : {get_total_orders():,}")

print(f"Customers           : {get_total_customers():,}")

print(f"Average Order Value : ₦{get_average_order():,.2f}")

print(f"Gross Margin        : {get_gross_margin():.2%}")

print("=" * 65)

print("\nTesting Monthly Revenue Query...\n")

monthly = get_monthly_revenue()

print(monthly.head())

print("\nTesting Sales by Region...\n")

print(get_sales_by_region())

print("\nTesting Sales by Category...\n")

print(get_sales_by_category())

print("\nTesting Sales by Channel...\n")

print(get_sales_by_channel())

print("\nTesting Customer Segments...\n")

print(get_customer_segments())

print("\n")
print("=" * 65)
print("ALL KPI FUNCTIONS EXECUTED SUCCESSFULLY")
print("=" * 65)