from enum import Enum


class ApplicationSource(str, Enum):
    API = "API"
    DASHBOARD_MOTO = "DASHBOARD_MOTO"
    DASHBOARD_PAYMENT_LINK = "DASHBOARD_PAYMENT_LINK"
    MAGENTO_MOTO = "MAGENTO_MOTO"
    MAGENTO_PAYMENT_LINK = "MAGENTO_PAYMENT_LINK"
    MOTO = "MOTO"
    PAY_NOW_IN_PERSON = "PAY_NOW_IN_PERSON"
    PAY_NOW_MOTO = "PAY_NOW_MOTO"
    PAY_NOW_PAYMENT_LINK = "PAY_NOW_PAYMENT_LINK"
    XERO = "XERO"

    def __str__(self) -> str:
        return str(self.value)
