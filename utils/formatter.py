from config.settings import CURRENCY


def currency(value):

    return f"{CURRENCY}{value:,.2f}"


def millions(value):

    return f"{CURRENCY}{value/1_000_000:.2f}M"


def percent(value):

    return f"{value:.2f}%"