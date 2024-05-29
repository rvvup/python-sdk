from enum import Enum


class PaymentSettlementStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    FUNDS_RECEIVED = "FUNDS_RECEIVED"
    NOT_INITIATED = "NOT_INITIATED"
    SETTLED = "SETTLED"
    SETTLED_EXTERNALLY = "SETTLED_EXTERNALLY"

    def __str__(self) -> str:
        return str(self.value)
