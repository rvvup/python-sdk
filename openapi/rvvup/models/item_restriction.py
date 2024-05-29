from enum import Enum


class ItemRestriction(str, Enum):
    ALLOWED = "ALLOWED"
    PROHIBITED = "PROHIBITED"
    RESTRICTED = "RESTRICTED"

    def __str__(self) -> str:
        return str(self.value)
