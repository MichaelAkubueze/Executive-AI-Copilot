import re


# ==========================================================
# QUESTION NORMALIZER
# ==========================================================

def normalize_question(question):

    question = question.lower().strip()

    question = re.sub(r"[^\w\s]", "", question)

    return question


# ==========================================================
# INTENT DETECTOR
# ==========================================================

def detect_intent(question):

    q = normalize_question(question)

    intents = {

        "revenue": [
            "revenue",
            "sales",
            "total revenue",
            "total sales",
            "sales generated",
            "revenue generated",
            "how much revenue",
            "how much sales",
        ],

        "profit": [
            "profit",
            "total profit",
            "earnings",
            "income",
            "gross profit",
        ],

        "margin": [
            "margin",
            "gross margin",
            "profit margin",
        ],

        "orders": [
            "orders",
            "order",
            "transactions",
            "sales orders",
        ],

        "customers": [
            "customers",
            "customer",
            "clients",
            "buyers",
        ],

        "region": [
            "region",
            "best region",
            "top region",
            "highest region",
        ],

        "category": [
            "category",
            "product category",
            "best category",
            "top category",
            "products",
        ],

    }

    for intent, keywords in intents.items():

        for keyword in keywords:

            if keyword in q:

                return intent

    return "unknown"