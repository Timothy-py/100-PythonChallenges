# Define a custom exception class which takes a string message as attribute.

class Xception(Exception):
    """My custom exception class
    Attributes:
    message =  something went wrong
    """

    def __init__(self, message):
        self.message = message
