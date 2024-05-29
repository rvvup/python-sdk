from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union

if TYPE_CHECKING:
    from ..models.checkout_card_settings_update_input import (
        CheckoutCardSettingsUpdateInput,
    )
    from ..models.checkout_pay_by_bank_settings_update_input import (
        CheckoutPayByBankSettingsUpdateInput,
    )
    from ..models.checkout_apple_pay_settings_update_input import (
        CheckoutApplePaySettingsUpdateInput,
    )


T = TypeVar("T", bound="CheckoutPaymentMethodSettingsUpdateInput")


@_attrs_define
class CheckoutPaymentMethodSettingsUpdateInput:
    """The payment method settings to be used for the checkout.

    Attributes:
        apple_pay (Union[Unset, CheckoutApplePaySettingsUpdateInput]): The Apple Pay settings to be used for the
            checkout.
        card (Union[Unset, CheckoutCardSettingsUpdateInput]): The Card settings to be used for the checkout.
        pay_by_bank (Union[Unset, CheckoutPayByBankSettingsUpdateInput]): The Pay by Bank settings to be used for the
            checkout.
    """

    apple_pay: Union[Unset, "CheckoutApplePaySettingsUpdateInput"] = UNSET
    card: Union[Unset, "CheckoutCardSettingsUpdateInput"] = UNSET
    pay_by_bank: Union[Unset, "CheckoutPayByBankSettingsUpdateInput"] = UNSET
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
        from ..models.checkout_card_settings_update_input import (
            CheckoutCardSettingsUpdateInput,
        )
        from ..models.checkout_pay_by_bank_settings_update_input import (
            CheckoutPayByBankSettingsUpdateInput,
        )
        from ..models.checkout_apple_pay_settings_update_input import (
            CheckoutApplePaySettingsUpdateInput,
        )

        d = src_dict.copy()
        _apple_pay = d.pop("applePay", UNSET)
        apple_pay: Union[Unset, CheckoutApplePaySettingsUpdateInput]
        if isinstance(_apple_pay, Unset):
            apple_pay = UNSET
        else:
            apple_pay = CheckoutApplePaySettingsUpdateInput.from_dict(_apple_pay)

        _card = d.pop("card", UNSET)
        card: Union[Unset, CheckoutCardSettingsUpdateInput]
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = CheckoutCardSettingsUpdateInput.from_dict(_card)

        _pay_by_bank = d.pop("payByBank", UNSET)
        pay_by_bank: Union[Unset, CheckoutPayByBankSettingsUpdateInput]
        if isinstance(_pay_by_bank, Unset):
            pay_by_bank = UNSET
        else:
            pay_by_bank = CheckoutPayByBankSettingsUpdateInput.from_dict(_pay_by_bank)

        checkout_payment_method_settings_update_input = cls(
            apple_pay=apple_pay,
            card=card,
            pay_by_bank=pay_by_bank,
        )

        checkout_payment_method_settings_update_input.additional_properties = d
        return checkout_payment_method_settings_update_input

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
