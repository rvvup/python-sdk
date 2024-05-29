from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from ..models.money_input_currency import MoneyInputCurrency


T = TypeVar("T", bound="MoneyInput")


@_attrs_define
class MoneyInput:
    """
    Example:
        {'amount': '100.00', 'currency': 'GBP'}

    Attributes:
        amount (str): The amount as a string.
        currency (MoneyInputCurrency): The three-letter ISO-4217 currency code of the amount.
    """

    amount: str
    currency: MoneyInputCurrency
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        currency = MoneyInputCurrency(d.pop("currency"))

        money_input = cls(
            amount=amount,
            currency=currency,
        )

        money_input.additional_properties = d
        return money_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
