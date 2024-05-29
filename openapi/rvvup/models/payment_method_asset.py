from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from ..models.payment_method_asset_type import PaymentMethodAssetType

if TYPE_CHECKING:
    from ..models.payment_method_asset_attributes import PaymentMethodAssetAttributes


T = TypeVar("T", bound="PaymentMethodAsset")


@_attrs_define
class PaymentMethodAsset:
    """Payment method assets object

    Attributes:
        asset_type (PaymentMethodAssetType): The type of the payment method asset.
        attributes (PaymentMethodAssetAttributes):
        url (str):
    """

    asset_type: PaymentMethodAssetType
    attributes: "PaymentMethodAssetAttributes"
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_type = self.asset_type.value

        attributes = self.attributes.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetType": asset_type,
                "attributes": attributes,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method_asset_attributes import (
            PaymentMethodAssetAttributes,
        )

        d = src_dict.copy()
        asset_type = PaymentMethodAssetType(d.pop("assetType"))

        attributes = PaymentMethodAssetAttributes.from_dict(d.pop("attributes"))

        url = d.pop("url")

        payment_method_asset = cls(
            asset_type=asset_type,
            attributes=attributes,
            url=url,
        )

        payment_method_asset.additional_properties = d
        return payment_method_asset

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
