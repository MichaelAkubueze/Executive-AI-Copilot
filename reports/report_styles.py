from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)


# ==========================================================
# PLATFORM-INDEPENDENT FONT CONFIGURATION
# ==========================================================
#
# Use ReportLab built-in fonts.
#
# This avoids dependency on:
#   C:\Windows\Fonts
#
# and ensures PDF generation works on:
#   - Windows
#   - Linux
#   - Streamlit Cloud
#   - Other deployment environments
#
# ==========================================================

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