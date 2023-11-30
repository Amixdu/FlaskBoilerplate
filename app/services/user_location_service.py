import app.repositories.user_location_repository as user_location_repository
import app.services.user_service as user_service
import app.services.location_service as location_service
from app.utils.api_error import ApiException


def create_user_location(user_id, body):
    # if provided user doesnt exist, raise an error
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise ApiException(400, "Provided user not found")
    # if provided location doesnt exist, throw an error
    location = location_service.get_location_by_id(body["locationId"])
    if not location:
        raise ApiException(400, "Provided location not found")
    body["userId"] = user_id
    try:
        return user_location_repository.create_user_location(body)
    except Exception as e:
        return f"Internal server error: {e}"
