from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="PaymentMethodTotalLimit")


@_attrs_define
class PaymentMethodTotalLimit:
    """Payment method total limit object. Contains min and max limits for a currency.

    Attributes:
        currency (str):
        max_ (str):
        min_ (str):
    """

    currency: str
    max_: str
    min_: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        max_ = self.max_

        min_ = self.min_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "max": max_,
                "min": min_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency")

        max_ = d.pop("max")

        min_ = d.pop("min")

        payment_method_total_limit = cls(
            currency=currency,
            max_=max_,
            min_=min_,
        )

        payment_method_total_limit.additional_properties = d
        return payment_method_total_limit

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
