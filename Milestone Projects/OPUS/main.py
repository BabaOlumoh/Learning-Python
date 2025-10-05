import os
import shutil
import time

processing_dir = '/Users/homebase/Desktop/Python/Udemy Course/Milestone Projects/Daily-File-Organiser'
source = os.path.join(processing_dir)
destination = os.path.join(os.getcwd(), "Dest")

destination = os.path.join(os.getcwd(), "Dest")
for folder, sub_folders, files in os.walk(processing_dir):
    
    if os.path.basename(folder) not in ["Folder1", "Folder2"]: #ignore other folders except these
            continue
    for file in files:
        if file.endswith(".pdf"):
            source = os.path.join(folder, file)
            shutil.copy(source, destination)
            time.sleep(2)
        if file.endswith(".csv"):
            source = os.path.join(folder, file)
            shutil.copy(source, destination)
            time.sleep(10)

processing_folders = os.path.join(processing_dir, "Archive")
for folder in os.listdir(processing_dir):
    source = os.path.join(processing_dir, folder)
    if not folder in ["Folder1", "Folder2"]:
        continue
    shutil.move(source, processing_folders)

    