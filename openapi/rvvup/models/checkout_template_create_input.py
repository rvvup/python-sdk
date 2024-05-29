from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.checkout_template_create_input_enabled_payment_methods import (
    CheckoutTemplateCreateInputEnabledPaymentMethods,
)
from ..models.application_source import ApplicationSource
from typing import Union
from ..models.checkout_amount_type import CheckoutAmountType

if TYPE_CHECKING:
    from ..models.checkout_payment_method_settings_input import (
        CheckoutPaymentMethodSettingsInput,
    )
    from ..models.checkout_customer_fields_input import CheckoutCustomerFieldsInput


T = TypeVar("T", bound="CheckoutTemplateCreateInput")


@_attrs_define
class CheckoutTemplateCreateInput:
    """The input for creating a checkout template.

    Example:
        {'name': 'My Checkout Template', 'source': 'API', 'amountType': 'FIXED', 'enabledPaymentMethods': ['CARD',
            'APPLE_PAY', 'PAY_BY_BANK'], 'notifyCustomer': False, 'notifyMerchant': False, 'customerFields': {'required':
            ['GIVEN_NAME', 'SURNAME', 'EMAIL'], 'optional': ['PHONE_NUMBER']}, 'paymentMethodSettings': None}

    Attributes:
        name (str): The name of the checkout template.
        amount_type (Union[Unset, CheckoutAmountType]): The amount type for the checkout. This can be either a fixed
            amount or an editable amount. If the amount is editable, the user can enter the amount they want to pay inside
            the hosted checkout. If the amount is fixed, the amount set in the checkout is the amount that will be paid and
            cannot be changed inside the hosted checkout.
        customer_fields (Union[Unset, CheckoutCustomerFieldsInput]): The customer fields that are required or optional
            for the checkout.
                                 If a field is not required or optional, it will not be shown in the hosted checkout page.
        enabled_payment_methods (Union[Unset, CheckoutTemplateCreateInputEnabledPaymentMethods]): Ordered list of
            payment methods that are enabled for the checkout.
        notify_customer (Union[Unset, bool]): Whether the customer should be notified on payment completion. Default:
            False.
        notify_merchant (Union[Unset, bool]): Whether you should be notified on payment completion. Default: False.
        payment_method_settings (Union[Unset, CheckoutPaymentMethodSettingsInput]): The payment method settings to be
            used for the checkout.
        source (Union[Unset, ApplicationSource]): The source of the application.
    """

    name: str
    amount_type: Union[Unset, CheckoutAmountType] = UNSET
    customer_fields: Union[Unset, "CheckoutCustomerFieldsInput"] = UNSET
    enabled_payment_methods: Union[
        Unset, CheckoutTemplateCreateInputEnabledPaymentMethods
    ] = UNSET
    notify_customer: Union[Unset, bool] = False
    notify_merchant: Union[Unset, bool] = False
    payment_method_settings: Union[Unset, "CheckoutPaymentMethodSettingsInput"] = UNSET
    source: Union[Unset, ApplicationSource] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        amount_type: Union[Unset, str] = UNSET
        if not isinstance(self.amount_type, Unset):
            amount_type = self.amount_type.value

        customer_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_fields, Unset):
            customer_fields = self.customer_fields.to_dict()

        enabled_payment_methods: Union[Unset, str] = UNSET
        if not isinstance(self.enabled_payment_methods, Unset):
            enabled_payment_methods = self.enabled_payment_methods.value

        notify_customer = self.notify_customer

        notify_merchant = self.notify_merchant

        payment_method_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_settings, Unset):
            payment_method_settings = self.payment_method_settings.to_dict()

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if amount_type is not UNSET:
            field_dict["amountType"] = amount_type
        if customer_fields is not UNSET:
            field_dict["customerFields"] = customer_fields
        if enabled_payment_methods is not UNSET:
            field_dict["enabledPaymentMethods"] = enabled_payment_methods
        if notify_customer is not UNSET:
            field_dict["notifyCustomer"] = notify_customer
        if notify_merchant is not UNSET:
            field_dict["notifyMerchant"] = notify_merchant
        if payment_method_settings is not UNSET:
            field_dict["paymentMethodSettings"] = payment_method_settings
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_payment_method_settings_input import (
            CheckoutPaymentMethodSettingsInput,
        )
        from ..models.checkout_customer_fields_input import CheckoutCustomerFieldsInput

        d = src_dict.copy()
        name = d.pop("name")

        _amount_type = d.pop("amountType", UNSET)
        amount_type: Union[Unset, CheckoutAmountType]
        if isinstance(_amount_type, Unset):
            amount_type = UNSET
        else:
            amount_type = CheckoutAmountType(_amount_type)

        _customer_fields = d.pop("customerFields", UNSET)
        customer_fields: Union[Unset, CheckoutCustomerFieldsInput]
        if isinstance(_customer_fields, Unset):
            customer_fields = UNSET
        else:
            customer_fields = CheckoutCustomerFieldsInput.from_dict(_customer_fields)

        _enabled_payment_methods = d.pop("enabledPaymentMethods", UNSET)
        enabled_payment_methods: Union[
            Unset, CheckoutTemplateCreateInputEnabledPaymentMethods
        ]
        if isinstance(_enabled_payment_methods, Unset):
            enabled_payment_methods = UNSET
        else:
            enabled_payment_methods = CheckoutTemplateCreateInputEnabledPaymentMethods(
                _enabled_payment_methods
            )

        notify_customer = d.pop("notifyCustomer", UNSET)

        notify_merchant = d.pop("notifyMerchant", UNSET)

        _payment_method_settings = d.pop("paymentMethodSettings", UNSET)
        payment_method_settings: Union[Unset, CheckoutPaymentMethodSettingsInput]
        if isinstance(_payment_method_settings, Unset):
            payment_method_settings = UNSET
        else:
            payment_method_settings = CheckoutPaymentMethodSettingsInput.from_dict(
                _payment_method_settings
            )

        _source = d.pop("source", UNSET)
        source: Union[Unset, ApplicationSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ApplicationSource(_source)

        checkout_template_create_input = cls(
            name=name,
            amount_type=amount_type,
            customer_fields=customer_fields,
            enabled_payment_methods=enabled_payment_methods,
            notify_customer=notify_customer,
            notify_merchant=notify_merchant,
            payment_method_settings=payment_method_settings,
            source=source,
        )

        checkout_template_create_input.additional_properties = d
        return checkout_template_create_input

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
