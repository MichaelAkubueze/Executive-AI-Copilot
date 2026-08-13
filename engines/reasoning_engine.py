from ai_config import (
    DEFAULT_REVENUE_TARGET,

    EXCELLENT_THRESHOLD,
    HEALTHY_THRESHOLD,
    WATCH_THRESHOLD,

    HIGH_MARGIN,
    MEDIUM_MARGIN,

    STATUS_EXCELLENT,
    STATUS_HEALTHY,
    STATUS_WATCH,
    STATUS_CRITICAL,

    CONFIDENCE_EXCELLENT,
    CONFIDENCE_HEALTHY,
    CONFIDENCE_WATCH,
    CONFIDENCE_CRITICAL,

    RISK_LOW,
    RISK_MODERATE,
    RISK_HIGH,
    RISK_CRITICAL,

    PRIORITY_MAINTAIN,
    PRIORITY_GROWTH,
    PRIORITY_REVENUE,
    PRIORITY_INTERVENTION,

    BOARDROOM_EXCELLENT,
    BOARDROOM_HEALTHY,
    BOARDROOM_WATCH,
    BOARDROOM_CRITICAL,
)

from engines.target_engine import get_target

from analytics import (
    get_total_revenue,
    get_total_profit,
    get_gross_margin,
    get_total_orders,
    get_total_customers,
)

from engines.executive_engine import business_health

def explain_revenue(df):

    revenue = get_total_revenue(df)
    profit = get_total_profit(df)
    margin = get_gross_margin(df)
    
    target = get_target("Revenue")

    achievement = revenue / target * 100

    if achievement >= EXCELLENT_THRESHOLD:

        status = STATUS_EXCELLENT

        insight = (
            f"Revenue of ₦{revenue:,.0f} represents "
            f"{achievement:.1f}% of the annual target. "
            f"The company generated ₦{profit:,.0f} in profit "
            f"while maintaining a gross margin of {margin:.1f}%."
        )
        impact = (
        "Strong revenue growth improves cash flow, supports business expansion, "
        "increases investor confidence, and provides capacity for strategic investments."
    )
        confidence = CONFIDENCE_EXCELLENT
        risk = RISK_LOW
        priority = PRIORITY_MAINTAIN
        
        recommendation = (
    "• Sustain current revenue growth.\n"
    "• Expand into new markets.\n"
    "• Increase strategic investments in high-performing regions.\n"
    "• Continue monitoring profitability."
    )

        boardroom_takeaway = BOARDROOM_EXCELLENT
    elif achievement >= HEALTHY_THRESHOLD:

        status = STATUS_HEALTHY

        insight = (
            f"Revenue of ₦{revenue:,.0f} represents "
            f"{achievement:.1f}% of the annual target. "
            f"The company generated ₦{profit:,.0f} in profit "
            f"while maintaining a gross margin of {margin:.1f}%."
        )
        impact = (
        "Current revenue performance supports stable operations and continued growth, "
        "although additional commercial initiatives could accelerate performance."
    )
        confidence = CONFIDENCE_HEALTHY
        risk = RISK_MODERATE
        priority = PRIORITY_GROWTH
        
        recommendation = (
    "• Increase sales campaigns.\n"
    "• Strengthen customer retention.\n"
    "• Expand top-performing product categories.\n"
    "• Monitor monthly revenue trends."
    )

        boardroom_takeaway = BOARDROOM_HEALTHY
    elif achievement >= WATCH_THRESHOLD:

        #status = "Watch"
        status = STATUS_WATCH

        insight = (
            f"Revenue has achieved {achievement:.1f}% of target. "
            f"Although revenue remains below strategic expectations, "
            f"profitability (₦{profit:,.0f}) and gross margin ({margin:.1f}%) "
            "indicate that operational efficiency remains strong."
        )
        impact = (
        "Business operations remain sustainable, but slower revenue growth may "
        "limit future expansion if not addressed."
    )
        confidence = CONFIDENCE_WATCH
        risk = RISK_HIGH
        priority = PRIORITY_REVENUE
        
        recommendation = (
    "• Expand high-performing regions.\n"
    "• Increase investment in the strongest product categories.\n"
    "• Strengthen sales conversion.\n"
    "• Review monthly revenue against targets."
    )

        boardroom_takeaway = BOARDROOM_WATCH
    else:

        #status = "Critical"
        status = STATUS_CRITICAL

        insight = (
            "Revenue performance is significantly below strategic expectations. "
            "Immediate commercial intervention is recommended."
        )
        impact = (
        "Poor revenue performance may reduce profitability, cash flow, and "
        "the organisation's ability to achieve strategic objectives."
    )
        confidence = CONFIDENCE_CRITICAL
        risk = RISK_CRITICAL
        priority = PRIORITY_INTERVENTION
        
        recommendation = (
    "• Launch immediate revenue recovery initiatives.\n"
    "• Review pricing and sales strategy.\n"
    "• Reduce underperforming operations.\n"
    "• Increase executive oversight."
    )

        boardroom_takeaway = BOARDROOM_CRITICAL
    return {

        "metric": revenue,

        "achievement": achievement,

        "status": status,

        "insight": insight,
        
        "impact": impact,
        
        "risk": risk,
        
        "priority": priority,
        
        "recommendation": recommendation,
        
        "boardroom_takeaway": boardroom_takeaway,
        
        "confidence": confidence,
        

    }

def explain_profit(df):

    profit = get_total_profit(df)

    margin = get_gross_margin(df)

    if margin >= HIGH_MARGIN:

        insight = (
            "Profitability exceeds the company's expected margin."
        )

    else:

        insight = (
            "Profitability requires improvement through cost optimisation."
        )

    return {

        "profit": profit,

        "margin": margin,

        "insight": insight,

    }


def explain_business(df):

    health = business_health(df)

    if health["score"] >= 90:

        summary = (
            "Business performance is excellent."
        )

    elif health["score"] >= 75:

        summary = (
            "Business performance is healthy with opportunities for improvement."
        )

    elif health["score"] >= 60:

        summary = (
            "Business performance requires executive attention."
        )

    else:

        summary = (
            "Business performance is critical and immediate intervention is required."
        )

    return {

        "health": health,

        "summary": summary,

    }
    
    