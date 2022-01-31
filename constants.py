from enum import Enum


class Status(str, Enum):
    SUCCESS = "Success"
    ERROR = "Error"


class InvalidData(str, Enum):
    INVALID = "Invalid data"
    NO_FILE = "No such file"
