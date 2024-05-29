from enum import Enum


class PaymentCaptureType(str, Enum):
    AUTOMATIC_CHECKOUT = "AUTOMATIC_CHECKOUT"
    AUTOMATIC_PLUGIN = "AUTOMATIC_PLUGIN"
    MANUAL = "MANUAL"

    def __str__(self) -> str:
        return str(self.value)
