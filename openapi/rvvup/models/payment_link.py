from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from dateutil.parser import isoparse
from ..models.application_source import ApplicationSource
from ..models.payment_link_status import PaymentLinkStatus
from typing import Union
import datetime

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="PaymentLink")


@_attrs_define
class PaymentLink:
    """Payment link object

    Attributes:
        checkout_ids (List[str]): The IDs of the checkouts that were created for this payment link.
        created_at (datetime.datetime): The datetime when the payment link was created.
        id (str): The unique ID of the payment link.
        merchant_id (str): The ID of the merchant that owns this checkout.
        reusable (bool): Whether the payment link can be reused for multiple payments.
        source (ApplicationSource): The source of the application.
        status (PaymentLinkStatus): The status of the payment link.
        updated_at (datetime.datetime): The datetime when the payment link was last updated.
        url (str): The URL to the hosted payment link page.
        amount (Union[Unset, Money]):
        checkout_template_id (Union[Unset, str]): The ID of the checkout template to use for this payment link.
                                     If not provided, the default template will be used.
        reference (Union[Unset, str]): Your reference to identify the payment link and subsequently created checkouts
                                     and payment sessions.
    """

    checkout_ids: List[str]
    created_at: datetime.datetime
    id: str
    merchant_id: str
    reusable: bool
    source: ApplicationSource
    status: PaymentLinkStatus
    updated_at: datetime.datetime
    url: str
    amount: Union[Unset, "Money"] = UNSET
    checkout_template_id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checkout_ids = self.checkout_ids

        created_at = self.created_at.isoformat()

        id = self.id

        merchant_id = self.merchant_id

        reusable = self.reusable

        source = self.source.value

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        url = self.url

        amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        checkout_template_id = self.checkout_template_id

        reference = self.reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkoutIds": checkout_ids,
                "createdAt": created_at,
                "id": id,
                "merchantId": merchant_id,
                "reusable": reusable,
                "source": source,
                "status": status,
                "updatedAt": updated_at,
                "url": url,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if checkout_template_id is not UNSET:
            field_dict["checkoutTemplateId"] = checkout_template_id
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        checkout_ids = cast(List[str], d.pop("checkoutIds"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        merchant_id = d.pop("merchantId")

        reusable = d.pop("reusable")

        source = ApplicationSource(d.pop("source"))

        status = PaymentLinkStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updatedAt"))

        url = d.pop("url")

        _amount = d.pop("amount", UNSET)
        amount: Union[Unset, Money]
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Money.from_dict(_amount)

        checkout_template_id = d.pop("checkoutTemplateId", UNSET)

        reference = d.pop("reference", UNSET)

        payment_link = cls(
            checkout_ids=checkout_ids,
            created_at=created_at,
            id=id,
            merchant_id=merchant_id,
            reusable=reusable,
            source=source,
            status=status,
            updated_at=updated_at,
            url=url,
            amount=amount,
            checkout_template_id=checkout_template_id,
            reference=reference,
        )

        payment_link.additional_properties = d
        return payment_link

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
