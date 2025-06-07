# This script organizes files into folders by type
import os
import shutil

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            ext = os.path.splitext(filename)[1][1:].lower()
            if not ext:
                continue
            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(ext_folder, filename))

if __name__ == "__main__":
    path = input("Enter folder path to clean: ")
    organize_folder(path)
    print("✅ Done organizing!")
