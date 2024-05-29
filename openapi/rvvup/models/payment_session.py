from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_session_status import PaymentSessionStatus
from dateutil.parser import isoparse
from typing import Union
import datetime

if TYPE_CHECKING:
    from ..models.customer import Customer
    from ..models.payment import Payment
    from ..models.address import Address
    from ..models.money import Money
    from ..models.item import Item


T = TypeVar("T", bound="PaymentSession")


@_attrs_define
class PaymentSession:
    """
    Attributes:
        created_at (datetime.datetime): The datetime when the payment session was created.
        dashboard_url (str): The URL to the merchant dashboard for the payment session.
        id (str): The unique ID for the payment session.
        items (List['Item']): List of items that the customer is purchasing.
        merchant_id (str): The ID of the merchant that the payment session was created for.
        payments (List['Payment']): List of payments that have been made for the payment session.
        status (PaymentSessionStatus): The status of the payment session.
        total (Money):
        updated_at (datetime.datetime): The datetime when the payment session was last updated.
        billing_address (Union[Unset, Address]):
        checkout_id (Union[Unset, str]): The ID of the checkout that the payment session was created from.
        customer (Union[Unset, Customer]):
        discount_total (Union[Unset, Money]):
        external_reference (Union[Unset, str]): Your reference to identify the payment session.
        payment_link_id (Union[Unset, str]): The ID of the payment link that the payment session was created from.
        requires_shipping (Union[Unset, bool]): Whether the customer is required to provide a shipping address.
        shipping_address (Union[Unset, Address]):
        shipping_total (Union[Unset, Money]):
        tax_total (Union[Unset, Money]):
    """

    created_at: datetime.datetime
    dashboard_url: str
    id: str
    items: List["Item"]
    merchant_id: str
    payments: List["Payment"]
    status: PaymentSessionStatus
    total: "Money"
    updated_at: datetime.datetime
    billing_address: Union[Unset, "Address"] = UNSET
    checkout_id: Union[Unset, str] = UNSET
    customer: Union[Unset, "Customer"] = UNSET
    discount_total: Union[Unset, "Money"] = UNSET
    external_reference: Union[Unset, str] = UNSET
    payment_link_id: Union[Unset, str] = UNSET
    requires_shipping: Union[Unset, bool] = UNSET
    shipping_address: Union[Unset, "Address"] = UNSET
    shipping_total: Union[Unset, "Money"] = UNSET
    tax_total: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        dashboard_url = self.dashboard_url

        id = self.id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        merchant_id = self.merchant_id

        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        status = self.status.value

        total = self.total.to_dict()

        updated_at = self.updated_at.isoformat()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        checkout_id = self.checkout_id

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        discount_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discount_total, Unset):
            discount_total = self.discount_total.to_dict()

        external_reference = self.external_reference

        payment_link_id = self.payment_link_id

        requires_shipping = self.requires_shipping

        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        shipping_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_total, Unset):
            shipping_total = self.shipping_total.to_dict()

        tax_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_total, Unset):
            tax_total = self.tax_total.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "dashboardUrl": dashboard_url,
                "id": id,
                "items": items,
                "merchantId": merchant_id,
                "payments": payments,
                "status": status,
                "total": total,
                "updatedAt": updated_at,
            }
        )
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if checkout_id is not UNSET:
            field_dict["checkoutId"] = checkout_id
        if customer is not UNSET:
            field_dict["customer"] = customer
        if discount_total is not UNSET:
            field_dict["discountTotal"] = discount_total
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if payment_link_id is not UNSET:
            field_dict["paymentLinkId"] = payment_link_id
        if requires_shipping is not UNSET:
            field_dict["requiresShipping"] = requires_shipping
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if shipping_total is not UNSET:
            field_dict["shippingTotal"] = shipping_total
        if tax_total is not UNSET:
            field_dict["taxTotal"] = tax_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer import Customer
        from ..models.payment import Payment
        from ..models.address import Address
        from ..models.money import Money
        from ..models.item import Item

        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        dashboard_url = d.pop("dashboardUrl")

        id = d.pop("id")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        merchant_id = d.pop("merchantId")

        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = Payment.from_dict(payments_item_data)

            payments.append(payments_item)

        status = PaymentSessionStatus(d.pop("status"))

        total = Money.from_dict(d.pop("total"))

        updated_at = isoparse(d.pop("updatedAt"))

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, Address]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = Address.from_dict(_billing_address)

        checkout_id = d.pop("checkoutId", UNSET)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, Customer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = Customer.from_dict(_customer)

        _discount_total = d.pop("discountTotal", UNSET)
        discount_total: Union[Unset, Money]
        if isinstance(_discount_total, Unset):
            discount_total = UNSET
        else:
            discount_total = Money.from_dict(_discount_total)

        external_reference = d.pop("externalReference", UNSET)

        payment_link_id = d.pop("paymentLinkId", UNSET)

        requires_shipping = d.pop("requiresShipping", UNSET)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, Address]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = Address.from_dict(_shipping_address)

        _shipping_total = d.pop("shippingTotal", UNSET)
        shipping_total: Union[Unset, Money]
        if isinstance(_shipping_total, Unset):
            shipping_total = UNSET
        else:
            shipping_total = Money.from_dict(_shipping_total)

        _tax_total = d.pop("taxTotal", UNSET)
        tax_total: Union[Unset, Money]
        if isinstance(_tax_total, Unset):
            tax_total = UNSET
        else:
            tax_total = Money.from_dict(_tax_total)

        payment_session = cls(
            created_at=created_at,
            dashboard_url=dashboard_url,
            id=id,
            items=items,
            merchant_id=merchant_id,
            payments=payments,
            status=status,
            total=total,
            updated_at=updated_at,
            billing_address=billing_address,
            checkout_id=checkout_id,
            customer=customer,
            discount_total=discount_total,
            external_reference=external_reference,
            payment_link_id=payment_link_id,
            requires_shipping=requires_shipping,
            shipping_address=shipping_address,
            shipping_total=shipping_total,
            tax_total=tax_total,
        )

        payment_session.additional_properties = d
        return payment_session

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
