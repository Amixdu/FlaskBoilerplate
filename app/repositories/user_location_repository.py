from firebase_admin import firestore
import uuid

db = firestore.client()
collection_ref = db.collection("userlocations")


def create_user_location(body):
    id = uuid.uuid4().hex
    collection_ref.document(id).set(body)
    return body
