from theme.colors import *


def progress(percent):

    colour=SUCCESS

    if percent<50:

        colour=DANGER

    elif percent<75:

        colour=WARNING

    return f"""

    <div style="

        background:#E5E7EB;

        height:8px;

        border-radius:10px;

        overflow:hidden;

    ">

        <div style="

            width:{percent}%;

            background:{colour};

            height:8px;

        ">

        </div>

    </div>

    """
    
    