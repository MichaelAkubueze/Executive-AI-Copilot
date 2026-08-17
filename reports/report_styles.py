import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ==========================================================
# FONT PATHS
# ==========================================================

# Windows Segoe UI
WINDOWS_REGULAR = Path(
    r"C:\Windows\Fonts\segoeui.ttf"
)

WINDOWS_BOLD = Path(
    r"C:\Windows\Fonts\segoeuib.ttf"
)


# Optional project fonts
#
# These allow Streamlit Cloud / Linux to use a font
# committed inside the project repository.
#
# Recommended structure:
#
# 03_Python_SQL_Analytics/
#       assets/
#           fonts/
#               segoeui.ttf
#               segoeuib.ttf
#

PROJECT_REGULAR = (
    PROJECT_ROOT
    / "assets"
    / "fonts"
    / "segoeui.ttf"
)

PROJECT_BOLD = (
    PROJECT_ROOT
    / "assets"
    / "fonts"
    / "segoeuib.ttf"
)


# ==========================================================
# DEFAULT REPORTLAB FONTS
# ==========================================================
#
# Helvetica is always available in ReportLab.
#
# It is used only as the final fallback.
#

FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"


# ==========================================================
# FONT REGISTRATION HELPER
# ==========================================================

def register_font(
    font_name,
    font_path,
):
    """
    Register a TrueType font safely.

    Returns True if registration succeeds.
    Returns False if the font cannot be loaded.
    """

    try:

        if not font_path.exists():
            return False

        if (
            font_name
            not in pdfmetrics.getRegisteredFontNames()
        ):

            pdfmetrics.registerFont(
                TTFont(
                    font_name,
                    str(font_path),
                )
            )

        return True

    except Exception:

        return False


# ==========================================================
# SELECT REPORT FONT
# ==========================================================
#
# Priority:
#
# 1. Windows Segoe UI
# 2. Project-bundled Segoe UI
# 3. Helvetica fallback
#
# Segoe UI contains the Naira symbol (₦), which is
# important for financial PDF reports.
# ==========================================================

regular_registered = False
bold_registered = False


# ----------------------------------------------------------
# WINDOWS
# ----------------------------------------------------------

if (
    WINDOWS_REGULAR.exists()
    and WINDOWS_BOLD.exists()
):

    regular_registered = register_font(
        "SegoeUI",
        WINDOWS_REGULAR,
    )

    bold_registered = register_font(
        "SegoeUI-Bold",
        WINDOWS_BOLD,
    )


# ----------------------------------------------------------
# PROJECT-BUNDLED FONT
# ----------------------------------------------------------

if not (
    regular_registered
    and bold_registered
):

    regular_registered = register_font(
        "SegoeUI",
        PROJECT_REGULAR,
    )

    bold_registered = register_font(
        "SegoeUI-Bold",
        PROJECT_BOLD,
    )


# ----------------------------------------------------------
# FINAL FONT SELECTION
# ----------------------------------------------------------

if (
    regular_registered
    and bold_registered
):

    FONT_REGULAR = "SegoeUI"
    FONT_BOLD = "SegoeUI-Bold"


# ==========================================================
# REPORT STYLES
# ==========================================================

TITLE_STYLE = ParagraphStyle(
    "ReportTitle",
    fontName=FONT_BOLD,
    fontSize=18,
    leading=22,
    alignment=TA_CENTER,
    spaceAfter=8,
)


SUBTITLE_STYLE = ParagraphStyle(
    "ReportSubtitle",
    fontName=FONT_REGULAR,
    fontSize=11,
    leading=14,
    alignment=TA_CENTER,
    spaceAfter=8,
)


HEADING_STYLE = ParagraphStyle(
    "ReportHeading",
    fontName=FONT_BOLD,
    fontSize=13,
    leading=16,
    alignment=TA_LEFT,
    spaceBefore=4,
    spaceAfter=8,
)


BODY_STYLE = ParagraphStyle(
    "ReportBody",
    fontName=FONT_REGULAR,
    fontSize=9.5,
    leading=13,
    alignment=TA_LEFT,
)


TABLE_HEADER_STYLE = ParagraphStyle(
    "ReportTableHeader",
    fontName=FONT_BOLD,
    fontSize=8,
    leading=10,
    textColor=colors.white,
)


TABLE_BODY_STYLE = ParagraphStyle(
    "ReportTableBody",
    fontName=FONT_REGULAR,
    fontSize=8,
    leading=10,
)


# ==========================================================
# OPTIONAL FINANCIAL STYLE
# ==========================================================

MONEY_STYLE = ParagraphStyle(
    "ReportMoney",
    fontName=FONT_REGULAR,
    fontSize=9,
    leading=12,
    alignment=TA_LEFT,
)


MONEY_BOLD_STYLE = ParagraphStyle(
    "ReportMoneyBold",
    fontName=FONT_BOLD,
    fontSize=9,
    leading=12,
    alignment=TA_LEFT,
)


# ==========================================================
# FONT STATUS
# ==========================================================

def get_report_font_status():
    """
    Returns information about the active PDF fonts.
    Useful for debugging Streamlit Cloud deployments.
    """

    return {
        "regular_font": FONT_REGULAR,
        "bold_font": FONT_BOLD,
        "regular_registered": (
            FONT_REGULAR
            in pdfmetrics.getRegisteredFontNames()
        ),
        "bold_registered": (
            FONT_BOLD
            in pdfmetrics.getRegisteredFontNames()
        ),
    }