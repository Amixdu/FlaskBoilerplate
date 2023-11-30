from flask import jsonify
from flask import request, jsonify
from marshmallow import ValidationError


def validate_request(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                data = schema().load(request.json)
                request.body = data  # Replace the request data with the validated and converted data
            except ValidationError as err:
                return (
                    jsonify({"message": "Validation error", "errors": err.messages}),
                    400,
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator
