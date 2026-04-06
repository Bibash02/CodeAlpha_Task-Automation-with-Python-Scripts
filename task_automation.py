import os
import shutil

source_folder = "source_images"
destination_folder = "jpg_images"

# create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# loop through all files in the source folder
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        src_path = os.path.join(source_folder, file)
        dst_path = os.path.join(destination_folder, file)

        shutil.move(src_path, dst_path)
        print(f"Moved: {file}")

print("All .jpg files have been moved to the destination folder.")
