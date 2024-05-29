from enum import Enum


class CheckoutAmountType(str, Enum):
    EDITABLE = "EDITABLE"
    FIXED = "FIXED"

    def __str__(self) -> str:
        return str(self.value)
