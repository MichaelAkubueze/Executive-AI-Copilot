"""
==========================================================
Executive AI Narrative Engine

Purpose:
    Converts business analysis into executive-ready
    narratives for the Executive Copilot.

Version:
    6.0 RC1
==========================================================
"""

# ==========================================================
# EXECUTIVE AI NARRATIVE
# Used by Executive Copilot
# ==========================================================

from typing import Optional
from ai_config import (
    DEFAULT_BOARDROOM_TAKEAWAY,
    AI_DISCLOSURE,
)
from engines.constants import STATUS_ICONS

def executive_narrative(
    title: str,
    metric: str,
    achievement: float,
    insight: str,
    impact: str,
    risk: str,
    priority: str,
    recommendation: str,
    boardroom_takeaway: Optional[str],
    status: str,
    confidence: int,
) -> str:
    
    """
Build a standardized executive narrative.

Parameters
----------
title
metric
achievement
insight
impact
risk
priority
recommendation
boardroom_takeaway
status
confidence

Returns
-------
str
    Formatted executive report.
"""
    


    icon = STATUS_ICONS.get(status, "🟠")

    boardroom_takeaway = (
    boardroom_takeaway or DEFAULT_BOARDROOM_TAKEAWAY
)
    return f"""
# {title}

---

## 📌 Executive Answer

{metric}

---

## 📊 Business Context

### Target Achievement

**{achievement:.1f}%**

### Current Status

{icon} **{status}**

---

## 🧠 Executive Interpretation

{insight}

---

## 💼 Business Impact

{impact}

---

## ⚠️ Risk Level

**{risk}**

---

## 🎯 Executive Priority

**{priority}**

---

## 🚀 Recommended Executive Actions

{recommendation}

---

## 🏛️ Boardroom Takeaway

{boardroom_takeaway}

---

## 📈 Confidence Level

**{confidence}%**

{AI_DISCLOSURE}

"""


# ==========================================================
# BOARD REPORT NARRATIVE
# Used by PDF Executive Board Report
# ==========================================================

def generate_narrative(df):

    from analytics import (
        get_total_revenue,
        get_total_profit,
        get_gross_margin,
        get_total_orders,
        get_total_customers,
    )

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    margin = get_gross_margin(df)
    orders = get_total_orders(df)
    customers = get_total_customers(df)

    return f"""
# Executive Business Summary

## Financial Performance

• Revenue: ₦{revenue:,.2f}

• Profit: ₦{profit:,.2f}

• Gross Margin: {margin:.2f}%

---

## Operational Performance

• Orders Processed: {orders:,}

• Customers Served: {customers:,}

---

## Executive Summary

The organisation continues to operate based on the current financial
and operational KPI indicators.

Management should continue focusing on:

• Revenue growth

• Profitability

• Customer acquisition

• Operational efficiency

while closely monitoring overall business performance.
"""