from firebase_admin import firestore

db = firestore.client()
collection_ref = db.collection("users")


def create_user(body):
    id = body["id"]
    collection_ref.document(id).set(body)
    return body


def get_user_by_id(id):
    document_ref = collection_ref.document(id)
    document_snapshot = document_ref.get()
    if document_snapshot.exists:
        return document_snapshot.to_dict()
    else:
        return None
