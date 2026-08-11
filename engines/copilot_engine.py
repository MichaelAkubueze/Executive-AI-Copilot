from engines.intent_engine import detect_intent

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_total_orders,
    get_total_customers,
    get_gross_margin,
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

from engines.advisor import generate_recommendation


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def executive_summary(df):

    health = business_health(df)

    return f"""
## 🤖 Executive AI

Business Health:
**{health['status']}**

Overall Health Score:
**{health['score']:.1f}%**

You can ask questions like:

• How much revenue did we make?
• Are we profitable?
• How healthy is the business?
• Show executive briefing
• Show business risks
• Show opportunities
• Which region performed best?
• Which category performed best?
• Give recommendations
"""


# ==========================================================
# EXECUTIVE COPILOT
# ==========================================================

def answer_question(df, question):

    intent = detect_intent(question)

    # =====================================================
    # REVENUE
    # =====================================================

    if intent == "revenue":

        revenue = get_total_revenue(df)

        target = 100_000_000

        achievement = (revenue / target) * 100

        if achievement >= 90:
            status = "🟢 Revenue performance is excellent."

        elif achievement >= 75:
            status = "🟠 Revenue performance is healthy but below target."

        else:
            status = "🔴 Revenue performance is below expectations."

        return f"""
## 💰 Revenue Performance

### Executive Answer

Current revenue is **₦{revenue:,.2f}**

### Business Context

Revenue achievement is **{achievement:.1f}%** of the annual target.

### Executive Insight

{status}

### Recommended Action

Increase investment in the highest-performing regions and product categories.

### Confidence

96%
"""

    # =====================================================
    # PROFIT
    # =====================================================

    elif intent == "profit":

        profit = get_total_profit(df)

        margin = get_gross_margin(df)

        if margin >= 25:
            status = "✅ Yes. The business is profitable."

        else:
            status = "🟠 Profitability needs improvement."

        return f"""
## 📈 Profitability Analysis

### Executive Answer

{status}

### Current Profit

₦{profit:,.2f}

### Gross Margin

{margin:.2f}%

### Executive Insight

Profitability remains healthy.

### Recommended Action

Continue focusing on high-margin products while improving revenue growth.

### Confidence

97%
"""

    # =====================================================
    # GROSS MARGIN
    # =====================================================

    elif intent == "margin":

        margin = get_gross_margin(df)

        return f"""
## 📊 Gross Margin

Current Gross Margin

**{margin:.2f}%**

This indicates the percentage of revenue retained after direct costs.

Confidence

97%
"""

    # =====================================================
    # CUSTOMERS
    # =====================================================

    elif intent == "customers":

        customers = get_total_customers(df)

        return f"""
## 👥 Customer Performance

### Executive Answer

The business currently serves **{customers:,}** unique customers.

### Business Context

Customer growth remains an important driver of long-term revenue.

### Executive Insight

Maintaining strong customer acquisition and retention will improve sustainable growth.

### Recommended Action

Strengthen customer loyalty programmes and acquire new high-value customers.

### Confidence

95%
"""

    # =====================================================
    # ORDERS
    # =====================================================

    elif intent == "orders":

        orders = get_total_orders(df)

        return f"""
## 🛒 Order Performance

### Executive Answer

Total processed orders are **{orders:,}**.

### Business Context

Order volume reflects current business activity.

### Executive Insight

Consistent order growth supports revenue expansion.

### Recommended Action

Increase conversion campaigns to improve order volume.

### Confidence

95%
"""

    # =====================================================
    # BUSINESS HEALTH
    # =====================================================

    elif intent == "business_health":

        health = business_health(df)

        return f"""
## 🏢 Business Health

### Executive Answer

Current business status:

**{health['status']}**

### Overall Health Score

**{health['score']:.1f}%**

### KPI Breakdown

• Revenue Score: {health['revenue_score']:.1f}%

• Profit Margin Score: {health['margin_score']:.1f}%

• Customer Score: {health['customer_score']:.1f}%

• Order Score: {health['order_score']:.1f}%

### Executive Insight

The organisation is financially stable with healthy operational performance.

### Recommended Action

Maintain profitability while accelerating revenue growth.

### Confidence

98%
"""

    # =====================================================
    # EXECUTIVE BRIEFING
    # =====================================================

    elif intent == "executive_briefing":

        return executive_briefing(df)

    # =====================================================
    # BEST REGION
    # =====================================================

    elif intent == "best_region":

        region = best_region(df)

        return f"""
## 🌍 Regional Performance

### Executive Answer

**{region['Region']}** is currently the strongest-performing region.

### Revenue

₦{region['Revenue']:,.2f}

### Growth Opportunity

₦{region['Potential']:,.2f}

### Executive Insight

This region consistently delivers the highest revenue and offers the greatest opportunity for expansion.

### Recommended Action

Increase marketing and operational investment within this region.

### Confidence

{region['Confidence']}%
"""

    # =====================================================
    # BEST CATEGORY
    # =====================================================

    elif intent == "best_category":

        category = best_category(df)

        return f"""
## 🏆 Product Category Performance

### Executive Answer

**{category['Category']}** is the highest-performing product category.

### Revenue

₦{category['Revenue']:,.2f}

### Growth Opportunity

₦{category['Potential']:,.2f}

### Executive Insight

Demand remains consistently high for this category.

### Recommended Action

Expand inventory and promotional activities for this category.

### Confidence

{category['Confidence']}%
"""

    # =====================================================
    # OPPORTUNITIES
    # =====================================================

    elif intent == "opportunity":

        region = best_region(df)
        category = best_category(df)

        return f"""
## 🚀 Executive Opportunities

### Highest Growth Region

**{region['Region']}**

Potential Revenue

₦{region['Potential']:,.2f}

---

### Highest Growth Category

**{category['Category']}**

Potential Revenue

₦{category['Potential']:,.2f}

### Executive Insight

Current performance indicates these two business areas provide the greatest opportunity for expansion.

### Recommended Action

Increase inventory, marketing budget and executive focus in these areas.

### Confidence

95%
"""

    # =====================================================
    # RISKS
    # =====================================================

    elif intent == "risk":

        alerts = executive_alerts(df)

        report = """
## 🚨 Executive Risk Assessment

"""

        for icon, message in alerts:
            report += f"{icon} {message}\n\n"

        report += """
### Executive Recommendation

Address medium- and high-risk indicators before they impact profitability.

### Confidence

94%
"""

        return report

    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    elif intent == "recommendation":

        recommendation = generate_recommendation(df)

        return f"""
## 🎯 Executive Strategy

### AI Recommendation

{recommendation}

### Executive Insight

Recommendations are generated from revenue, profitability, customer performance, regional analysis and product performance.

### Confidence

96%
"""

    # =====================================================
    # UNKNOWN
    # =====================================================

    else:

        return """
## 🤖 Executive Copilot

I couldn't understand your request.

Try asking:

• How much revenue did we make?

• Are we profitable?

• How healthy is the business?

• Which region performed best?

• Which category performed best?

• Show opportunities

• Show business risks

• Give executive briefing

• Give recommendations
"""