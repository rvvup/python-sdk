from enum import Enum


class CheckoutCustomerFieldType(str, Enum):
    BILLING_ADDRESS = "BILLING_ADDRESS"
    EMAIL = "EMAIL"
    GIVEN_NAME = "GIVEN_NAME"
    PHONE_NUMBER = "PHONE_NUMBER"
    SURNAME = "SURNAME"

    def __str__(self) -> str:
        return str(self.value)
