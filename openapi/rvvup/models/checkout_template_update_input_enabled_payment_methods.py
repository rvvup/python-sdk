from enum import Enum


class CheckoutTemplateUpdateInputEnabledPaymentMethods(str, Enum):
    APPLE_PAY = "APPLE_PAY"
    CARD = "CARD"
    PAY_BY_BANK = "PAY_BY_BANK"

    def __str__(self) -> str:
        return str(self.value)
