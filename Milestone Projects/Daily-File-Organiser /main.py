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

#Others
others = os.path.join(os.getcwd(), "Downloads/Others")
try:
    os.makedirs(others, exist_ok = False)
    print("File created successfully")
except OSError as error:
    print("File already exist!")

