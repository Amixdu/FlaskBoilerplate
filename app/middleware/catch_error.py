from functools import wraps
from flask import jsonify
from app.utils.api_error import ApiException

def catch_async_error(func):
    """
    Function for catching errors in the entire backend and handling them appropriately
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            return jsonify({"error": str(e)}), e.status_code  # Return a JSON response with the custom ApiException status code
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Return a JSON response with a 500 status code for unhandled errors

    return wrapper
