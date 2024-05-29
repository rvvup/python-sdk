from enum import Enum


class PaymentSessionStatus(str, Enum):
    CANCELLED = "CANCELLED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"
    PENDING = "PENDING"
    REQUIRES_ACTION = "REQUIRES_ACTION"
    REQUIRES_PAYMENT = "REQUIRES_PAYMENT"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
