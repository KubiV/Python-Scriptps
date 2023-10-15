import sys
from PIL import Image, ImageDraw, ImageFont
import os

# Input files names
if len(sys.argv) < 2:
    print("Enter image names as arguments for the script")
    sys.exit(1)

file_paths = sys.argv[1:] # File names as a list

# Going through the file names list
for file_path in file_paths:

    # Is file an image
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        continue
    if not file_path.endswith((".jpg", ".jpeg", ".png", ".bmp")):
        print(f"File {file_path} needs to be JPG, JPEG, PNG or BMP.")
        continue

    # Image loading
    try:
        image = Image.open(file_path)
    except IOError:
        print(f"Error loading the image {file_path}.")
        continue

    # Image crop 9:16 - vertical (for a phone wallpaper)
    width, height = image.size
    if width / height > 9 / 16:
        new_width = int(height * 9 / 16)
        left = (width - new_width) / 2
        right = left + new_width
        top = 0
        bottom = height
    else:
        new_height = int(width * 16 / 9)
        top = (height - new_height) / 2
        bottom = top + new_height
        left = 0
        right = width
    image = image.crop((left, top, right, bottom))

    # Addition of the text to the image from thr file name
    filename = os.path.splitext(os.path.basename(file_path))[0]
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Arial.ttf", 20)
    text_width, text_height = draw.textsize(filename, font=font)
    x = (image.width - text_width) / 2
    y = image.height * 2 / 3
    draw.text((x, y), filename, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0,0,0), font=font)

    # Save the final image
    output_filename = os.path.splitext(filename)[0] + "_edited.png"
    image.save(output_filename)

    print(f"File {filename} was saved as {output_filename}.")
