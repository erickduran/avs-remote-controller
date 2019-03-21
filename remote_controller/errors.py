# errors.py
"""This is the definition class for all errors in the controller."""


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidCommandError(Error):
    """Exception raised for errors invalid commands.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class InvalidArgumentError(Error):
    """Exception raised for errors invalid arguments.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class InvalidCompositeCommandError(Error):
    """Exception raised for errors invalid composite commands configuration.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class FileNotLoadedError(Error):
    """Exception raised when a file is not loaded.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
