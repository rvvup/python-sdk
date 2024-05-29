from enum import Enum


class CheckoutStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
