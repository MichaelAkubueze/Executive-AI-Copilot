from nlp_engine import detect_intent

questions = [

    "Revenue",
    "Sales",
    "Current Sales",
    "How much revenue did we make?",
    "Total Revenue",
    "Profit",
    "Total Profit",
    "Income",
    "Gross Margin",
    "Profit Margin",
    "Customers",
    "Clients",
    "Buyers",
    "Orders",
    "Transactions",
    "Best Region",
    "Top Region",
    "Highest Region",
    "Best Category",
    "Products",
    "What is our revenue?",
    "How many customers do we have?",
    "Show me the best region",
    "Show me top category",
    "Unknown Question"

]

print("=" * 70)
print("NATURAL LANGUAGE ENGINE TEST")
print("=" * 70)

for q in questions:

    print(f"{q:<40} -> {detect_intent(q)}")