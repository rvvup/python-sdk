from enum import Enum


class PaymentActionType(str, Enum):
    AUTHORIZATION = "AUTHORIZATION"
    CANCEL = "CANCEL"
    CAPTURE = "CAPTURE"
    CARD_3DS_AUTHENTICATION = "CARD_3DS_AUTHENTICATION"
    CONFIRM_AUTHORIZATION = "CONFIRM_AUTHORIZATION"

    def __str__(self) -> str:
        return str(self.value)
