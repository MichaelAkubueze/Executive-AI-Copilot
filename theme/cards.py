from theme.colors import *
from theme.spacing import *


def card_style():

    return f"""
        background:{CARD};
        padding:{CARD_PADDING};
        border-radius:{CARD_RADIUS};
        box-shadow:{SHADOW};
        border:1px solid {BORDER};
        margin-bottom:{CARD_MARGIN};
    """