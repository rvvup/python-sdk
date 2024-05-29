from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.payment_method_asset import PaymentMethodAsset


T = TypeVar("T", bound="PaymentMethodSettings")


@_attrs_define
class PaymentMethodSettings:
    """Payment method settings object

    Attributes:
        assets (List['PaymentMethodAsset']):
        description (str):
        display_name (str):
    """

    assets: List["PaymentMethodAsset"]
    description: str
    display_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        description = self.description

        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assets": assets,
                "description": description,
                "displayName": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method_asset import PaymentMethodAsset

        d = src_dict.copy()
        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = PaymentMethodAsset.from_dict(assets_item_data)

            assets.append(assets_item)

        description = d.pop("description")

        display_name = d.pop("displayName")

        payment_method_settings = cls(
            assets=assets,
            description=description,
            display_name=display_name,
        )

        payment_method_settings.additional_properties = d
        return payment_method_settings

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
