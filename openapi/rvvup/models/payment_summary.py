from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.money import Money
    from ..models.payment_action import PaymentAction


T = TypeVar("T", bound="PaymentSummary")


@_attrs_define
class PaymentSummary:
    """
    Attributes:
        is_manually_capturable (bool): Whether the payment can be captured manually later.
        is_refundable (bool): Whether the payment is refundable.
        is_voidable (bool): Whether the payment is voidable.
        payment_actions (List['PaymentAction']): The list of actions that can be performed on the payment.
        refundable_amount (Money):
    """

    is_manually_capturable: bool
    is_refundable: bool
    is_voidable: bool
    payment_actions: List["PaymentAction"]
    refundable_amount: "Money"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_manually_capturable = self.is_manually_capturable

        is_refundable = self.is_refundable

        is_voidable = self.is_voidable

        payment_actions = []
        for payment_actions_item_data in self.payment_actions:
            payment_actions_item = payment_actions_item_data.to_dict()
            payment_actions.append(payment_actions_item)

        refundable_amount = self.refundable_amount.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isManuallyCapturable": is_manually_capturable,
                "isRefundable": is_refundable,
                "isVoidable": is_voidable,
                "paymentActions": payment_actions,
                "refundableAmount": refundable_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money
        from ..models.payment_action import PaymentAction

        d = src_dict.copy()
        is_manually_capturable = d.pop("isManuallyCapturable")

        is_refundable = d.pop("isRefundable")

        is_voidable = d.pop("isVoidable")

        payment_actions = []
        _payment_actions = d.pop("paymentActions")
        for payment_actions_item_data in _payment_actions:
            payment_actions_item = PaymentAction.from_dict(payment_actions_item_data)

            payment_actions.append(payment_actions_item)

        refundable_amount = Money.from_dict(d.pop("refundableAmount"))

        payment_summary = cls(
            is_manually_capturable=is_manually_capturable,
            is_refundable=is_refundable,
            is_voidable=is_voidable,
            payment_actions=payment_actions,
            refundable_amount=refundable_amount,
        )

        payment_summary.additional_properties = d
        return payment_summary

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
