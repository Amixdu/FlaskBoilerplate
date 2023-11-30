from flask import Blueprint, request, jsonify
import app.services.user_service as user_service
import app.services.user_location_service as user_location_service
from app.middleware.verify_token import verify_token
from app.schemas.usser_location_schema import UserLocationSchema
from app.middleware.catch_error import catch_async_error
from app.middleware.request_validator import validate_request

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/", methods=["POST"])
@catch_async_error
# @verify_token
def create_user():
    """
    API for creating a new user
    """
    response = user_service.create_user(request.json)
    return jsonify(response)


@user_bp.route("/", methods=["GET"])
@catch_async_error
# @verify_token
def get():
    """
    API for fetching existing users
    """
    return "Users"


@user_bp.route("/<string:user_id>/locations", methods=["GET"])
@catch_async_error
# @verify_token
def get_user_locations(user_id):
    """
    API for fetching a given users locations (planned locations or favourite locations)
    """
    return "Get User Locations"


@user_bp.route("/<string:user_id>/locations", methods=["POST"])
@catch_async_error
@validate_request(UserLocationSchema)
# @verify_token
def create_user_location(user_id):
    """
    API for adding to a given user's locations (planned locations or favourite locations)
    """
    # TODO: Validate to ensure a given user can only update their own data, and not other users' data
    # Extract token from bearer

    # Decode token

    # Obtain email from token

    # Query the db using the email (unique) and fetch the full user record

    # Obtain the id from the user record

    # Obtain the id (user_id) in the path param of the url

    # If ids are equal, it indicates the user is trying to update their own data

    # Else, the user is trying to update a different user's data

    # This validation can only be bypassed if a malicious user gets hold of a different user's auth token
    
    response = user_location_service.create_user_location(user_id, request.body)
    return jsonify(response)
