from os import getenv
from dotenv import load_dotenv
from json import loads

load_dotenv()

ENV = {
    "FIREBASE_KEY": {
        "type": "service_account",
        "project_id": getenv("FIREBASE_PRIVATE_KEY_PROJECT_ID"),
        "private_key_id": getenv("FIREBASE_PRIVATE_KEY_PRIVATE_KEY_ID"),
        "private_key": getenv("FIREBASE_PRIVATE_KEY_PRIVATE_KEY"),
        "client_email": getenv("FIREBASE_PRIVATE_KEY_CLIENT_EMAIL"),
        "client_id": getenv("FIREBASE_PRIVATE_KEY_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": getenv("FIREBASE_PRIVATE_KEY_AUTH_PROVIDER_CERT_URL"),
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-avpx4%40dialog-inno-tourism.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com",
    },
    "GOOGLE_API_KEY": getenv("GOOGLE_API_KEY"),
}
