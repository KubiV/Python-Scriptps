import os
import cv2
import numpy as np

# Path to the directory with images
path = "/folder"

# List for images
images = []

# Loading the images from the directory
for file in os.listdir(path):
    if file.endswith(".png"):
        file_path = os.path.join(path, file)
        images.append(cv2.imread(file_path))

# Sort images by names
images = sorted(images, key=lambda x: x.shape[0] * x.shape[1])

# Create empty grid
width, height, _ = images[0].shape
grid = np.zeros((height * 4, width * 3, 3), dtype=np.uint8)

# Add images to the grid
for i, foto in enumerate(images):
    x = (i % 3) * width
    y = (i // 3) * height
    grid[y:y+height, x:x+width] = foto

# Save the final image - grid
cv2.imwrite("grid_final.jpg", grid)