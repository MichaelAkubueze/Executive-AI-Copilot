from database import load_sales_data
from query_engine import QueryEngine

# Load data
df = load_sales_data()

# Create engine
engine = QueryEngine(df)

print("=" * 60)
print("ENTERPRISE QUERY ENGINE TEST")
print("=" * 60)

print(f"Revenue           : ₦{engine.revenue():,.2f}")
print(f"Profit            : ₦{engine.profit():,.2f}")
print(f"Gross Margin      : {engine.margin():.2%}")
print(f"Customers         : {engine.customers():,}")
print(f"Orders            : {engine.orders():,}")

print()

region = engine.best_region()

print("BEST REGION")
print(region)

print()

category = engine.best_category()

print("BEST CATEGORY")
print(category)

print("=" * 60)