from flask import Blueprint, request, jsonify
import app.services.location_service as location_service
from app.middleware.verify_token import verify_token
from app.middleware.catch_error import catch_async_error
from app.schemas.location_schema import LocationSchema
from app.middleware.request_validator import validate_request

location_bp = Blueprint("location_bp", __name__)


@location_bp.route("/", methods=["POST"])
@catch_async_error
@validate_request(LocationSchema)
# @verify_token
def create_location():
    """
    API for adding a new location
    """
    response = location_service.create_location(request.json)
    return jsonify(response)


@location_bp.route("/", methods=["GET"])
@catch_async_error
# @verify_token
def read_locations():
    """
    API for retrieving available locations
    """
    response = location_service.read_locations()
    return jsonify(response)


@location_bp.route("/<string:location_id>", methods=["PATCH"])
@catch_async_error
# @verify_token
def update_location(location_id):
    """
    API for updating a specific location
    """
    response = location_service.update_location(location_id, request.json)
    return jsonify(response)
