from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_apple_pay_settings_input import CheckoutApplePaySettingsInput
    from ..models.checkout_card_settings_input import CheckoutCardSettingsInput
    from ..models.checkout_pay_by_bank_settings_input import (
        CheckoutPayByBankSettingsInput,
    )


T = TypeVar("T", bound="CheckoutPaymentMethodSettingsInput")


@_attrs_define
class CheckoutPaymentMethodSettingsInput:
    """The payment method settings to be used for the checkout.

    Attributes:
        apple_pay (Union[Unset, CheckoutApplePaySettingsInput]): The Apple Pay settings to be used for the checkout.
        card (Union[Unset, CheckoutCardSettingsInput]): The Card settings to be used for the checkout.
        pay_by_bank (Union[Unset, CheckoutPayByBankSettingsInput]): The Pay by Bank settings to be used for the
            checkout.
    """

    apple_pay: Union[Unset, "CheckoutApplePaySettingsInput"] = UNSET
    card: Union[Unset, "CheckoutCardSettingsInput"] = UNSET
    pay_by_bank: Union[Unset, "CheckoutPayByBankSettingsInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        apple_pay: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.apple_pay, Unset):
            apple_pay = self.apple_pay.to_dict()

        card: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        pay_by_bank: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pay_by_bank, Unset):
            pay_by_bank = self.pay_by_bank.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apple_pay is not UNSET:
            field_dict["applePay"] = apple_pay
        if card is not UNSET:
            field_dict["card"] = card
        if pay_by_bank is not UNSET:
            field_dict["payByBank"] = pay_by_bank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_apple_pay_settings_input import (
            CheckoutApplePaySettingsInput,
        )
        from ..models.checkout_card_settings_input import CheckoutCardSettingsInput
        from ..models.checkout_pay_by_bank_settings_input import (
            CheckoutPayByBankSettingsInput,
        )

        d = src_dict.copy()
        _apple_pay = d.pop("applePay", UNSET)
        apple_pay: Union[Unset, CheckoutApplePaySettingsInput]
        if isinstance(_apple_pay, Unset):
            apple_pay = UNSET
        else:
            apple_pay = CheckoutApplePaySettingsInput.from_dict(_apple_pay)

        _card = d.pop("card", UNSET)
        card: Union[Unset, CheckoutCardSettingsInput]
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = CheckoutCardSettingsInput.from_dict(_card)

        _pay_by_bank = d.pop("payByBank", UNSET)
        pay_by_bank: Union[Unset, CheckoutPayByBankSettingsInput]
        if isinstance(_pay_by_bank, Unset):
            pay_by_bank = UNSET
        else:
            pay_by_bank = CheckoutPayByBankSettingsInput.from_dict(_pay_by_bank)

        checkout_payment_method_settings_input = cls(
            apple_pay=apple_pay,
            card=card,
            pay_by_bank=pay_by_bank,
        )

        checkout_payment_method_settings_input.additional_properties = d
        return checkout_payment_method_settings_input

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
