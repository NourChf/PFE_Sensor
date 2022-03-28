import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('drawsiness').document('etat')

    doc_ref.set({
        'etat': name
    })