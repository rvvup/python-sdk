from enum import Enum


class PaymentStatus(str, Enum):
    AUTHORIZATION_EXPIRED = "AUTHORIZATION_EXPIRED"
    AUTHORIZED = "AUTHORIZED"
    CANCELLED = "CANCELLED"
    CREATED = "CREATED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    REQUIRES_ACTION = "REQUIRES_ACTION"
    SUCCEEDED = "SUCCEEDED"
    VOIDED = "VOIDED"

    def __str__(self) -> str:
        return str(self.value)
