from theme.colors import *


def badge(status):

    status=status.lower()

    if status in [

        "excellent",

        "healthy",

        "growing",

        "business growth"

    ]:

        colour=SUCCESS

    elif status in [

        "warning",

        "watch"

    ]:

        colour=WARNING

    else:

        colour=DANGER

    return colour

