import datetime
import os
import shutil

#Getting time for file name
get_date = datetime.datetime.now().strftime("%Y%m%d_%H%M")

#File creation and error handling for folders
#PDF Folder
pdf = os.path.join(os.getcwd(), "Downloads/PDFs")
try:
    os.makedirs(pdf, exist_ok = False)
    print(f"{os.path.basename(pdf)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(pdf)} folder already exist!")

#Images Folder
images = os.path.join(os.getcwd(), "Downloads/Images")
try:
    os.makedirs(images, exist_ok = False)
    print(f"{os.path.basename(images)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(images)} folder already exist!")
    
#Videos Folder
videos = os.path.join(os.getcwd(), "Downloads/Videos")
try:
    os.makedirs(videos, exist_ok = False)
    print(f"{os.path.basename(videos)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(videos)} folder already exist!")

#Documents Folder
documents = os.path.join(os.getcwd(), "Downloads/Documents")
try:
    os.makedirs(documents, exist_ok = False)
    print(f"{os.path.basename(documents)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(documents)} folder already exist!")

#Zip Folder
zips = os.path.join(os.getcwd(), "Downloads/Zips")
try:
    os.makedirs(zips, exist_ok = False)
    print(f"{os.path.basename(zips)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(zips)} folder already exist!")

#Others Folder
others = os.path.join(os.getcwd(), "Downloads/Others")
try:
    os.makedirs(others, exist_ok = False)
    print(f"{os.path.basename(others)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(others)} folder already exist!")

#Log Folder
log = os.path.join(os.getcwd(), "Log")
try:
    os.makedirs(log, exist_ok = False)
    print(f"{os.path.basename(log)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(log)} folder already exist!")

#Backup Folder
backup = os.path.join(os.getcwd(), "Backup")
try:
    os.makedirs(backup, exist_ok = False)
    print(f"{os.path.basename(backup)} folder created successfully")
except OSError as error:
    print(f"{os.path.basename(backup)} folder already exist!")

#Moving files
downloads = os.path.join(os.getcwd(), "Downloads")
with open(f"Log/{get_date}logfile", "a") as f:
    for file in os.listdir(downloads):
        source = os.path.join(downloads, file)

        #To ensure only a file is moved
        if not os.path.isfile(source):
            continue
            
        if file.endswith((".mp4", ".mkv", ".mov")):
            destination = os.path.join(videos, file)
            shutil.move(source, destination)
            f.write(f"{file} moved to {os.path.basename(videos)} on {get_date}\n")
        elif file.endswith((".jpg", ".jpeg", ".png", ".gif")):
            destination = os.path.join(images, file)
            shutil.move(source, destination)
            f.write(f"{file} moved to {os.path.basename(images)} on {get_date}\n")
        elif file.endswith((".pdf")):
            destination = os.path.join(pdf, file)
            shutil.move(source, destination)
            f.write(f"{file} moved to {os.path.basename(pdf)} on {get_date}\n")
        elif file.endswith((".docx", ".txt", ".csv")):      
            destination = os.path.join(documents, file)
            shutil.move(source, destination)
            f.write(f"{file} moved to {os.path.basename(documents)} on {get_date}\n")
        elif file.endswith((".zip", ".rar", ".7z")):    
            destination = os.path.join(zips, file)
            shutil.move(source, destination)
            f.write(f"{file} moved to {os.path.basename(zips)}  on {get_date}\n")
        else: 
            destination = os.path.join(others, file)
            shutil.move(source, destination)
            f.write(f"{file} moved to {os.path.basename(others)}  on {get_date}\n")

#Backup
with open(f"Log/Backup_{get_date}", "a") as f:
    for folder in os.listdir(downloads):
        source = os.path.join(downloads, folder)
        destination = os.path.join(backup, folder)
        if os.path.isfile(source):
            continue
        if folder in ["PDFs", "Images", "Videos", "Documents", "Zips", "Others"]:
            continue
        try:
            shutil.copytree(source, destination)
            f.write(f"{folder} back up on {get_date}\n")
        except:
            print(f"{folder} exists, skipped")       

print("\n✅ File organization and backup completed!")
print(f"📁 Log saved in Log/{get_date}_logfile.txt")