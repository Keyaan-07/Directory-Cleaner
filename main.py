import os
import shutil

directory_path = input("Enter the path of the directory to clean: ").strip()

if not os.path.exists(directory_path):
    print(f"The directory {directory_path} does not exist.")
else:
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1][1:]
            folder_name = file_extension if file_extension else "Unknown"
            folder_path = os.path.join(directory_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(item_path, os.path.join(folder_path, item))

    print("Directory cleaning and sorting complete.")
