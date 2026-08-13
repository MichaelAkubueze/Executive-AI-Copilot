"""
==========================================================
Executive AI Copilot Engine

Routes executive questions to the appropriate
analysis engine and returns executive-ready responses.

Version : 6.0 RC1
==========================================================
"""

# ==========================================================
# Standard Library
# ==========================================================

# (none currently)

# ==========================================================
# Internal Engines
# ==========================================================

from ai_config import (
    
    ACTION_REVENUE,
    ACTION_PROFIT,
    ACTION_MARGIN,
    ACTION_CUSTOMERS,
    ACTION_ORDERS,
    ACTION_BUSINESS,
    ACTION_REGION,
    ACTION_CATEGORY,
    ACTION_RISK,
    ACTION_OPPORTUNITY,

    INSIGHT_REGION,
    INSIGHT_CATEGORY,
    INSIGHT_OPPORTUNITY,
    INSIGHT_RISK,
    HIGH_MARGIN,
    MEDIUM_MARGIN,
    
    CONFIDENCE_PROFIT,
    CONFIDENCE_MARGIN,
    CONFIDENCE_CUSTOMERS,
    CONFIDENCE_ORDERS,
    CONFIDENCE_BUSINESS,
    CONFIDENCE_BRIEFING,
    CONFIDENCE_REGION,
    CONFIDENCE_CATEGORY,
    CONFIDENCE_RISK,
    CONFIDENCE_RECOMMENDATION,
    )


from engines.intent_engine import detect_intent
from engines.narrative_engine import executive_narrative
from engines.reasoning_engine import (
    explain_revenue,
    explain_profit,
    explain_business,
)

from engines.executive_engine import (
    business_health,
    executive_alerts,
    executive_briefing,
)

from engines.opportunity_engine import (
    best_region,
    best_category,
)

from engines.context_engine import (
    remember,
    recall,
)

from engines.advisor import generate_recommendation

# ==========================================================
# Analytics
# ==========================================================

from analytics import (
    get_total_customers,
    get_total_orders,
    get_gross_margin,
)


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def executive_summary(df) -> str:

    health = business_health(df)

    return f"""
## 🤖 Executive AI Decision Intelligence

### Business Health

**{health['status']}**

### Overall Score

**{health['score']:.1f}%**

---

You can ask:

• Revenue
• Profit
• Gross Margin
• Orders
• Customers
• Business Health
• Best Region
• Best Category
• Opportunities
• Risks
• Executive Briefing
• Recommendations
"""


# ==========================================================
# EXECUTIVE QUESTION ENGINE
# ==========================================================

def answer_question(df, question: str) -> str:
    
    """
Routes an executive question to the appropriate
business intelligence engine and returns a
formatted executive response.

Parameters
----------
df : pandas.DataFrame
    Sales dataset.

question : str
    Executive question.

Returns
-------
str
    Executive AI response.
"""

    intent = detect_intent(question)

    # =====================================================
    # REVENUE
    # =====================================================

    if intent == "revenue":

        analysis = explain_revenue(df)

        return executive_narrative(

            title="💰 Executive Revenue Performance",

            metric=f"₦{analysis['metric']:,.2f}",

            achievement=analysis["achievement"],

            insight=analysis["insight"],

            impact=analysis["impact"],

            risk=analysis["risk"],

            priority=analysis["priority"],

            recommendation=analysis["recommendation"],

            boardroom_takeaway=analysis["boardroom_takeaway"],

            status=analysis["status"],

            confidence=analysis["confidence"],
        )

    # =====================================================
    # PROFIT
    # =====================================================

    elif intent == "profit":

        analysis = explain_profit(df)

        profit = analysis["profit"]
        margin = analysis["margin"]
        insight = analysis["insight"]

        if margin >= HIGH_MARGIN:

            opinion = (
                "🟢 The business is highly profitable."
            )

        elif margin >= MEDIUM_MARGIN:

            opinion = (
                "🟠 Profitability is healthy but has room for improvement."
            )

        else:

            opinion = (
                "🔴 Profitability is below the desired strategic level."
            )

        return f"""
# 📈 Executive Profit Performance

---

## Executive Answer

{opinion}

---

## Total Profit

₦{profit:,.2f}

---

## Gross Margin

{margin:.2f}%

---

## Executive Insight

{insight}

---

## Recommended Action

Increase revenue from high-performing regions while maintaining cost discipline.

---

## Confidence

{CONFIDENCE_PROFIT}%
"""

    # =====================================================
    # GROSS MARGIN
    # =====================================================

    elif intent == "margin":

        margin = get_gross_margin(df)

        if margin >= 25:

            interpretation = (
                "Gross margin exceeds the strategic target."
            )

        elif margin >= 15:

            interpretation = (
                "Gross margin is acceptable but can still improve."
            )

        else:

            interpretation = (
                "Gross margin requires immediate executive attention."
            )

        return f"""
# 📊 Gross Margin Performance

---

## Current Gross Margin

{margin:.2f}%

---

## Executive Insight

{interpretation}

---

## Recommended Action

Review pricing strategy, discounting, procurement costs and product mix.

---

## Confidence
{CONFIDENCE_MARGIN}%
"""

    # =====================================================
    # CUSTOMERS
    # =====================================================

    elif intent == "customers":

        customers = get_total_customers(df)

        return f"""
# 👥 Customer Performance

---

## Executive Answer

Current Active Customers

**{customers:,}**

---

## Business Context

Customer acquisition and retention are leading indicators of future revenue growth.

---

## Executive Insight

A growing customer base improves revenue sustainability and market penetration.

---

## Recommended Action

Increase customer acquisition campaigns while strengthening customer retention programmes.

---

## Confidence

{CONFIDENCE_CUSTOMERS}%
"""

    # =====================================================
    # ORDERS
    # =====================================================

    elif intent == "orders":

        orders = get_total_orders(df)

        return f"""
# 🛒 Order Performance

---

## Executive Answer

Orders Processed

**{orders:,}**

---

## Business Context

Order volume reflects sales effectiveness and market demand.

---

## Executive Insight

Consistent order growth supports sustainable revenue expansion.

---

## Recommended Action

Improve conversion rates, cross-selling and repeat purchases.

---

## Confidence

95%
"""

    # =====================================================
    # BUSINESS HEALTH
    # =====================================================

    elif intent == "business_health":

        analysis = explain_business(df)

        health = analysis["health"]

        summary = analysis["summary"]

        return f"""
# 🏢 Business Health Assessment

---

## Executive Answer

**{health['status']}**

---

## Overall Business Score

**{health['score']:.1f}%**

---

## KPI Breakdown

Revenue Score

**{health['revenue_score']:.1f}%**

Profit Margin Score

**{health['margin_score']:.1f}%**

Customer Score

**{health['customer_score']:.1f}%**

Order Score

**{health['order_score']:.1f}%**

---

## Executive Insight

{summary}

---

## Recommended Action

Continue strengthening weaker KPIs while maintaining current operational efficiency.

---

## Confidence

{CONFIDENCE_BUSINESS}%
"""

    # =====================================================
    # EXECUTIVE BRIEFING
    # =====================================================

    elif intent == "executive_briefing":

        briefing = executive_briefing(df)

        return f"""
# 📰 Executive Briefing

{briefing}

---

## Confidence

98%
"""

    # =====================================================
    # BEST REGION
    # =====================================================

    elif intent == "best_region":

        region = best_region(df)

        remember("last_region", region)

        return f"""
# 🌍 Regional Performance

---

## Executive Answer

**{region['Region']}**

is currently the highest-performing region.

---

## Revenue

**₦{region['Revenue']:,.2f}**

---

## Growth Potential

**₦{region['Potential']:,.2f}**

---

## Confidence

**{region['Confidence']}%**

---

## Executive Insight

This region currently generates the strongest commercial performance.

---

## Recommended Action

Increase marketing investment, sales resources and operational support.
"""

    # =====================================================
    # BEST CATEGORY
    # =====================================================

    elif intent == "best_category":

        category = best_category(df)

        remember("last_category", category)

        return f"""
# 🏆 Product Category Performance

---

## Executive Answer

**{category['Category']}**

is currently the highest-performing category.

---

## Revenue

**₦{category['Revenue']:,.2f}**

---

## Growth Potential

**₦{category['Potential']:,.2f}**

---

## Confidence

**{category['Confidence']}%**

---

## Executive Insight

{INSIGHT_CATEGORY}

---

## Recommended Action

### Recommended Action

{ACTION_CATEGORY}
"""

    # =====================================================
    # FOLLOW-UP REGION REVENUE
    # =====================================================

    elif intent == "followup_region_revenue":

        region = recall("last_region")

        if region is None:

            return """
# 🌍 Regional Revenue

I don't know which region you are referring to yet.

Please ask:

• Which region performed best?

Then ask:

• How much revenue did it generate?
"""

        return f"""
# 🌍 Regional Revenue

---

## Executive Answer

**{region['Region']}**

generated

**₦{region['Revenue']:,.2f}**

---

## Executive Insight

This region remains the strongest revenue contributor.

---

## Recommended Action

Maintain investment while expanding market share.

---

## Confidence

{CONFIDENCE_REGION}%
"""

    # =====================================================
    # EXECUTIVE OPPORTUNITIES
    # =====================================================

    elif intent == "opportunity":

        region = best_region(df)
        category = best_category(df)

        return f"""
# 🚀 Executive Opportunities

---

## Highest Growth Region

**{region['Region']}**

Potential Revenue

**₦{region['Potential']:,.2f}**

---

## Highest Growth Category

**{category['Category']}**

Potential Revenue

**₦{category['Potential']:,.2f}**

---

## Executive Insight

These business areas currently provide the highest potential return on additional investment.

---

## Recommended Executive Action

• Increase executive attention

• Increase marketing investment

• Allocate additional inventory

• Expand sales coverage

• Closely monitor quarterly performance

---

## Confidence

95%
"""

    # =====================================================
    # BUSINESS RISKS
    # =====================================================

    elif intent == "risk":

        alerts = executive_alerts(df)

        report = """
# 🚨 Executive Risk Assessment

---

"""

        if alerts:

            for icon, message in alerts:
                report += f"{icon} {message}\n\n"

        else:

            report += "🟢 No significant business risks detected.\n\n"

        report += """

---

## Executive Insight

The above indicators represent the highest operational risks currently affecting business performance.

---

## Recommended Executive Action

• Address high-risk KPIs immediately

• Monitor medium-risk indicators weekly

• Review strategic performance monthly

• Continue executive oversight

---

## Confidence

{CONFIDENCE_RISK}%
"""

        return report

    # =====================================================
    # AI RECOMMENDATIONS
    # =====================================================

    elif intent == "recommendation":

        recommendation = generate_recommendation(df)

        return f"""
# 🎯 Executive Strategy Recommendation

---

## AI Recommendation

{recommendation}

---

## Executive Insight

Recommendations are generated using:

• Revenue

• Profitability

• Gross Margin

• Customer Performance

• Order Volume

• Regional Analysis

• Product Performance

• Executive Risk Indicators

---

## Confidence

{CONFIDENCE_RECOMMENDATION}%
"""

    # =====================================================
    # FOLLOW-UP (CATEGORY)
    # =====================================================

    elif intent == "followup_category_revenue":

        category = recall("last_category")

        if category is None:

            return """
# 🏆 Category Revenue

I don't know which category you are referring to yet.

Please ask:

• Which category performed best?

Then ask:

• How much revenue did it generate?
"""

        return f"""
# 🏆 Category Revenue

---

## Executive Answer

**{category['Category']}**

generated

**₦{category['Revenue']:,.2f}**

---

## Executive Insight

This category currently contributes the highest revenue within the portfolio.

---

## Recommended Executive Action

Maintain inventory levels while expanding promotional activities.

---

## Confidence

97%
"""

    # =====================================================
    # UNKNOWN QUESTION
    # =====================================================

    else:

        return """
# 🤖 Executive AI Assistant

I couldn't confidently understand your request.

---

## Try asking questions like:

• How much revenue did we make?

• Are we profitable?

• What is our gross margin?

• How many customers do we have?

• How many orders have we processed?

• How healthy is the business?

• Which region performed best?

• Which category performed best?

• How much revenue did it generate?

• Show opportunities

• Show business risks

• Give executive briefing

• Give recommendations

• Should we invest more?

---

Executive AI v6.0 is ready to answer strategic business questions using your enterprise sales data.
"""