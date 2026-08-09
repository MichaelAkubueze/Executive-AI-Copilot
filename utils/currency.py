# ==========================================
# ENTERPRISE CURRENCY FORMATTER
# ==========================================

def format_currency(value, symbol="₦"):

    if value is None:
        return f"{symbol}0.00"

    if abs(value) >= 1_000_000_000:
        return f"{symbol}{value/1_000_000_000:,.2f}B"

    if abs(value) >= 1_000_000:
        return f"{symbol}{value/1_000_000:,.2f}M"

    if abs(value) >= 1_000:
        return f"{symbol}{value:,.0f}"

    return f"{symbol}{value:,.2f}"
