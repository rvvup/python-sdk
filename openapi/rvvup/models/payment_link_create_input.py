from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.application_source import ApplicationSource
from typing import Union

if TYPE_CHECKING:
    from ..models.money_input import MoneyInput


T = TypeVar("T", bound="PaymentLinkCreateInput")


@_attrs_define
class PaymentLinkCreateInput:
    """The input for creating a payment link.

    Attributes:
        amount (Union[Unset, MoneyInput]):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        checkout_template_id (Union[Unset, str]): The ID of the checkout template to use for this payment link.
                                     If not provided, the default template will be used.
                                     If provided, the template must be available to the merchant.
        reference (Union[Unset, str]): Your reference to identify the payment link and subsequently created checkouts
                                     and payment sessions. Example: INVOICE-12345.
        reusable (Union[Unset, bool]): Whether the payment link can be reused for multiple payments. Default: False.
        source (Union[Unset, ApplicationSource]): The source of the application.
    """

    amount: Union[Unset, "MoneyInput"] = UNSET
    checkout_template_id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    reusable: Union[Unset, bool] = False
    source: Union[Unset, ApplicationSource] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        checkout_template_id = self.checkout_template_id

        reference = self.reference

        reusable = self.reusable

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if checkout_template_id is not UNSET:
            field_dict["checkoutTemplateId"] = checkout_template_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reusable is not UNSET:
            field_dict["reusable"] = reusable
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_input import MoneyInput

        d = src_dict.copy()
        _amount = d.pop("amount", UNSET)
        amount: Union[Unset, MoneyInput]
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = MoneyInput.from_dict(_amount)

        checkout_template_id = d.pop("checkoutTemplateId", UNSET)

        reference = d.pop("reference", UNSET)

        reusable = d.pop("reusable", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ApplicationSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ApplicationSource(_source)

        payment_link_create_input = cls(
            amount=amount,
            checkout_template_id=checkout_template_id,
            reference=reference,
            reusable=reusable,
            source=source,
        )

        payment_link_create_input.additional_properties = d
        return payment_link_create_input

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
