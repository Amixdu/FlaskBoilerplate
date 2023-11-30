from marshmallow import ValidationError, fields
from datetime import datetime
import app.utils.date as date_util


class CustomDateField(fields.Field):
    def _deserialize(self, value, attr, obj):
        if not value:
            return None
        try:
            # Parse the date string into a Date object
            if isinstance(value, str):
                return date_util.parse_date(value)
            elif isinstance(value, datetime.date):
                # If it's already a date, return it as is
                return value
            else:
                raise ValidationError("Invalid date format")
        except ValueError:
            raise ValidationError("Invalid date format")
