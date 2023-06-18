# pip install qrcode

import qrcode
from PIL import Image, ImageDraw

# Generate the QR code
url = 'https://cargonvis.github.io/'
qr = qrcode.QRCode(version=1, box_size=10, border=6)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Convert the QR code to a rounded shape
width, height = img.size
mask = Image.new('L', (width, height), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, width, height), fill=255)

# Convert the image mode to RGBA
img = img.convert("RGBA")
img.putalpha(mask)

# Create a new image with a circular border
border_width = 10
border_color = "black"
img_with_border = Image.new("RGBA", (width + border_width * 2, height + border_width * 2), (255, 255, 255, 0))
draw = ImageDraw.Draw(img_with_border)
draw.ellipse((0, 0, width + border_width * 2, height + border_width * 2), outline=border_color, width=border_width)

# Paste the QR code image on top of the border
img_with_border.paste(img, (border_width, border_width), img)

# Save the final image
img_with_border.save('rounded_qr_with_border.png')