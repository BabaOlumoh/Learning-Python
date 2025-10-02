import datetime
import os
import shutil

#Getting time for file name
getdate = datetime.datetime.now()
file_name = getdate.strftime("%Y%m%d__%H%M")

#File creation and error handling for folders
#PDF
pdf = os.path.join(os.getcwd(), "Downloads/PDFs")
try:
    os.makedirs(pdf, exist_ok = False)
    print("File created successfully")
except OSError as error:
    print("File already exist!")

#Images
images = os.path.join(os.getcwd(), "Downloads/Images")
try:
    os.makedirs(images, exist_ok = False)
    print("File created successfully")
except OSError as error:
    print("File already exist!")
    
#Videos
videos = os.path.join(os.getcwd(), "Downloads/Videos")
try:
    os.makedirs(videos, exist_ok = False)
    print("File created successfully")
except OSError as error:
    print("File already exist!")

#Documents
documents = os.path.join(os.getcwd(), "Downloads/Documents")
try:
    os.makedirs(documents, exist_ok = False)
    print("File created successfully")
except OSError as error:
    print("File already exist!")

#Zips
zips = os.path.join(os.getcwd(), "Downloads/Zips")
try:
    os.makedirs(zips, exist_ok = False)
    print("File created successfully")
except OSError as error:
    print("File already exist!")
    
#Others
others = os.path.join(os.getcwd(), "Downloads/Others")
try:
    os.makedirs(others, exist_ok = False)
    print("File created successfully")
except OSError as error:
    print("File already exist!")

#Moving files
downloads = os.path.join(os.getcwd(), "Downloads")

for file in os.listdir(downloads):
    source = os.path.join(downloads, file)
    if file.endswith((".mp4", ".mkv", ".mov")):
        source = os.path.join(downloads, file)
        destination = os.path.join(videos, file)
        shutil.move(source, destination)
        print(f"{file} moved to {os.path.basename(videos)}")
    elif file.endswith((".jpg", ".jpeg", ".png", ".gif")):
        source = os.path.join(downloads, file)
        destination = os.path.join(images, file)
        shutil.move(source, destination)
        print(f"{file} moved to {os.path.basename(images)}")
    elif file.endswith((".pdf")):
        source = os.path.join(downloads, file)
        destination = os.path.join(pdf, file)
        shutil.move(source, destination)
        print(f"{file} moved to {os.path.basename(pdf)}")
    elif file.endswith((".docx", ".txt", ".csv")):
        source = os.path.join(downloads, file)
        destination = os.path.join(documents, file)
        shutil.move(source, destination)
        print(f"{file} moved to {os.path.basename(documents)}")
    elif file.endswith((".zip", ".rar", ".7z")):
        source = os.path.join(downloads, file)
        destination = os.path.join(zips, file)
        shutil.move(source, destination)
        print(f"{file} moved to {os.path.basename(zips)}")
    elif os.path.isfile(source): #To ensure only a file is movedA
        destination = os.path.join(others, file)
        shutil.move(source, destination)
        print(f"{file} moved to {os.path.basename(others)}")
    else:
        print("No found moved!")