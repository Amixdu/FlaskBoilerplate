def safe_get(obj, key, default=None):
    """
    Function to safely get values from python objects
    """
    try:
        return obj[key]
    except (KeyError, TypeError, AttributeError):
        return default
