from PIL import Image
import os

input_folder = "static/images"
output_folder = "static_compressed/images/"

os.makedirs(output_folder, exist_ok=True)

for root, _, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(root, file)
            img = Image.open(img_path)

            # Keep structure inside static folder
            relative_path = os.path.relpath(root, input_folder)
            output_dir = os.path.join(output_folder, relative_path)
            os.makedirs(output_dir, exist_ok=True)

            save_path = os.path.join(output_dir, file)

            # PNG — keep transparency
            if file.lower().endswith(".png"):
                img.save(save_path, optimize=True)
            else:
                # JPG — compress quality
                img.save(save_path, optimize=True, quality=75)

print("✅ Compression done! New files in: static_compressed/")
