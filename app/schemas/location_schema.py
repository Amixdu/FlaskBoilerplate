from marshmallow import Schema, fields, validates, ValidationError, validate
from app.config.constants import (
    SEASON_MONTHS,
    URL_VALIDATION_REGEX,
    ACTIVITES,
    DAYS,
    OPEN_SCHEDULE_VALIDATION_REGEX,
    TICKET_TYPES,
)


class OpeningHoursSchema(Schema):
    open = fields.String(
        required=True,
        validate=validate.Regexp(
            OPEN_SCHEDULE_VALIDATION_REGEX, error="Invalid time format"
        ),
    )
    close = fields.String(
        required=True,
        validate=validate.Regexp(
            OPEN_SCHEDULE_VALIDATION_REGEX, error="Invalid time format"
        ),
    )


class PrinceRangeSchema(Schema):
    min = fields.Decimal(
        required=True, validate=validate.Range(0, error="Value must be greater than 0")
    )
    max = fields.Decimal(
        required=True, validate=validate.Range(0, error="Value must be greater than 0")
    )


class LocationSchema(Schema):
    name = fields.String(required=True)
    houseNumber = fields.String(required=True)
    street = fields.String(required=True)
    city = fields.String(required=True)
    province = fields.String(required=True)
    latitude = fields.Decimal(required=False)
    longitude = fields.Decimal(required=False)
    images = fields.List(fields.String(), required=False)

    @validates("images")
    def validate_images(self, value):
        for item in value:
            if not (bool(URL_VALIDATION_REGEX.match(item))):
                raise ValidationError(f'"{item}" is not a valid url.')

    seasons = fields.List(fields.String(), required=False)

    @validates("seasons")
    def validate_seasons(self, value):
        for item in value:
            if item not in list(SEASON_MONTHS.values()):
                raise ValidationError(f'"{item}" is not a valid season.')

    activites = fields.List(fields.String(), required=True)

    @validates("activites")
    def validate_activites(self, value):
        for item in value:
            if item not in list(ACTIVITES.values()):
                raise ValidationError(f'"{item}" is not a valid activity.')

    rating = fields.Decimal(required=False)
    openSchedule = fields.Dict(
        keys=fields.String(validate=validate.OneOf(list(DAYS.values()))),
        values=fields.Nested(OpeningHoursSchema, required=True),
    )

    @validates("openSchedule")
    def validate_open_schedule(self, value):
        for day, hours in value.items():
            # Ensure that 'open' is before 'close' for each day (auto converts to int)
            if hours["open"] >= hours["close"]:
                raise ValidationError(f"Invalid opening and closing times for {day}")

    description = fields.String(required=True)

    entryPricing = fields.Dict(
        keys=fields.String(validate=validate.OneOf(list(TICKET_TYPES.values()))),
        values=fields.Nested(PrinceRangeSchema, required=True),
    )

    @validates("entryPricing")
    def validate_open_schedule(self, value):
        for type, ranges in value.items():
            # Ensure that 'min' is lesser than 'max' for each entry type (auto converts to int)
            if ranges["min"] >= ranges["max"]:
                raise ValidationError(f"Invalid min and max prices for {type}")
