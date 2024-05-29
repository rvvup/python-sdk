from enum import Enum


class PaymentMethodStatus(str, Enum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    SUSPENDED = "SUSPENDED"
    UNAVAILABLE = "UNAVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
