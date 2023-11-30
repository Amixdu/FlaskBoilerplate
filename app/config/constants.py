from re import compile

SEASON_MONTHS = {
    "JAN": "january",
    "FEB": "february",
    "MAR": "march",
    "APR": "april",
    "MAY": "may",
    "JUN": "june",
    "JUL": "july",
    "AUG": "august",
    "SEP": "september",
    "OCT": "october",
    "NOV": "november",
    "DEC": "december",
}
ACTIVITES = {
    "ART": "Art",
    "BEACH": "Beach",
    "CULTURAL_SITE": "Cultural Site",
    "DIVE_BAR": "Dive Bar",
    "FOOD": "Food",
    "HIKE": "Hike",
    "NATURE": "Nature",
}
DAYS = {
    "MON": "monday",
    "TUE": "tuesday",
    "WED": "wednesday",
    "THU": "thursday",
    "FRI": "friday",
    "SAT": "saturday",
    "SUN": "sunday",
}
TICKET_TYPES = {
    "ADULT": "adult",
    "CHILD": "child",
}
URL_VALIDATION_REGEX = compile(
    r"^(https?://)?"  # Optional scheme (http/https)
    r"([a-zA-Z0-9.-]+)"  # Domain (may contain subdomains and periods)
    r"(\.[a-zA-Z]{2,})"  # Top-level domain (e.g., .com, .org)
    r"(/[\w.-]*)*"  # Optional path
    r"(\?[a-zA-Z0-9%&=._-]*)?"  # Optional query string
    r"(#.*)?$"  # Optional fragment identifier
)
OPEN_SCHEDULE_VALIDATION_REGEX = r"^\d{4}$"
USER_LOCATION_TYPES = {
    "PLANNED": "planned",
    "FAVOURITED": "favourited",
}