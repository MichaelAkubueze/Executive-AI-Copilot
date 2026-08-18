from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent


# ==========================================================
# FONT PATHS
# ==========================================================

FONT_REGULAR = (
    PROJECT_ROOT
    / "assets"
    / "fonts"
    / "NotoSans-Regular.ttf"
)

FONT_BOLD = (
    PROJECT_ROOT
    / "assets"
    / "fonts"
    / "NotoSans-Bold.ttf"
)


# ==========================================================
# REGISTER FONTS
# ==========================================================

pdfmetrics.registerFont(
    TTFont(
        "NotoSans",
        str(FONT_REGULAR),
    )
)

pdfmetrics.registerFont(
    TTFont(
        "NotoSans-Bold",
        str(FONT_BOLD),
    )
)


# ==========================================================
# CREATE TEST PDF
# ==========================================================

filename = "test_naira.pdf"

pdf = canvas.Canvas(filename)

pdf.setFont(
    "NotoSans-Bold",
    16,
)

pdf.drawString(
    100,
    750,
    "Naira Rendering Test",
)

pdf.setFont(
    "NotoSans",
    14,
)

pdf.drawString(
    100,
    710,
    "Revenue: ₦74,018,814.78",
)

pdf.drawString(
    100,
    680,
    "Profit: ₦22,250,542.37",
)

pdf.drawString(
    100,
    650,
    "Expenses: ₦51,768,272.41",
)

pdf.drawString(
    100,
    620,
    "Target: ₦282,117,169.00",
)

pdf.save()

print(
    f"PDF created successfully: {filename}"
)

print(
    f"Regular font: {FONT_REGULAR}"
)

print(
    f"Bold font: {FONT_BOLD}"
)