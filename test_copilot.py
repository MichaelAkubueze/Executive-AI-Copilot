from database import load_sales_data
from copilot import ask_copilot

df = load_sales_data()

questions = [

    "Revenue",
    "Sales",
    "How much revenue?",
    "Profit",
    "Income",
    "Margin",
    "Customers",
    "Clients",
    "Orders",
    "Transactions",
    "Best Region",
    "Top Region",
    "Best Category",
    "Products",
    "Unknown Question"

]

print("=" * 70)
print("AI COPILOT TEST")
print("=" * 70)

for q in questions:

    print()

    print("QUESTION :", q)

    print("ANSWER   :", ask_copilot(q, df))