
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
db.collection('sensor').document('alcohol').set(
    {
        'value' : "nour"
    }
)
