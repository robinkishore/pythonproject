import os
import shutil

source_folder=r"D:\organizer"
destination_folder="D:\organizer"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
files = os.listdir(source_folder)
files_by_format = {}
for file in files:
    source_path = os.path.join(source_folder,file)
    if os.path.isfile(source_path):
        file_name,file_extension = os.path.splitext(file)
        format_folder = os.path.join(destination_folder,file_extension[1:])
        if not os.path.exists(format_folder):
            os.makedirs(format_folder)
            destination_path = os.path.join(format_folder,file)
            shutil.move(source_path,destination_path)
            print(f"file {file} moved to {format_folder}")
print("file organization completed")








