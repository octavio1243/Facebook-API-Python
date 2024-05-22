from enum import Enum

class CredentialsType(Enum):
    LOGIN = "device_based_login_password"
    TWO_FACTOR = "two_factor"
    PASSWORD = "password"
