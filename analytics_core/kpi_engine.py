from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
)

# ==========================================================
# TARGETS
# (Temporary - later replaced by tblTargets)
# ==========================================================

REVENUE_TARGET = 100_000_000
PROFIT_TARGET = 30_000_000
ORDER_TARGET = 12_000
CUSTOMER_TARGET = 1_200
MARGIN_TARGET = 0.35


# ==========================================================
# Generic Achievement Calculator
# ==========================================================

def achievement(actual, target):

    if target == 0:
        return 0

    return min((actual / target) * 100, 100)


# ==========================================================
# Revenue
# ==========================================================

def revenue_achievement(df):

    return achievement(
        get_total_revenue(df),
        REVENUE_TARGET,
    )


# ==========================================================
# Profit
# ==========================================================

def profit_achievement(df):

    return achievement(
        get_total_profit(df),
        PROFIT_TARGET,
    )


# ==========================================================
# Orders
# ==========================================================

def orders_achievement(df):

    return achievement(
        get_total_orders(df),
        ORDER_TARGET,
    )


# ==========================================================
# Customers
# ==========================================================

def customer_achievement(df):

    return achievement(
        get_total_customers(df),
        CUSTOMER_TARGET,
    )


# ==========================================================
# Margin
# ==========================================================

def margin_achievement(df):

    return achievement(
        get_gross_margin(df),
        MARGIN_TARGET,
    )


# ==========================================================
# Status Engine
# ==========================================================

def performance_status(percent):

    if percent >= 90:
        return "Excellent", "#10B981"

    if percent >= 75:
        return "Healthy", "#2563EB"

    if percent >= 60:
        return "Watch", "#F59E0B"

    return "Critical", "#EF4444"