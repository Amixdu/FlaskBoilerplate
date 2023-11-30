import app.repositories.location_repository as location_repository
import app.services.geocoder_service as geocoder_service
import app.utils.objects as object_util
from app.utils.api_error import ApiException


def create_location(body):
    """
    Function for creating new locations. \n
    This function calls the geocoder API from OSM to obtain lattitude and longitude values. \n
    """
    reqLatitude = object_util.safe_get(body, "latitude", None)
    reqLongitude = object_util.safe_get(body, "longitude", None)

    # if req body doesnt have lattitude, use the one obtained via api (user input values is prioritized)
    if not reqLatitude:
        # obtain latitude via OSM
        latitude = geocoder_service.get_latitude(body["name"])

        # if no latitude found via OSM either, raise api error
        if not latitude:
            raise ApiException(400, "Latitude value is required")

        # if found, assign it to the body
        body["latitude"] = latitude

    # if req body doesnt have longitude, use the one obtained via api (user input values is prioritized)
    if not reqLongitude:
        # obtain longitude via OSM
        longitude = geocoder_service.get_longitude(body["name"])

        # if no latitude found via OSM either, raise api error
        if not longitude:
            raise ApiException(400, "Longitude value is required")

        # if found, assign it to the body
        body["longitude"] = longitude

    return location_repository.create_location(body)


def read_locations():
    """
    Function for fetching locations.
    """
    return location_repository.read_locations()


def update_location(id, body):
    """
    Function for updating a specified location.
    """
    # check if provided location exists, and if it doesn't return 404 error
    location = location_repository.get_location_by_id(id)
    if not location:
        raise ApiException(404, "Provided location not found")
    return location_repository.update_locations(id, body)


def get_location_by_id(id):
    """
    Function for obtaining a location by id.
    """
    return location_repository.get_location_by_id(id)
