import re
from marshmallow import ValidationError


def validate_document_id(value):
    # Check if the ID is not empty
    if not value.strip():
        raise ValidationError("Document ID cannot be empty")

    # Check for forbidden characters (slashes)
    if "/" in value:
        raise ValidationError("Document ID cannot contain slashes ('/')")

    # Check the length of the ID (UTF-8 encoded bytes)
    if len(value.encode("utf-8")) > 1500:
        raise ValidationError(
            "Document ID is too long (max 1500 bytes when UTF-8 encoded)"
        )

    # Check if the ID contains only valid characters
    if not re.match(r"^[A-Za-z0-9_-]+$", value):
        raise ValidationError("Document ID contains invalid characters")
