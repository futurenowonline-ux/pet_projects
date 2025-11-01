import qrcode
from PIL import Image, ImageDraw, ImageFont

# URL for the QR code
url = "bit.ly/joinhellotitans"

# Generate QR code
qr = qrcode.QRCode(
    version=4,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction to allow logo overlay
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo image from file
logo_path = 'logo.png'  # Make sure this file is in the same directory as the script
logo = Image.open(logo_path)

# Resize logo to fit in the center of the QR code
logo_size = 100
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Ensure logo has an alpha channel for transparency
if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')

# Create a mask for the logo
mask = logo.split()[3]

# Calculate logo position
qr_width, qr_height = qr_img.size
logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste the logo into the QR code with mask
qr_img.paste(logo, logo_pos, mask)

# Add "Book Now" CTA text below the QR code
cta_text = "Scan Here"

# Create a new image to add text below
total_height = qr_height + 50
new_img = Image.new('RGB', (qr_width, total_height), 'white')
new_img.paste(qr_img, (0, 0))

# Draw the text
draw = ImageDraw.Draw(new_img)
try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), cta_text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

text_x = (qr_width - text_width) // 2
text_y = qr_height + 10

# Draw text in black
draw.text((text_x, text_y), cta_text, font=font, fill='black')

# Save the final image
new_img.save("logo_qr_code.png")
print("QR code saved as logo_qr_code.png")
