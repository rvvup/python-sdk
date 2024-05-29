from enum import Enum


class MoneyInputCurrency(str, Enum):
    GBP = "GBP"

    def __str__(self) -> str:
        return str(self.value)
