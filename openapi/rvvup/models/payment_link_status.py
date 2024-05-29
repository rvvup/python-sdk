from enum import Enum


class PaymentLinkStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
