from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_method import PaymentMethod
from ..models.payment_capture_type import PaymentCaptureType
from typing import Union

if TYPE_CHECKING:
    from ..models.item_input import ItemInput
    from ..models.money_input import MoneyInput
    from ..models.address_input import AddressInput
    from ..models.customer_input import CustomerInput


T = TypeVar("T", bound="PaymentSessionCreateInput")


@_attrs_define
class PaymentSessionCreateInput:
    """Input for creating a payment session.

    Attributes:
        payment_method (PaymentMethod): The payment method.
        session_key (str): The unique identifier for the payment session. If the same session key has been used,
                                     the existing payment session will be updated with the new values. Example:
            DEFC8F15-3BBD-4153-9D6D-3A3D9F06C544.
        total (MoneyInput):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        billing_address (Union[Unset, AddressInput]): The address details.
        customer (Union[Unset, CustomerInput]): The customer's details.
        discount_total (Union[Unset, MoneyInput]):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        external_reference (Union[Unset, str]): Your reference to identify the payment session. Example: REF-12345.
        items (Union[Unset, List['ItemInput']]): List of items that the customer is purchasing.
        payment_capture_type (Union[Unset, PaymentCaptureType]): The capture type for the payment.
        requires_shipping (Union[Unset, bool]): Whether the customer is required to provide a shipping address. Default:
            False.
        shipping_address (Union[Unset, AddressInput]): The address details.
        shipping_total (Union[Unset, MoneyInput]):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        tax_total (Union[Unset, MoneyInput]):  Example: {'amount': '100.00', 'currency': 'GBP'}.
    """

    payment_method: PaymentMethod
    session_key: str
    total: "MoneyInput"
    billing_address: Union[Unset, "AddressInput"] = UNSET
    customer: Union[Unset, "CustomerInput"] = UNSET
    discount_total: Union[Unset, "MoneyInput"] = UNSET
    external_reference: Union[Unset, str] = UNSET
    items: Union[Unset, List["ItemInput"]] = UNSET
    payment_capture_type: Union[Unset, PaymentCaptureType] = UNSET
    requires_shipping: Union[Unset, bool] = False
    shipping_address: Union[Unset, "AddressInput"] = UNSET
    shipping_total: Union[Unset, "MoneyInput"] = UNSET
    tax_total: Union[Unset, "MoneyInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_method = self.payment_method.value

        session_key = self.session_key

        total = self.total.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        discount_total: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discount_total, Unset):
            discount_total = self.discount_total.to_dict()

        external_reference = self.external_reference

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        payment_capture_type: Union[Unset, str] = UNSET
        if not isinstance(self.payment_capture_type, Unset):
            payment_capture_type = self.payment_capture_type.value

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
                "paymentMethod": payment_method,
                "sessionKey": session_key,
                "total": total,
            }
        )
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if customer is not UNSET:
            field_dict["customer"] = customer
        if discount_total is not UNSET:
            field_dict["discountTotal"] = discount_total
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if items is not UNSET:
            field_dict["items"] = items
        if payment_capture_type is not UNSET:
            field_dict["paymentCaptureType"] = payment_capture_type
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
        from ..models.item_input import ItemInput
        from ..models.money_input import MoneyInput
        from ..models.address_input import AddressInput
        from ..models.customer_input import CustomerInput

        d = src_dict.copy()
        payment_method = PaymentMethod(d.pop("paymentMethod"))

        session_key = d.pop("sessionKey")

        total = MoneyInput.from_dict(d.pop("total"))

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, AddressInput]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = AddressInput.from_dict(_billing_address)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CustomerInput]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CustomerInput.from_dict(_customer)

        _discount_total = d.pop("discountTotal", UNSET)
        discount_total: Union[Unset, MoneyInput]
        if isinstance(_discount_total, Unset):
            discount_total = UNSET
        else:
            discount_total = MoneyInput.from_dict(_discount_total)

        external_reference = d.pop("externalReference", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = ItemInput.from_dict(items_item_data)

            items.append(items_item)

        _payment_capture_type = d.pop("paymentCaptureType", UNSET)
        payment_capture_type: Union[Unset, PaymentCaptureType]
        if isinstance(_payment_capture_type, Unset):
            payment_capture_type = UNSET
        else:
            payment_capture_type = PaymentCaptureType(_payment_capture_type)

        requires_shipping = d.pop("requiresShipping", UNSET)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, AddressInput]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = AddressInput.from_dict(_shipping_address)

        _shipping_total = d.pop("shippingTotal", UNSET)
        shipping_total: Union[Unset, MoneyInput]
        if isinstance(_shipping_total, Unset):
            shipping_total = UNSET
        else:
            shipping_total = MoneyInput.from_dict(_shipping_total)

        _tax_total = d.pop("taxTotal", UNSET)
        tax_total: Union[Unset, MoneyInput]
        if isinstance(_tax_total, Unset):
            tax_total = UNSET
        else:
            tax_total = MoneyInput.from_dict(_tax_total)

        payment_session_create_input = cls(
            payment_method=payment_method,
            session_key=session_key,
            total=total,
            billing_address=billing_address,
            customer=customer,
            discount_total=discount_total,
            external_reference=external_reference,
            items=items,
            payment_capture_type=payment_capture_type,
            requires_shipping=requires_shipping,
            shipping_address=shipping_address,
            shipping_total=shipping_total,
            tax_total=tax_total,
        )

        payment_session_create_input.additional_properties = d
        return payment_session_create_input

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
