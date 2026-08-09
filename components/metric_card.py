import streamlit as st

from datetime import datetime

from theme.colors import *
from theme.cards import card_style


def metric_card(
    title,
    value,
    icon="📊",
    change=None,
    suffix="%",
    status="Healthy",
    target=None,
    achievement=None,
):

    # -----------------------------------------
    # Trend
    # -----------------------------------------

    if change is None:

        trend = ""

        trend_colour = TEXT_LIGHT

    elif change > 0:

        trend = f"▲ +{change:.2f}{suffix}"

        trend_colour = SUCCESS

    elif change < 0:

        trend = f"▼ {change:.2f}{suffix}"

        trend_colour = DANGER

    else:

        trend = f"■ {change:.2f}{suffix}"

        trend_colour = WARNING

    # -----------------------------------------
    # Achievement Bar
    # -----------------------------------------

    progress_html = ""

    if achievement is not None:

        width = min(max(float(achievement), 0), 100)

        colour = SUCCESS

        if width < 50:
            colour = DANGER
        elif width < 75:
            colour = WARNING

        progress_html = f"""
        <div style="margin-top:12px;">

            <div style="
                background:#E5E7EB;
                height:8px;
                border-radius:5px;
                overflow:hidden;
            ">

                <div style="
                    width:{width}%;
                    height:8px;
                    background:{colour};
                "></div>

            </div>

            <div style="
                font-size:12px;
                color:{TEXT_LIGHT};
                margin-top:6px;
            ">

                {width:.1f}% Target Achieved

            </div>

        </div>
        """

    # -----------------------------------------
    # Target
    # -----------------------------------------

    target_html = ""

    if target:

        target_html = f"""
        <div style="
            font-size:13px;
            color:{TEXT_LIGHT};
            margin-top:10px;
        ">

            🎯 Target: <b>{target}</b>

        </div>
        """

    # -----------------------------------------
    # Status Badge
    # -----------------------------------------

    badge_colour = INFO

    if status.lower() in ["excellent", "healthy", "business growth", "growing"]:

        badge_colour = SUCCESS

    elif status.lower() in ["warning", "watch"]:

        badge_colour = WARNING

    elif status.lower() in ["critical", "poor"]:

        badge_colour = DANGER

    # -----------------------------------------
    # Timestamp
    # -----------------------------------------

    updated = datetime.now().strftime("%d %b %Y %I:%M %p")

    # -----------------------------------------
    # Render
    # -----------------------------------------

    st.markdown(

        f"""
        <div style="{card_style()}">

            <div style="font-size:36px;">
                {icon}
            </div>

            <div style="
                font-size:14px;
                color:{TEXT_LIGHT};
                margin-top:8px;
            ">
                {title}
            </div>

            <div style="
                font-size:34px;
                font-weight:700;
                color:{TEXT};
                margin-top:10px;
            ">
                {value}
            </div>

            <div style="
                color:{trend_colour};
                font-weight:700;
                font-size:15px;
                margin-top:10px;
            ">
                {trend}
            </div>

            {progress_html}

            {target_html}

            <div style="
                display:inline-block;
                margin-top:12px;
                padding:5px 12px;
                border-radius:14px;
                background:{badge_colour}20;
                color:{badge_colour};
                font-size:12px;
                font-weight:600;
            ">
                {status}
            </div>

            <div style="
                font-size:11px;
                color:{TEXT_LIGHT};
                margin-top:14px;
            ">
                🕒 Updated: {updated}
            </div>

        </div>
        """,

        unsafe_allow_html=True,

    )