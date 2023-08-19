from firebase_admin import firestore
import uuid

db = firestore.client()
user_ref = db.collection('user')

def create_user(body):
    try:
      id = body.pop("id")
      user_ref.document(id).set(body)
      return body
    except Exception as e: 
       return f"Internal server error: {e}"
    
