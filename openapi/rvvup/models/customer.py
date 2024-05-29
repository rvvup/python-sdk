from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        email (Union[Unset, str]): The customer's email address.
        given_name (Union[Unset, str]): The customer's given name.
        phone_number (Union[Unset, str]): The customer's phone number.
        surname (Union[Unset, str]): The customer's surname.
    """

    email: Union[Unset, str] = UNSET
    given_name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        given_name = self.given_name

        phone_number = self.phone_number

        surname = self.surname

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if surname is not UNSET:
            field_dict["surname"] = surname

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        given_name = d.pop("givenName", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        surname = d.pop("surname", UNSET)

        customer = cls(
            email=email,
            given_name=given_name,
            phone_number=phone_number,
            surname=surname,
        )

        customer.additional_properties = d
        return customer

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
