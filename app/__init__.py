from flask import Flask
from firebase_admin import credentials, initialize_app
import app.config.config as config

from app.services.geocoder_service import geocode_address

firebase_key = config.ENV["FIREBASE_KEY"]
cred = credentials.Certificate(firebase_key)
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)

    # import controller blueprints
    from .controllers.auth_controller import auth_bp
    from .controllers.user_controller import user_bp
    from .controllers.location_controller import location_bp

    # register controller blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(location_bp, url_prefix="/locations")

    return app

