import fitz
from PIL import Image

pdf_path = "assets/PF334.6 -  Đại Việt - Thiệp - 125x200mm - Duyệt (1).pdf"
doc = fitz.open(pdf_path)
page = doc[0]
pix = page.get_pixmap(dpi=300)
pix.save("temp_page0.png")

img = Image.open("temp_page0.png")
width, height = img.size
print(f"Original size: {width}x{height}")

# Assuming the left half is the "Lời tri ân"
# Let's crop it. Usually it's side by side or maybe top/bottom.
# From the user's screenshot, it looks like two panels side by side.
left_half = img.crop((0, 0, width//2, height))
left_half.save("assets/images/loi-tri-an.png")
print("Saved left half to assets/images/loi-tri-an.png")
