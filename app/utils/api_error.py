class ApiException(Exception):
    """
    Custom API Exception class to raise API errors
    """
    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code
