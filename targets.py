TARGETS = {

    "Revenue": 282_117_169,

    "Profit": 74_497_128,

    "Orders": 281_217,

    "Customers": 1_200,

    "Gross Margin": 0.35,

}


def load_targets():

    return TARGETS.copy()


def revenue_target(targets=None):

    if targets is None:
        targets = TARGETS

    return targets.get(
        "Revenue",
        0
    )


def profit_target(targets=None):

    if targets is None:
        targets = TARGETS

    return targets.get(
        "Profit",
        0
    )


def order_target(targets=None):

    if targets is None:
        targets = TARGETS

    return targets.get(
        "Orders",
        0
    )


def customer_target(targets=None):

    if targets is None:
        targets = TARGETS

    return targets.get(
        "Customers",
        0
    )


def get_target(name):

    return TARGETS.get(
        name,
        0
    )


def achievement(actual, target):

    if target == 0:
        return 0

    return actual / target * 100


def variance(actual, target):

    return actual - target


def status(actual, target):

    pct = achievement(
        actual,
        target
    )

    if pct >= 100:
        return "Excellent"

    if pct >= 90:
        return "Good"

    if pct >= 75:
        return "Watch"

    return "Critical"