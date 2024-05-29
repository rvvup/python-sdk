from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_method import PaymentMethod
from ..models.payment_method_status import PaymentMethodStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_method_limit import PaymentMethodLimit
    from ..models.payment_method_settings import PaymentMethodSettings


T = TypeVar("T", bound="PaymentMethodDetail")


@_attrs_define
class PaymentMethodDetail:
    """Payment method object

    Attributes:
        logo_url (str):
        name (PaymentMethod): The payment method.
        settings (PaymentMethodSettings): Payment method settings object
        status (PaymentMethodStatus): The status of the payment method.
        summary_url (str):
        limits (Union[Unset, PaymentMethodLimit]): Payment method limits object. Contains expiration date and
            restrictions on the total for a currency.
    """

    logo_url: str
    name: PaymentMethod
    settings: "PaymentMethodSettings"
    status: PaymentMethodStatus
    summary_url: str
    limits: Union[Unset, "PaymentMethodLimit"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logo_url = self.logo_url

        name = self.name.value

        settings = self.settings.to_dict()

        status = self.status.value

        summary_url = self.summary_url

        limits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logoUrl": logo_url,
                "name": name,
                "settings": settings,
                "status": status,
                "summaryUrl": summary_url,
            }
        )
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method_limit import PaymentMethodLimit
        from ..models.payment_method_settings import PaymentMethodSettings

        d = src_dict.copy()
        logo_url = d.pop("logoUrl")

        name = PaymentMethod(d.pop("name"))

        settings = PaymentMethodSettings.from_dict(d.pop("settings"))

        status = PaymentMethodStatus(d.pop("status"))

        summary_url = d.pop("summaryUrl")

        _limits = d.pop("limits", UNSET)
        limits: Union[Unset, PaymentMethodLimit]
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = PaymentMethodLimit.from_dict(_limits)

        payment_method_detail = cls(
            logo_url=logo_url,
            name=name,
            settings=settings,
            status=status,
            summary_url=summary_url,
            limits=limits,
        )

        payment_method_detail.additional_properties = d
        return payment_method_detail

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
