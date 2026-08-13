"""
==========================================================
Executive AI Configuration

Central configuration values for Executive AI.
Changing values here affects the entire application.

Version : 6.0 RC1
==========================================================
"""

# ==========================================================
# COMPANY TARGETS
# ==========================================================

DEFAULT_REVENUE_TARGET = 100_000_000
DEFAULT_PROFIT_TARGET = 25_000_000
DEFAULT_ORDER_TARGET = 12_000
DEFAULT_CUSTOMER_TARGET = 1_200

# ==========================================================
# BUSINESS HEALTH
# ==========================================================

EXCELLENT_THRESHOLD = 100
HEALTHY_THRESHOLD = 85
WATCH_THRESHOLD = 60

# ==========================================================
# PROFITABILITY
# ==========================================================

HIGH_MARGIN = 25
MEDIUM_MARGIN = 15


# ==========================================================
# GROWTH FACTOR
# ==========================================================

REGION_GROWTH_FACTOR = 0.20
CATEGORY_GROWTH_FACTOR = 0.15

# ==========================================================
# CONFIDENCE
# ==========================================================

CONFIDENCE_EXCELLENT = 98
CONFIDENCE_HEALTHY = 96
CONFIDENCE_WATCH = 93
CONFIDENCE_CRITICAL = 90

CONFIDENCE_REGION = 95
CONFIDENCE_CATEGORY = 94
CONFIDENCE_MARGIN = 95

CONFIDENCE_CUSTOMERS = 95
CONFIDENCE_ORDERS = 95
CONFIDENCE_BRIEFING = 98
CONFIDENCE_OPPORTUNITY = 95
CONFIDENCE_RISK = 94
CONFIDENCE_RECOMMENDATION = 96

CONFIDENCE_PROFIT = 97
CONFIDENCE_CUSTOMERS = 95
CONFIDENCE_ORDERS = 95
CONFIDENCE_BUSINESS = 98
CONFIDENCE_BRIEFING = 98
CONFIDENCE_REGION = 95
CONFIDENCE_CATEGORY = 94
CONFIDENCE_OPPORTUNITY = 95
CONFIDENCE_RISK = 94
CONFIDENCE_RECOMMENDATION = 96

# ==========================================================
# STATUS
# ==========================================================

STATUS_EXCELLENT = "Excellent"
STATUS_HEALTHY = "Healthy"
STATUS_WATCH = "Watch"
STATUS_CRITICAL = "Critical"

# ==========================================================
# RISK
# ==========================================================

RISK_LOW = "🟢 Low Risk"
RISK_MODERATE = "🟡 Moderate Risk"
RISK_HIGH = "🟠 High Risk"
RISK_CRITICAL = "🔴 Critical Risk"

# ==========================================================
# EXECUTIVE PRIORITIES
# ==========================================================

PRIORITY_MAINTAIN = "Maintain Leadership"

PRIORITY_GROWTH = "Accelerate Growth"

PRIORITY_REVENUE = "Increase Revenue Performance"

PRIORITY_INTERVENTION = "Immediate Executive Intervention"

# ==========================================================
# BOARDROOM TAKEAWAYS
# ==========================================================

BOARDROOM_EXCELLENT = (
    "Continue scaling successful commercial strategies while "
    "exploring new markets."
)

BOARDROOM_HEALTHY = (
    "Performance remains healthy. Focus on accelerating growth "
    "to exceed annual targets."
)

BOARDROOM_WATCH = (
    "Revenue performance requires closer executive monitoring "
    "to avoid missing strategic objectives."
)

BOARDROOM_CRITICAL = (
    "Immediate executive intervention is required to restore "
    "commercial performance."
)

# ==========================================================
# STANDARD EXECUTIVE ACTIONS
# ==========================================================

ACTION_REVENUE = (
    "Increase marketing investment, strengthen sales execution, "
    "and focus on high-performing regions."
)

ACTION_PROFIT = (
    "Maintain cost discipline while expanding revenue from "
    "high-performing products and regions."
)

ACTION_MARGIN = (
    "Review pricing strategy, procurement costs, "
    "discounting and product mix."
)

ACTION_CUSTOMERS = (
    "Increase customer acquisition while strengthening "
    "customer retention programmes."
)

ACTION_ORDERS = (
    "Improve conversion rates, cross-selling and "
    "repeat purchases."
)

ACTION_BUSINESS = (
    "Continue strengthening weaker KPIs while maintaining "
    "current operational efficiency."
)

ACTION_REGION = (
    "Increase marketing investment, sales resources and "
    "operational support."
)

ACTION_CATEGORY = (
    "Increase inventory allocation and marketing investment."
)

ACTION_RISK = (
    "Address high-risk KPIs immediately, monitor medium-risk "
    "indicators weekly and review strategic performance monthly."
)

ACTION_OPPORTUNITY = (
    "Increase executive attention, marketing investment, "
    "inventory allocation and sales coverage."
)

# ==========================================================
# STANDARD EXECUTIVE INSIGHTS
# ==========================================================

INSIGHT_REGION = (
    "This region currently generates the strongest commercial performance."
)

INSIGHT_CATEGORY = (
    "Demand remains consistently strong for this product category."
)

INSIGHT_OPPORTUNITY = (
    "These business areas currently provide the highest potential "
    "return on additional investment."
)

INSIGHT_RISK = (
    "The above indicators represent the highest operational risks "
    "currently affecting business performance."
)


# ==========================================================
# DEFAULT NARRATIVE
# ==========================================================

DEFAULT_BOARDROOM_TAKEAWAY = (
    "Management should continue monitoring performance "
    "while focusing on strategic growth opportunities."
)

# ==========================================================
# AI DISCLOSURE
# ==========================================================

AI_DISCLOSURE = (
    "This recommendation is generated using the organisation's "
    "current revenue, profitability, customer performance, "
    "order volume and operational KPIs."
)