# ==========================================================
# ENTERPRISE AI INTENT ENGINE
# Version 2.0
# ==========================================================

INTENTS = {

    # ------------------------------------------------------
    # Revenue
    # ------------------------------------------------------

    "revenue": [

        "revenue",
        "sales",
        "sales revenue",
        "turnover",
        "income",
        "earnings",
        "money",
        "amount sold",
        "sales amount",
        "how much did we make",
        "how much money did we make",
        "how much did we sell",
        "total sales",
        "company revenue",

    ],

    # ------------------------------------------------------
    # Profit
    # ------------------------------------------------------

    "profit": [

        "profit",
        "net profit",
        "gross profit",
        "earnings",
        "gain",
        "company profit",
        "profit amount",

    ],

    # ------------------------------------------------------
    # Gross Margin
    # ------------------------------------------------------

    "margin": [

        "margin",
        "gross margin",
        "profit margin",
        "margin percentage",

    ],

    # ------------------------------------------------------
    # Customers
    # ------------------------------------------------------

    "customers": [

        "customers",
        "customer",
        "clients",
        "buyers",
        "accounts",
        "customer count",
        "total customers",

    ],

    # ------------------------------------------------------
    # Orders
    # ------------------------------------------------------

    "orders": [

        "orders",
        "order",
        "transactions",
        "sales orders",
        "purchases",
        "total orders",

    ],

    # ------------------------------------------------------
    # Best Region
    # ------------------------------------------------------

    "best_region": [

        "best region",
        "top region",
        "highest region",
        "leading region",
        "highest sales region",
        "best performing region",
        "top performing region",

    ],

    # ------------------------------------------------------
    # Worst Region
    # ------------------------------------------------------

    "worst_region": [

        "worst region",
        "lowest region",
        "weakest region",
        "lowest sales region",
        "poor region",

    ],

    # ------------------------------------------------------
    # Best Category
    # ------------------------------------------------------

    "best_category": [

        "best category",
        "top category",
        "highest category",
        "best product category",
        "highest selling category",

    ],

    # ------------------------------------------------------
    # Recommendation
    # ------------------------------------------------------

    "recommendation": [

        "recommendation",
        "advice",
        "suggestion",
        "management advice",
        "what should we do",
        "next step",
        "improvement",
        "strategy",

    ],

}


# ==========================================================
# DETECT USER INTENT
# ==========================================================

def detect_intent(question):

    if question is None:
        return None

    q = question.lower().strip()

    best_match = None
    highest_score = 0

    for intent, keywords in INTENTS.items():

        score = 0

        for keyword in keywords:

            if keyword in q:
                score += len(keyword)

        if score > highest_score:

            highest_score = score
            best_match = intent

    return best_match