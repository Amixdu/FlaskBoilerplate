from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validate,
    validates_schema,
)
from app.config.constants import (
    OPEN_SCHEDULE_VALIDATION_REGEX,
    USER_LOCATION_TYPES,
)
from app.schemas.custom_validations import validate_document_id
import app.utils.objects as object_util
import app.utils.date as date_util
from app.schemas.common_schema import CustomDateField


class UserLocationSchema(Schema):
    date = CustomDateField(required=False)
    startTime = fields.String(
        required=False,
        validate=validate.Regexp(
            OPEN_SCHEDULE_VALIDATION_REGEX, error="Invalid time format"
        ),
    )
    endTime = fields.String(
        required=False,
        validate=validate.Regexp(
            OPEN_SCHEDULE_VALIDATION_REGEX, error="Invalid time format"
        ),
    )
    type = fields.String(
        required=True, validate=validate.OneOf(list(USER_LOCATION_TYPES.values()))
    )
    locationId = fields.String(required=True, validate=validate_document_id)

    @validates_schema
    def validate_type(self, data, **kwargs):
        type = object_util.safe_get(data, "type")
        if type == USER_LOCATION_TYPES["PLANNED"]:
            # If type is USER_LOCATION_TYPES.PLANNED, date, startTime, and endTime are required.
            if "date" not in data:
                raise ValidationError("Date is required when type is planned")
            if "startTime" not in data:
                raise ValidationError("Start time is required when type is planned")
            if "endTime" not in data:
                raise ValidationError("End time is required when type is planned")
        else:
            # If type is not USER_LOCATION_TYPES.PLANNED, date, startTime, and endTime are forbidden.
            if "date" in data:
                raise ValidationError("Date is forbidden when type is not planned")
            if "startTime" in data:
                raise ValidationError(
                    "Start time is forbidden for when type is not planned"
                )
            if "endTime" in data:
                raise ValidationError(
                    "End time is forbidden for when type is not planned"
                )
