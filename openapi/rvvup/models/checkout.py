from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from dateutil.parser import isoparse
from ..models.application_source import ApplicationSource
from typing import Union
import datetime
from ..models.checkout_status import CheckoutStatus

if TYPE_CHECKING:
    from ..models.customer import Customer
    from ..models.address import Address
    from ..models.checkout_metadata import CheckoutMetadata
    from ..models.money import Money


T = TypeVar("T", bound="Checkout")


@_attrs_define
class Checkout:
    """Checkout object

    Attributes:
        checkout_template_id (str): The ID of the checkout template to use for this checkout.
        created_at (datetime.datetime): The datetime when the checkout was created.
        expires_at (datetime.datetime): The datetime when the checkout will expire.
        id (str): The unique ID of the checkout.
        merchant_id (str): The ID of the merchant that owns this checkout.
        metadata (CheckoutMetadata): Key value pairs to store additional information about the checkout.
        payment_session_ids (List[str]): The IDs of the payment sessions that were created for this checkout.
        source (ApplicationSource): The source of the application.
        status (CheckoutStatus): The status of the checkout.
        updated_at (datetime.datetime): The datetime when the checkout was last updated.
        url (str): The URL to the hosted checkout page.
        amount (Union[Unset, Money]):
        billing_address (Union[Unset, Address]):
        customer (Union[Unset, Customer]):
        payment_link_id (Union[Unset, str]): The ID of the payment link that was used to create this checkout.
        reference (Union[Unset, str]): Your reference to identify the checkout and the subsequently created payment
            sessions.
        success_url (Union[Unset, str]): The URL to redirect the customer to after the checkout is completed
            successfully.
    """

    checkout_template_id: str
    created_at: datetime.datetime
    expires_at: datetime.datetime
    id: str
    merchant_id: str
    metadata: "CheckoutMetadata"
    payment_session_ids: List[str]
    source: ApplicationSource
    status: CheckoutStatus
    updated_at: datetime.datetime
    url: str
    amount: Union[Unset, "Money"] = UNSET
    billing_address: Union[Unset, "Address"] = UNSET
    customer: Union[Unset, "Customer"] = UNSET
    payment_link_id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    success_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checkout_template_id = self.checkout_template_id

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        id = self.id

        merchant_id = self.merchant_id

        metadata = self.metadata.to_dict()

        payment_session_ids = self.payment_session_ids

        source = self.source.value

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        url = self.url

        amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        payment_link_id = self.payment_link_id

        reference = self.reference

        success_url = self.success_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkoutTemplateId": checkout_template_id,
                "createdAt": created_at,
                "expiresAt": expires_at,
                "id": id,
                "merchantId": merchant_id,
                "metadata": metadata,
                "paymentSessionIds": payment_session_ids,
                "source": source,
                "status": status,
                "updatedAt": updated_at,
                "url": url,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if customer is not UNSET:
            field_dict["customer"] = customer
        if payment_link_id is not UNSET:
            field_dict["paymentLinkId"] = payment_link_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if success_url is not UNSET:
            field_dict["successUrl"] = success_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer import Customer
        from ..models.address import Address
        from ..models.checkout_metadata import CheckoutMetadata
        from ..models.money import Money

        d = src_dict.copy()
        checkout_template_id = d.pop("checkoutTemplateId")

        created_at = isoparse(d.pop("createdAt"))

        expires_at = isoparse(d.pop("expiresAt"))

        id = d.pop("id")

        merchant_id = d.pop("merchantId")

        metadata = CheckoutMetadata.from_dict(d.pop("metadata"))

        payment_session_ids = cast(List[str], d.pop("paymentSessionIds"))

        source = ApplicationSource(d.pop("source"))

        status = CheckoutStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updatedAt"))

        url = d.pop("url")

        _amount = d.pop("amount", UNSET)
        amount: Union[Unset, Money]
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Money.from_dict(_amount)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, Address]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = Address.from_dict(_billing_address)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, Customer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = Customer.from_dict(_customer)

        payment_link_id = d.pop("paymentLinkId", UNSET)

        reference = d.pop("reference", UNSET)

        success_url = d.pop("successUrl", UNSET)

        checkout = cls(
            checkout_template_id=checkout_template_id,
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            merchant_id=merchant_id,
            metadata=metadata,
            payment_session_ids=payment_session_ids,
            source=source,
            status=status,
            updated_at=updated_at,
            url=url,
            amount=amount,
            billing_address=billing_address,
            customer=customer,
            payment_link_id=payment_link_id,
            reference=reference,
            success_url=success_url,
        )

        checkout.additional_properties = d
        return checkout

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
