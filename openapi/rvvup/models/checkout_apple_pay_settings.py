from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_capture_type import PaymentCaptureType
from typing import Union

if TYPE_CHECKING:
    from ..models.checkout_customer_fields import CheckoutCustomerFields


T = TypeVar("T", bound="CheckoutApplePaySettings")


@_attrs_define
class CheckoutApplePaySettings:
    """The Apple Pay settings to be used for the checkout.

    Attributes:
        capture_type (Union[Unset, PaymentCaptureType]): The capture type for the payment.
        customer_fields (Union[Unset, CheckoutCustomerFields]):
    """

    capture_type: Union[Unset, PaymentCaptureType] = UNSET
    customer_fields: Union[Unset, "CheckoutCustomerFields"] = UNSET
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
        from ..models.checkout_customer_fields import CheckoutCustomerFields

        d = src_dict.copy()
        _capture_type = d.pop("captureType", UNSET)
        capture_type: Union[Unset, PaymentCaptureType]
        if isinstance(_capture_type, Unset):
            capture_type = UNSET
        else:
            capture_type = PaymentCaptureType(_capture_type)

        _customer_fields = d.pop("customerFields", UNSET)
        customer_fields: Union[Unset, CheckoutCustomerFields]
        if isinstance(_customer_fields, Unset):
            customer_fields = UNSET
        else:
            customer_fields = CheckoutCustomerFields.from_dict(_customer_fields)

        checkout_apple_pay_settings = cls(
            capture_type=capture_type,
            customer_fields=customer_fields,
        )

        checkout_apple_pay_settings.additional_properties = d
        return checkout_apple_pay_settings

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
