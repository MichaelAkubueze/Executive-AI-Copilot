# ==========================================
# NUMBER FORMATTER
# ==========================================

def format_number(value):

    if value is None:
        return "0"

    if abs(value) >= 1_000_000_000:
        return f"{value/1_000_000_000:,.2f}B"

    if abs(value) >= 1_000_000:
        return f"{value/1_000_000:,.2f}M"

    return f"{value:,.0f}"

