import os
from PIL import Image

print("=== Resize images by cm without cropping ===\n")

# ===== Input dimensions =====
width_cm = float(input("Enter width in cm: "))
height_cm = float(input("Enter height in cm: "))
dpi = int(input("Enter DPI (e.g. 300): "))

# Convert cm → pixels
inch_per_cm = 0.393701
width_px = int(width_cm * inch_per_cm * dpi)
height_px = int(height_cm * inch_per_cm * dpi)

# Script's directory
current_folder = os.path.dirname(os.path.abspath(__file__))

# Output folder
output_folder = os.path.join(current_folder, "output")
os.makedirs(output_folder, exist_ok=True)

# Supported extensions
formats = (".jpg", ".jpeg", ".png", ".tiff", ".bmp")

count = 0

for file in os.listdir(current_folder):

    # Skip output folder and this script
    if file == "output":
        continue

    if file.lower().endswith(formats):

        img_path = os.path.join(current_folder, file)
        img = Image.open(img_path)

        # Preserve aspect ratio without cropping
        img.thumbnail((width_px, height_px), Image.LANCZOS)

        # Save the new version
        output_path = os.path.join(output_folder, file)
        img.save(output_path, dpi=(dpi, dpi), quality=95)

        count += 1
        print(f"Processed: {file}")

print(f"\nDone ✅ Processed {count} image(s)")
