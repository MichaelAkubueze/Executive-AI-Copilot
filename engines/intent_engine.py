def detect_intent(question):

    q = question.lower().strip()

    # ==========================================================
    # REVENUE
    # ==========================================================

    revenue_words = [
        "revenue",
        "sales",
        "income",
        "turnover",
        "sell",
        "money",
        "cash",
        "generated",
        "made",
        "earning",
    ]

    if any(word in q for word in revenue_words):
        return "revenue"

    # ==========================================================
    # PROFIT
    # ==========================================================

    profit_words = [
        "profit",
        "profits",
        "earnings",
        "gain",
        "gains",
        "net income",
        "bottom line",
        "profitable",
    ]

    if any(word in q for word in profit_words):
        return "profit"

    # ==========================================================
    # GROSS MARGIN
    # ==========================================================

    margin_words = [
        "margin",
        "gross margin",
        "profit margin",
    ]

    if any(word in q for word in margin_words):
        return "margin"

    # ==========================================================
    # ORDERS
    # ==========================================================

    order_words = [
        "orders",
        "order",
        "transactions",
        "transaction",
        "sales orders",
    ]

    if any(word in q for word in order_words):
        return "orders"

    # ==========================================================
    # CUSTOMERS
    # ==========================================================

    customer_words = [
        "customer",
        "customers",
        "client",
        "clients",
        "buyers",
    ]

    if any(word in q for word in customer_words):
        return "customers"

    # ==========================================================
    # BUSINESS HEALTH
    # ==========================================================

    health_words = [
        "health",
        "healthy",
        "business health",
        "company health",
        "overall performance",
        "performance",
    ]

    if any(word in q for word in health_words):
        return "business_health"

    # ==========================================================
    # EXECUTIVE BRIEFING
    # ==========================================================

    briefing_words = [
        "brief",
        "briefing",
        "summary",
        "summarize",
        "executive summary",
        "executive briefing",
        "board summary",
        "overview",
    ]

    if any(word in q for word in briefing_words):
        return "executive_briefing"

    # ==========================================================
    # RISK
    # ==========================================================

    risk_words = [
        "risk",
        "risks",
        "danger",
        "threat",
        "problem",
        "problems",
        "issue",
        "issues",
        "alert",
        "alerts",
    ]

    if any(word in q for word in risk_words):
        return "risk"

    # ==========================================================
    # OPPORTUNITY
    # ==========================================================

    opportunity_words = [
        "opportunity",
        "opportunities",
        "invest",
        "investment",
        "grow",
        "growth opportunity",
        "expand",
    ]

    if any(word in q for word in opportunity_words):
        return "opportunity"

    # ==========================================================
    # BEST REGION
    # ==========================================================

    if (
        "region" in q
        and any(
            word in q
            for word in [
                "best",
                "highest",
                "top",
                "perform",
                "strongest",
            ]
        )
    ):
        return "best_region"

    # ==========================================================
    # WORST REGION
    # ==========================================================

    if (
        "region" in q
        and any(
            word in q
            for word in [
                "worst",
                "lowest",
                "weakest",
                "poor",
            ]
        )
    ):
        return "worst_region"

    # ==========================================================
    # BEST CATEGORY
    # ==========================================================

    if (
        "category" in q
        and any(
            word in q
            for word in [
                "best",
                "highest",
                "top",
                "strongest",
            ]
        )
    ):
        return "best_category"

    # ==========================================================
    # RECOMMENDATION
    # ==========================================================

    recommendation_words = [
        "recommend",
        "recommendation",
        "advice",
        "suggest",
        "improve",
        "increase",
        "reduce",
        "optimize",
        "what should",
        "next step",
        "ceo",
        "management",
    ]

    if any(word in q for word in recommendation_words):
        return "recommendation"

    return "unknown"