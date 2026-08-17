from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os


# ==========================================================
# FONT CONFIGURATION
# ==========================================================
#
# Use Calibri when it is available locally.
# Fall back to ReportLab's built-in Helvetica fonts on
# Linux/Streamlit Cloud.
#
# This keeps the application platform-independent.
# ==========================================================


CALIBRI_PATH = r"C:\Windows\Fonts\calibri.ttf"
CALIBRI_BOLD_PATH = r"C:\Windows\Fonts\calibrib.ttf"


FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"


# ----------------------------------------------------------
# CALIBRI AVAILABLE?
# ----------------------------------------------------------

if (
    os.path.exists(CALIBRI_PATH)
    and os.path.exists(CALIBRI_BOLD_PATH)
):

    try:

        if "Calibri" not in pdfmetrics.getRegisteredFontNames():

            pdfmetrics.registerFont(
                TTFont(
                    "Calibri",
                    CALIBRI_PATH,
                )
            )

        if "Calibri-Bold" not in pdfmetrics.getRegisteredFontNames():

            pdfmetrics.registerFont(
                TTFont(
                    "Calibri-Bold",
                    CALIBRI_BOLD_PATH,
                )
            )

        FONT_REGULAR = "Calibri"
        FONT_BOLD = "Calibri-Bold"

    except Exception:

        FONT_REGULAR = "Helvetica"
        FONT_BOLD = "Helvetica-Bold"


# ==========================================================
# BASE STYLES
# ==========================================================

styles = getSampleStyleSheet()


# ==========================================================
# REPORT TITLE
# ==========================================================

TITLE_STYLE = ParagraphStyle(
    "ReportTitle",
    parent=styles["Title"],
    fontName=FONT_BOLD,
    fontSize=20,
    leading=24,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#123B63"),
    spaceAfter=10,
)


# ==========================================================
# REPORT HEADING
# ==========================================================

HEADING_STYLE = ParagraphStyle(
    "ReportHeading",
    parent=styles["Heading2"],
    fontName=FONT_BOLD,
    fontSize=13,
    leading=17,
    textColor=colors.HexColor("#123B63"),
    spaceBefore=8,
    spaceAfter=8,
)


# ==========================================================
# REPORT BODY
# ==========================================================

BODY_STYLE = ParagraphStyle(
    "ReportBody",
    parent=styles["BodyText"],
    fontName=FONT_REGULAR,
    fontSize=10,
    leading=15,
    textColor=colors.black,
    spaceAfter=6,
)

