def money(value):

    if value >= 1_000_000_000:

        return f"₦{value/1_000_000_000:.2f}B"

    if value >= 1_000_000:

        return f"₦{value/1_000_000:.2f}M"

    if value >= 1000:

        return f"₦{value:,.0f}"

    return f"₦{value:.2f}"

