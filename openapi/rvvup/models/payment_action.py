from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from ..models.payment_action_type import PaymentActionType
from ..models.payment_action_method import PaymentActionMethod


T = TypeVar("T", bound="PaymentAction")


@_attrs_define
class PaymentAction:
    """The list of actions that can be performed on the payment.

    Attributes:
        method (PaymentActionMethod): The method of the payment action.
        type (PaymentActionType): The type of the payment action.
        value (str):
    """

    method: PaymentActionMethod
    type: PaymentActionType
    value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method.value

        type = self.type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "type": type,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = PaymentActionMethod(d.pop("method"))

        type = PaymentActionType(d.pop("type"))

        value = d.pop("value")

        payment_action = cls(
            method=method,
            type=type,
            value=value,
        )

        payment_action.additional_properties = d
        return payment_action

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
