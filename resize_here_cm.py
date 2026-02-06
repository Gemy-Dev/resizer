import os
import sys
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

# Use exe directory when run as PyInstaller bundle, else script directory
if getattr(sys, "frozen", False):
    current_folder = os.path.dirname(sys.executable)
else:
    current_folder = os.path.dirname(os.path.abspath(__file__))

# Output folder
output_folder = os.path.join(current_folder, "output")
os.makedirs(output_folder, exist_ok=True)

# Supported extensions
formats = (".jpg", ".jpeg", ".png", ".tiff", ".bmp")

count = 0

# Skip the executable itself when running as .exe
exe_name = os.path.basename(sys.executable) if getattr(sys, "frozen", False) else ""

for file in os.listdir(current_folder):

    # Skip output folder, this script, and the exe
    if file == "output" or file == exe_name:
        continue

    if file.lower().endswith(formats):

        img_path = os.path.join(current_folder, file)
        img = Image.open(img_path)

        # Resize to exact dimensions (preserves aspect ratio, adds letterboxing if needed)
        img = img.resize((width_px, height_px), Image.LANCZOS)

        # Save the new version
        output_path = os.path.join(output_folder, file)
        img.save(output_path, dpi=(dpi, dpi), quality=95)

        count += 1
        print(f"Processed: {file}")

print(f"\nDone ✅ Processed {count} image(s)")
