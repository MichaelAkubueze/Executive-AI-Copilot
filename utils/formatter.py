from utils.currency import format_currency
from utils.numbers import format_number


def format_percent(value):

    if value is None:
        return "0.00%"

    return f"{value:.2%}"
