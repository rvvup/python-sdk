from enum import Enum


class PaymentActionMethod(str, Enum):
    REDIRECT_URL = "REDIRECT_URL"
    TOKEN = "TOKEN"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
