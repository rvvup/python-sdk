from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from dateutil.parser import isoparse
import datetime

if TYPE_CHECKING:
    from ..models.payment_method_total_limit import PaymentMethodTotalLimit


T = TypeVar("T", bound="PaymentMethodLimit")


@_attrs_define
class PaymentMethodLimit:
    """Payment method limits object. Contains expiration date and restrictions on the total for a currency.

    Attributes:
        expires_at (datetime.datetime):
        total (List['PaymentMethodTotalLimit']):
    """

    expires_at: datetime.datetime
    total: List["PaymentMethodTotalLimit"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        total = []
        for total_item_data in self.total:
            total_item = total_item_data.to_dict()
            total.append(total_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiresAt": expires_at,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method_total_limit import PaymentMethodTotalLimit

        d = src_dict.copy()
        expires_at = isoparse(d.pop("expiresAt"))

        total = []
        _total = d.pop("total")
        for total_item_data in _total:
            total_item = PaymentMethodTotalLimit.from_dict(total_item_data)

            total.append(total_item)

        payment_method_limit = cls(
            expires_at=expires_at,
            total=total,
        )

        payment_method_limit.additional_properties = d
        return payment_method_limit

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
