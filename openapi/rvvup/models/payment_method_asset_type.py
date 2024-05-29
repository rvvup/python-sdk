from enum import Enum


class PaymentMethodAssetType(str, Enum):
    SCRIPT = "SCRIPT"

    def __str__(self) -> str:
        return str(self.value)
