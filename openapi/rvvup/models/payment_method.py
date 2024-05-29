from enum import Enum


class PaymentMethod(str, Enum):
    APPLE_PAY = "APPLE_PAY"
    CARD = "CARD"
    CLEARPAY = "CLEARPAY"
    CRYPTO = "CRYPTO"
    FAKE_PAYMENT_METHOD = "FAKE_PAYMENT_METHOD"
    PAYPAL = "PAYPAL"
    PAYPAL_CUSTOM_CARD = "PAYPAL_CUSTOM_CARD"
    PAY_BY_BANK = "PAY_BY_BANK"

    def __str__(self) -> str:
        return str(self.value)
