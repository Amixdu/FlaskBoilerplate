from flask import Flask
from firebase_admin import credentials, initialize_app
from os import getenv
from dotenv import load_dotenv
from json import loads

load_dotenv()
firebase_key = loads(getenv("FIREBASE_KEY"))
# cred = credentials.Certificate("app/firebase-key.json")
cred = credentials.Certificate(firebase_key)
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)

    # import controller blueprints
    from .controllers.auth_controller import auth_bp
    from .controllers.user_controller import user_bp

    # register controller blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")

    return app

