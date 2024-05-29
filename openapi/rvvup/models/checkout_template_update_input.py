from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkout_amount_type import CheckoutAmountType
from ..models.checkout_template_update_input_enabled_payment_methods import (
    CheckoutTemplateUpdateInputEnabledPaymentMethods,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_customer_fields_update_input import (
        CheckoutCustomerFieldsUpdateInput,
    )
    from ..models.checkout_payment_method_settings_update_input import (
        CheckoutPaymentMethodSettingsUpdateInput,
    )


T = TypeVar("T", bound="CheckoutTemplateUpdateInput")


@_attrs_define
class CheckoutTemplateUpdateInput:
    """The input for updating a checkout template.

    Example:
        {'name': 'My Checkout Template Updated', 'amountType': 'FIXED', 'enabledPaymentMethods': ['CARD',
            'PAY_BY_BANK'], 'notifyCustomer': False, 'notifyMerchant': False, 'customerFields': {'required': ['GIVEN_NAME',
            'SURNAME', 'EMAIL'], 'optional': ['PHONE_NUMBER']}, 'paymentMethodSettings': None}

    Attributes:
        amount_type (Union[Unset, CheckoutAmountType]): The amount type for the checkout. This can be either a fixed
            amount or an editable amount. If the amount is editable, the user can enter the amount they want to pay inside
            the hosted checkout. If the amount is fixed, the amount set in the checkout is the amount that will be paid and
            cannot be changed inside the hosted checkout.
        customer_fields (Union[Unset, CheckoutCustomerFieldsUpdateInput]): The customer fields that are required or
            optional for the checkout.
                                 If a field is not required or optional, it will not be shown in the hosted checkout page.
        enabled_payment_methods (Union[Unset, CheckoutTemplateUpdateInputEnabledPaymentMethods]): Ordered list of
            payment methods that are enabled for the checkout.
        name (Union[Unset, str]): The name of the checkout template.
        notify_customer (Union[Unset, bool]): Whether the customer should be notified on payment completion. Default:
            False.
        notify_merchant (Union[Unset, bool]): Whether you should be notified on payment completion. Default: False.
        payment_method_settings (Union[Unset, CheckoutPaymentMethodSettingsUpdateInput]): The payment method settings to
            be used for the checkout.
    """

    amount_type: Union[Unset, CheckoutAmountType] = UNSET
    customer_fields: Union[Unset, "CheckoutCustomerFieldsUpdateInput"] = UNSET
    enabled_payment_methods: Union[
        Unset, CheckoutTemplateUpdateInputEnabledPaymentMethods
    ] = UNSET
    name: Union[Unset, str] = UNSET
    notify_customer: Union[Unset, bool] = False
    notify_merchant: Union[Unset, bool] = False
    payment_method_settings: Union[
        Unset, "CheckoutPaymentMethodSettingsUpdateInput"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount_type: Union[Unset, str] = UNSET
        if not isinstance(self.amount_type, Unset):
            amount_type = self.amount_type.value

        customer_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_fields, Unset):
            customer_fields = self.customer_fields.to_dict()

        enabled_payment_methods: Union[Unset, str] = UNSET
        if not isinstance(self.enabled_payment_methods, Unset):
            enabled_payment_methods = self.enabled_payment_methods.value

        name = self.name

        notify_customer = self.notify_customer

        notify_merchant = self.notify_merchant

        payment_method_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method_settings, Unset):
            payment_method_settings = self.payment_method_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_type is not UNSET:
            field_dict["amountType"] = amount_type
        if customer_fields is not UNSET:
            field_dict["customerFields"] = customer_fields
        if enabled_payment_methods is not UNSET:
            field_dict["enabledPaymentMethods"] = enabled_payment_methods
        if name is not UNSET:
            field_dict["name"] = name
        if notify_customer is not UNSET:
            field_dict["notifyCustomer"] = notify_customer
        if notify_merchant is not UNSET:
            field_dict["notifyMerchant"] = notify_merchant
        if payment_method_settings is not UNSET:
            field_dict["paymentMethodSettings"] = payment_method_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_customer_fields_update_input import (
            CheckoutCustomerFieldsUpdateInput,
        )
        from ..models.checkout_payment_method_settings_update_input import (
            CheckoutPaymentMethodSettingsUpdateInput,
        )

        d = src_dict.copy()
        _amount_type = d.pop("amountType", UNSET)
        amount_type: Union[Unset, CheckoutAmountType]
        if isinstance(_amount_type, Unset):
            amount_type = UNSET
        else:
            amount_type = CheckoutAmountType(_amount_type)

        _customer_fields = d.pop("customerFields", UNSET)
        customer_fields: Union[Unset, CheckoutCustomerFieldsUpdateInput]
        if isinstance(_customer_fields, Unset):
            customer_fields = UNSET
        else:
            customer_fields = CheckoutCustomerFieldsUpdateInput.from_dict(
                _customer_fields
            )

        _enabled_payment_methods = d.pop("enabledPaymentMethods", UNSET)
        enabled_payment_methods: Union[
            Unset, CheckoutTemplateUpdateInputEnabledPaymentMethods
        ]
        if isinstance(_enabled_payment_methods, Unset):
            enabled_payment_methods = UNSET
        else:
            enabled_payment_methods = CheckoutTemplateUpdateInputEnabledPaymentMethods(
                _enabled_payment_methods
            )

        name = d.pop("name", UNSET)

        notify_customer = d.pop("notifyCustomer", UNSET)

        notify_merchant = d.pop("notifyMerchant", UNSET)

        _payment_method_settings = d.pop("paymentMethodSettings", UNSET)
        payment_method_settings: Union[Unset, CheckoutPaymentMethodSettingsUpdateInput]
        if isinstance(_payment_method_settings, Unset):
            payment_method_settings = UNSET
        else:
            payment_method_settings = (
                CheckoutPaymentMethodSettingsUpdateInput.from_dict(
                    _payment_method_settings
                )
            )

        checkout_template_update_input = cls(
            amount_type=amount_type,
            customer_fields=customer_fields,
            enabled_payment_methods=enabled_payment_methods,
            name=name,
            notify_customer=notify_customer,
            notify_merchant=notify_merchant,
            payment_method_settings=payment_method_settings,
        )

        checkout_template_update_input.additional_properties = d
        return checkout_template_update_input

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
