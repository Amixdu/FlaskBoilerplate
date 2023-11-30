from datetime import datetime


def parse_date(date_str):
    try:
        # Parse the date string into a datetime object
        parsed_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        # Convert the datetime object to ISO format
        return parsed_datetime.isoformat()
    except ValueError:
        raise ValueError("Invalid date format")
