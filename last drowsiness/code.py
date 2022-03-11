#import the necessary libaries

import time

from datetime import datetime

#initialize firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



               
                dateTime= datetime.now()
                
              
                etat = dateTime -datetime.now()
                print(etat)


