from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# ==========================================================
# CALIBRI FONTS
# ==========================================================

pdfmetrics.registerFont(
    TTFont(
        "Calibri",
        r"C:\Windows\Fonts\calibri.ttf"
    )
)

pdfmetrics.registerFont(
    TTFont(
        "Calibri-Bold",
        r"C:\Windows\Fonts\calibrib.ttf"
    )
)


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
    fontName="Calibri-Bold",
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
    fontName="Calibri-Bold",
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
    fontName="Calibri",
    fontSize=10,
    leading=15,
    textColor=colors.black,
    spaceAfter=6,
)