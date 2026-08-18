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

# ----------------------------------------------------------
# Project-bundled Noto Sans
# ----------------------------------------------------------
#
# These fonts are committed inside the repository so PDF
# generation works consistently on:
#
# - Windows
# - Linux
# - Streamlit Cloud
# - Other deployment environments
#
# Noto Sans supports Unicode characters including the
# Nigerian Naira symbol: ₦
#

PROJECT_REGULAR = (
    PROJECT_ROOT
    / "assets"
    / "fonts"
    / "NotoSans-Regular.ttf"
)

PROJECT_BOLD = (
    PROJECT_ROOT
    / "assets"
    / "fonts"
    / "NotoSans-Bold.ttf"
)


# ----------------------------------------------------------
# Windows Segoe UI fallback
# ----------------------------------------------------------

WINDOWS_REGULAR = Path(
    r"C:\Windows\Fonts\segoeui.ttf"
)

WINDOWS_BOLD = Path(
    r"C:\Windows\Fonts\segoeuib.ttf"
)


# ==========================================================
# DEFAULT REPORTLAB FONTS
# ==========================================================
#
# Helvetica is always available in ReportLab.
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

        registered_fonts = pdfmetrics.getRegisteredFontNames()

        if font_name not in registered_fonts:

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
# 1. Project-bundled Noto Sans
# 2. Windows Segoe UI
# 3. Helvetica
#
# Noto Sans is the preferred font because it is stored
# inside the project repository and therefore available
# to Streamlit Cloud / Linux.
# ==========================================================

regular_registered = False
bold_registered = False


# ----------------------------------------------------------
# 1. PROJECT-BUNDLED NOTO SANS
# ----------------------------------------------------------

regular_registered = register_font(
    "NotoSans",
    PROJECT_REGULAR,
)

bold_registered = register_font(
    "NotoSans-Bold",
    PROJECT_BOLD,
)


if (
    regular_registered
    and bold_registered
):

    FONT_REGULAR = "NotoSans"
    FONT_BOLD = "NotoSans-Bold"


# ----------------------------------------------------------
# 2. WINDOWS SEGoe UI FALLBACK
# ----------------------------------------------------------

else:

    regular_registered = register_font(
        "SegoeUI",
        WINDOWS_REGULAR,
    )

    bold_registered = register_font(
        "SegoeUI-Bold",
        WINDOWS_BOLD,
    )

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
# FINANCIAL STYLES
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

    Useful for debugging local and Streamlit Cloud
    deployments.
    """

    registered_fonts = pdfmetrics.getRegisteredFontNames()

    return {
        "regular_font": FONT_REGULAR,
        "bold_font": FONT_BOLD,
        "regular_registered": (
            FONT_REGULAR
            in registered_fonts
        ),
        "bold_registered": (
            FONT_BOLD
            in registered_fonts
        ),
        "noto_regular_exists": (
            PROJECT_REGULAR.exists()
        ),
        "noto_bold_exists": (
            PROJECT_BOLD.exists()
        ),
        "noto_regular_size": (
            PROJECT_REGULAR.stat().st_size
            if PROJECT_REGULAR.exists()
            else 0
        ),
        "noto_bold_size": (
            PROJECT_BOLD.stat().st_size
            if PROJECT_BOLD.exists()
            else 0
        ),
    }