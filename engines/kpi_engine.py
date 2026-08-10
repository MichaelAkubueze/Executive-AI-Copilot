from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)

from engines.target_engine import get_target


# ==========================================================
# Generic Achievement Calculator
# ==========================================================

def achievement(actual, target):
    """
    Returns percentage achievement.
    Caps value at 100%.
    """

    if target is None or target == 0:
        return 0

    return min((actual / target) * 100, 100)


# ==========================================================
# Revenue
# ==========================================================

def revenue_achievement(df):

    target = get_target("Revenue")

    return achievement(
        get_total_revenue(df),
        target,
    )


# ==========================================================
# Profit
# ==========================================================

def profit_achievement(df):

    target = get_target("Profit")

    return achievement(
        get_total_profit(df),
        target,
    )


# ==========================================================
# Orders
# ==========================================================

def orders_achievement(df):

    target = get_target("Orders")

    return achievement(
        get_total_orders(df),
        target,
    )


# ==========================================================
# Customers
# ==========================================================

def customer_achievement(df):

    target = get_target("Customers")

    return achievement(
        get_total_customers(df),
        target,
    )


# ==========================================================
# Gross Margin
# ==========================================================

def margin_achievement(df):

    target = get_target("Margin")

    return achievement(
        get_gross_margin(df),
        target,
    )


# ==========================================================
# PERFORMANCE STATUS ENGINE
# ==========================================================

def performance_status(percent):
    """
    Returns dashboard badge and colour.
    """

    if percent >= 90:
        return "Excellent", "#10B981"

    elif percent >= 75:
        return "Healthy", "#2563EB"

    elif percent >= 60:
        return "Watch", "#F59E0B"

    else:
        return "Critical", "#EF4444"


# ==========================================================
# TARGET LOOKUP HELPERS
# ==========================================================

def revenue_target():
    return get_target("Revenue")


def profit_target():
    return get_target("Profit")


def orders_target():
    return get_target("Orders")


def customer_target():
    return get_target("Customers")


def margin_target():
    return get_target("Margin")