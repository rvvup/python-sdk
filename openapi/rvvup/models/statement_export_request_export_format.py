from enum import Enum


class StatementExportRequestExportFormat(str, Enum):
    OFX_V2 = "OFX_V2"

    def __str__(self) -> str:
        return str(self.value)
