import pyperclip
import qrcode
from PIL import Image

# Get the clipvboard content
clipboard_content = pyperclip.paste()

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(clipboard_content)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code to the temorary file
qr_img.save("temp_qr.png")

# Open the QR code image file
qr_img.show()

# Script waits for the image window to be closed
input("Press Enter to close the QR code window...")
