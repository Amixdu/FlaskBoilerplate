import requests
from app.utils.api_error import ApiException

def geocode_address(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    
    # set up the parameters for the API request
    params = {
        "q": address,
        "format": "json",
    }
    
    # send the HTTP request to the OpenStreetMap Nominatim API
    response = requests.get(base_url, params=params)
    
    # check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # check if the API returned any results
        if len(data) > 0:
            # return first value, if multiple matches found
            return data[0]
        else:
            return None
    else:
        raise ApiException(500, "Error retrieving lattitude and longitude values")
    
def get_latitude(address):
    data = geocode_address(address)
    # extract the latitude
    return float(data["lat"])

def get_longitude(address):
    data = geocode_address(address)
    # extract the longitude
    return float(data["lon"])
