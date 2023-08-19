from flask import Blueprint
import app.services.auth_service as auth_service

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login')
def login():
    return auth_service.login()
