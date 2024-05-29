import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.application_source import ApplicationSource
from ..models.checkout_amount_type import CheckoutAmountType
from ..models.payment_method import PaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_customer_fields import CheckoutCustomerFields
    from ..models.checkout_payment_method_settings import CheckoutPaymentMethodSettings


T = TypeVar("T", bound="CheckoutTemplate")


@_attrs_define
class CheckoutTemplate:
    """
    Attributes:
        amount_type (CheckoutAmountType): The amount type for the checkout. This can be either a fixed amount or an
            editable amount. If the amount is editable, the user can enter the amount they want to pay inside the hosted
            checkout. If the amount is fixed, the amount set in the checkout is the amount that will be paid and cannot be
            changed inside the hosted checkout.
        created_at (datetime.datetime): The datetime when the checkout template was created.
        id (str): The unique ID of the checkout template.
        merchant_id (str): The ID of the merchant that owns this checkout template.
        name (str): The name of the checkout template.
        notify_customer (bool): Whether the customer should be notified on payment completion.
        notify_merchant (bool): Whether you should be notified on payment completion.
        source (ApplicationSource): The source of the application.
        updated_at (datetime.datetime): The datetime when the checkout template was last updated.
        customer_fields (Union[Unset, CheckoutCustomerFields]):
        enabled_payment_methods (Union[Unset, List[PaymentMethod]]): Ordered list of payment methods that are enabled
            for the checkout.
        payment_method_settings (Union[Unset, CheckoutPaymentMethodSettings]): The payment method settings to be used
            for the checkout.
    """

    amount_type: CheckoutAmountType
    created_at: datetime.datetime
    id: str
    merchant_id: str
    name: str
    notify_customer: bool
    notify_merchant: bool
    source: ApplicationSource
    updated_at: datetime.datetime
    customer_fields: Union[Unset, "CheckoutCustomerFields"] = UNSET
    enabled_payment_methods: Union[Unset, List[PaymentMethod]] = UNSET
    payment_method_settings: Union[Unset, "CheckoutPaymentMethodSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount_type = self.amount_type.value

        created_at = self.created_at.isoformat()

        id = self.id

        merchant_id = self.merchant_id

        name = self.name

        notify_customer = self.notify_customer

        notify_merchant = self.notify_merchant

        source = self.source.value

        updated_at = self.updated_at.isoformat()

        customer_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_fields, Unset):
            customer_fields = self.customer_fields.to_dict()

        enabled_payment_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.enabled_payment_methods, Unset):
            enabled_payment_methods = []
            for enabled_payment_methods_item_data in self.enabled_payment_methods:
                enabled_payment_methods_item = enabled_payment_methods_item_data.value
                enabled_payment_methods.append(enabled_payment_methods_item)

        payment_method_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_settings, Unset):
            payment_method_settings = self.payment_method_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountType": amount_type,
                "createdAt": created_at,
                "id": id,
                "merchantId": merchant_id,
                "name": name,
                "notifyCustomer": notify_customer,
                "notifyMerchant": notify_merchant,
                "source": source,
                "updatedAt": updated_at,
            }
        )
        if customer_fields is not UNSET:
            field_dict["customerFields"] = customer_fields
        if enabled_payment_methods is not UNSET:
            field_dict["enabledPaymentMethods"] = enabled_payment_methods
        if payment_method_settings is not UNSET:
            field_dict["paymentMethodSettings"] = payment_method_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_customer_fields import CheckoutCustomerFields
        from ..models.checkout_payment_method_settings import (
            CheckoutPaymentMethodSettings,
        )

        d = src_dict.copy()
        amount_type = CheckoutAmountType(d.pop("amountType"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        merchant_id = d.pop("merchantId")

        name = d.pop("name")

        notify_customer = d.pop("notifyCustomer")

        notify_merchant = d.pop("notifyMerchant")

        source = ApplicationSource(d.pop("source"))

        updated_at = isoparse(d.pop("updatedAt"))

        _customer_fields = d.pop("customerFields", UNSET)
        customer_fields: Union[Unset, CheckoutCustomerFields]
        if isinstance(_customer_fields, Unset):
            customer_fields = UNSET
        else:
            customer_fields = CheckoutCustomerFields.from_dict(_customer_fields)

        enabled_payment_methods = []
        _enabled_payment_methods = d.pop("enabledPaymentMethods", UNSET)
        for enabled_payment_methods_item_data in _enabled_payment_methods or []:
            enabled_payment_methods_item = PaymentMethod(
                enabled_payment_methods_item_data
            )

            enabled_payment_methods.append(enabled_payment_methods_item)

        _payment_method_settings = d.pop("paymentMethodSettings", UNSET)
        payment_method_settings: Union[Unset, CheckoutPaymentMethodSettings]
        if isinstance(_payment_method_settings, Unset):
            payment_method_settings = UNSET
        else:
            payment_method_settings = CheckoutPaymentMethodSettings.from_dict(
                _payment_method_settings
            )

        checkout_template = cls(
            amount_type=amount_type,
            created_at=created_at,
            id=id,
            merchant_id=merchant_id,
            name=name,
            notify_customer=notify_customer,
            notify_merchant=notify_merchant,
            source=source,
            updated_at=updated_at,
            customer_fields=customer_fields,
            enabled_payment_methods=enabled_payment_methods,
            payment_method_settings=payment_method_settings,
        )

        checkout_template.additional_properties = d
        return checkout_template

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
