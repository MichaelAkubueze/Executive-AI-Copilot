from datetime import datetime


def report_date():
    return datetime.now().strftime("%d %B %Y")


def report_time():
    return datetime.now().strftime("%H:%M")


def naira(value):
    return f"₦{value:,.2f}"

