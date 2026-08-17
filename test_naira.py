from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# ==========================================================
# WINDOWS UNICODE FONT
# ==========================================================

FONT_PATH = r"C:\Windows\Fonts\segoeui.ttf"


# ==========================================================
# REGISTER FONT
# ==========================================================

pdfmetrics.registerFont(
    TTFont(
        "SegoeUI",
        FONT_PATH,
    )
)


# ==========================================================
# CREATE TEST PDF
# ==========================================================

filename = "test_naira.pdf"

pdf = canvas.Canvas(filename)

pdf.setFont(
    "SegoeUI",
    16,
)

pdf.drawString(
    100,
    750,
    "Naira Test: ₦1,250,000.00",
)

pdf.drawString(
    100,
    720,
    "Revenue: ₦74,018,814.78",
)

pdf.drawString(
    100,
    690,
    "Profit: ₦22,250,542.37",
)

pdf.save()

print(
    f"PDF created successfully: {filename}"
)