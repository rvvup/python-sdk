from enum import Enum


class PaymentVoidReason(str, Enum):
    CUSTOMER_REQUEST = "CUSTOMER_REQUEST"
    INVALID_DATA = "INVALID_DATA"
    MERCHANT_REQUEST = "MERCHANT_REQUEST"
    STOCK_ISSUES = "STOCK_ISSUES"
    SUSPECTED_FRAUD = "SUSPECTED_FRAUD"

    def __str__(self) -> str:
        return str(self.value)
