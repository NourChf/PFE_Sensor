#-------------------------------------------------------------------------------
# Imports
import pyrebase
import os

#-------------------------------------------------------------------------------
# Variables & Setup

filelist = [ f for f in os.listdir(".") if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(".", f))

config = {
"apiKey": "AIzaSyA2L-06VNcQlqvCbTGRd0BtTexZB671NVI",
"authDomain": "stage-eedc0.firebaseapp.com",
"databaseURL": "https://stage-eedc0-default-rtdb.firebaseio.com",
"projectId": "stage-eedc0",
"storageBucket": "stage-eedc0.appspot.com",
"serviceAccount": "serviceAccountKey.json"
}

firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()

#-------------------------------------------------------------------------------
# Uploading And Downloading Images

#storage.child("nour.jpg").put("nour.jpg")
storage.child("nour.jpg").download("nour.jpg")

all_files = storage.list_files()

for file in all_files:
    print(file.name)
    file.download_to_filename(file.name)
