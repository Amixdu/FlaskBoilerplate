from firebase_admin import firestore
import uuid
import app.repositories.utils.queries as queries

db = firestore.client()
collection_ref = db.collection('locations')

def create_location(body):
    id = uuid.uuid4().hex
    body["id"] = id
    collection_ref.document(id).set(body)
    return body
    
def read_locations():
    query = collection_ref.stream()
    return queries.process_query(query)

def get_location_by_id(id):
    document_ref = collection_ref.document(id)
    document_snapshot = document_ref.get()
    if document_snapshot.exists:
        return document_snapshot.to_dict()
    else:
        return None  

def update_locations(id, body):
    document_ref = collection_ref.document(id)
    document_ref.update(body)
    return get_location_by_id(id)
