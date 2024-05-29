from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.checkout_customer_field_type import CheckoutCustomerFieldType
from typing import Union


T = TypeVar("T", bound="CheckoutCustomerFieldsInput")


@_attrs_define
class CheckoutCustomerFieldsInput:
    """The customer fields that are required or optional for the checkout.
                     If a field is not required or optional, it will not be shown in the hosted checkout page.

    Attributes:
        optional (Union[Unset, List[CheckoutCustomerFieldType]]): The optional customer fields for the checkout.
        required (Union[Unset, List[CheckoutCustomerFieldType]]): The required customer fields for the checkout.
    """

    optional: Union[Unset, List[CheckoutCustomerFieldType]] = UNSET
    required: Union[Unset, List[CheckoutCustomerFieldType]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        optional: Union[Unset, List[str]] = UNSET
        if not isinstance(self.optional, Unset):
            optional = []
            for optional_item_data in self.optional:
                optional_item = optional_item_data.value
                optional.append(optional_item)

        required: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required, Unset):
            required = []
            for required_item_data in self.required:
                required_item = required_item_data.value
                required.append(required_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if optional is not UNSET:
            field_dict["optional"] = optional
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        optional = []
        _optional = d.pop("optional", UNSET)
        for optional_item_data in _optional or []:
            optional_item = CheckoutCustomerFieldType(optional_item_data)

            optional.append(optional_item)

        required = []
        _required = d.pop("required", UNSET)
        for required_item_data in _required or []:
            required_item = CheckoutCustomerFieldType(required_item_data)

            required.append(required_item)

        checkout_customer_fields_input = cls(
            optional=optional,
            required=required,
        )

        checkout_customer_fields_input.additional_properties = d
        return checkout_customer_fields_input

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
