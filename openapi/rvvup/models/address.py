from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        city (str): City.
        country_code (str): Two letter ISO 3166-1 alpha-2 country code.
        line1 (str): Address line 1.
        name (str): Name.
        postcode (str): Postcode.
        company (Union[Unset, str]): Company name.
        line2 (Union[Unset, str]): Address line 2.
        phone_number (Union[Unset, str]): Phone number.
        state (Union[Unset, str]): State.
    """

    city: str
    country_code: str
    line1: str
    name: str
    postcode: str
    company: Union[Unset, str] = UNSET
    line2: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        city = self.city

        country_code = self.country_code

        line1 = self.line1

        name = self.name

        postcode = self.postcode

        company = self.company

        line2 = self.line2

        phone_number = self.phone_number

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "countryCode": country_code,
                "line1": line1,
                "name": name,
                "postcode": postcode,
            }
        )
        if company is not UNSET:
            field_dict["company"] = company
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        city = d.pop("city")

        country_code = d.pop("countryCode")

        line1 = d.pop("line1")

        name = d.pop("name")

        postcode = d.pop("postcode")

        company = d.pop("company", UNSET)

        line2 = d.pop("line2", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        state = d.pop("state", UNSET)

        address = cls(
            city=city,
            country_code=country_code,
            line1=line1,
            name=name,
            postcode=postcode,
            company=company,
            line2=line2,
            phone_number=phone_number,
            state=state,
        )

        address.additional_properties = d
        return address

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
