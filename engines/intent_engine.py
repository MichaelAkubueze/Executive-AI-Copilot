def detect_intent(question):

    q = question.lower()

    # -------------------------------
    # Revenue
    # -------------------------------

    if any(word in q for word in [
        "revenue",
        "sales",
        "income",
        "turnover",
        "sell",
    ]):
        return "revenue"

    # -------------------------------
    # Profit
    # -------------------------------

    if any(word in q for word in [
        "profit",
        "earnings",
        "gain",
    ]):
        return "profit"

    # -------------------------------
    # Orders
    # -------------------------------

    if any(word in q for word in [
        "orders",
        "transactions",
    ]):
        return "orders"

    # -------------------------------
    # Customers
    # -------------------------------

    if any(word in q for word in [
        "customers",
        "clients",
    ]):
        return "customers"

    # -------------------------------
    # Gross Margin
    # -------------------------------

    if "margin" in q:
        return "margin"

    # -------------------------------
    # Best Region
    # -------------------------------

    if "region" in q and any(word in q for word in [
        "best",
        "highest",
        "top",
        "perform",
    ]):
        return "best_region"

    # -------------------------------
    # Worst Region
    # -------------------------------

    if "region" in q and any(word in q for word in [
        "worst",
        "lowest",
        "weakest",
    ]):
        return "worst_region"

    # -------------------------------
    # Best Category
    # -------------------------------

    if "category" in q and any(word in q for word in [
        "best",
        "highest",
        "top",
    ]):
        return "best_category"

    # -------------------------------
    # Recommendation
    # -------------------------------

    if any(word in q for word in [
        "recommend",
        "recommendation",
        "advice",
        "suggest",
    ]):
        return "recommendation"

    return "unknown"