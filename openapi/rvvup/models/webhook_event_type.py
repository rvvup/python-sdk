from enum import Enum


class WebhookEventType(str, Enum):
    PAYMENT_AUTHORIZED = "PAYMENT_AUTHORIZED"
    PAYMENT_COMPLETED = "PAYMENT_COMPLETED"
    PAYMENT_SUCCEEDED = "PAYMENT_SUCCEEDED"
    REFUND_COMPLETED = "REFUND_COMPLETED"
    REFUND_SUCCEEDED = "REFUND_SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
