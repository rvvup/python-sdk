from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_capture_type import PaymentCaptureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_customer_fields_update_input import (
        CheckoutCustomerFieldsUpdateInput,
    )


T = TypeVar("T", bound="CheckoutCardSettingsUpdateInput")


@_attrs_define
class CheckoutCardSettingsUpdateInput:
    """The Card settings to be used for the checkout.

    Attributes:
        capture_type (Union[Unset, PaymentCaptureType]): The capture type for the payment.
        customer_fields (Union[Unset, CheckoutCustomerFieldsUpdateInput]): The customer fields that are required or
            optional for the checkout.
                                 If a field is not required or optional, it will not be shown in the hosted checkout page.
    """

    capture_type: Union[Unset, PaymentCaptureType] = UNSET
    customer_fields: Union[Unset, "CheckoutCustomerFieldsUpdateInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capture_type: Union[Unset, str] = UNSET
        if not isinstance(self.capture_type, Unset):
            capture_type = self.capture_type.value

        customer_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_fields, Unset):
            customer_fields = self.customer_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capture_type is not UNSET:
            field_dict["captureType"] = capture_type
        if customer_fields is not UNSET:
            field_dict["customerFields"] = customer_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_customer_fields_update_input import (
            CheckoutCustomerFieldsUpdateInput,
        )

        d = src_dict.copy()
        _capture_type = d.pop("captureType", UNSET)
        capture_type: Union[Unset, PaymentCaptureType]
        if isinstance(_capture_type, Unset):
            capture_type = UNSET
        else:
            capture_type = PaymentCaptureType(_capture_type)

        _customer_fields = d.pop("customerFields", UNSET)
        customer_fields: Union[Unset, CheckoutCustomerFieldsUpdateInput]
        if isinstance(_customer_fields, Unset):
            customer_fields = UNSET
        else:
            customer_fields = CheckoutCustomerFieldsUpdateInput.from_dict(
                _customer_fields
            )

        checkout_card_settings_update_input = cls(
            capture_type=capture_type,
            customer_fields=customer_fields,
        )

        checkout_card_settings_update_input.additional_properties = d
        return checkout_card_settings_update_input

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
