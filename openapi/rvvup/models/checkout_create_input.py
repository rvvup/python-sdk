from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.application_source import ApplicationSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_input import AddressInput
    from ..models.checkout_create_input_metadata import CheckoutCreateInputMetadata
    from ..models.customer_input import CustomerInput
    from ..models.money_input import MoneyInput


T = TypeVar("T", bound="CheckoutCreateInput")


@_attrs_define
class CheckoutCreateInput:
    """The input to create a new checkout.

    Attributes:
        amount (Union[Unset, MoneyInput]):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        billing_address (Union[Unset, AddressInput]): The address details.
        checkout_template_id (Union[Unset, str]): The ID of the checkout template to use for this checkout.
                                     If not provided, the default template will be used.
                                     If provided, the template must be available to the merchant.
        customer (Union[Unset, CustomerInput]): The customer's details.
        metadata (Union[Unset, CheckoutCreateInputMetadata]): Key value pairs to store additional information about the
            checkout. Example: {'key1': 'value1', 'key2': 'value2'}.
        reference (Union[Unset, str]): Your reference to identify the checkout and the subsequently created payment
            sessions. Example: Order #12345.
        source (Union[Unset, ApplicationSource]): The source of the application.
        success_url (Union[Unset, str]): The URL to redirect the user to after the checkout is completed successfully.
                                     This field supports the template variable `{{CHECKOUT_ID}}` which will be replaced with
            the
                                     created checkouts ID. Example: https://example.com/success?checkout_id={{CHECKOUT_ID}}.
    """

    amount: Union[Unset, "MoneyInput"] = UNSET
    billing_address: Union[Unset, "AddressInput"] = UNSET
    checkout_template_id: Union[Unset, str] = UNSET
    customer: Union[Unset, "CustomerInput"] = UNSET
    metadata: Union[Unset, "CheckoutCreateInputMetadata"] = UNSET
    reference: Union[Unset, str] = UNSET
    source: Union[Unset, ApplicationSource] = UNSET
    success_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        checkout_template_id = self.checkout_template_id

        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        reference = self.reference

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        success_url = self.success_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if checkout_template_id is not UNSET:
            field_dict["checkoutTemplateId"] = checkout_template_id
        if customer is not UNSET:
            field_dict["customer"] = customer
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if reference is not UNSET:
            field_dict["reference"] = reference
        if source is not UNSET:
            field_dict["source"] = source
        if success_url is not UNSET:
            field_dict["successUrl"] = success_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_input import AddressInput
        from ..models.checkout_create_input_metadata import CheckoutCreateInputMetadata
        from ..models.customer_input import CustomerInput
        from ..models.money_input import MoneyInput

        d = src_dict.copy()
        _amount = d.pop("amount", UNSET)
        amount: Union[Unset, MoneyInput]
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = MoneyInput.from_dict(_amount)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, AddressInput]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = AddressInput.from_dict(_billing_address)

        checkout_template_id = d.pop("checkoutTemplateId", UNSET)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CustomerInput]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CustomerInput.from_dict(_customer)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CheckoutCreateInputMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CheckoutCreateInputMetadata.from_dict(_metadata)

        reference = d.pop("reference", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ApplicationSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ApplicationSource(_source)

        success_url = d.pop("successUrl", UNSET)

        checkout_create_input = cls(
            amount=amount,
            billing_address=billing_address,
            checkout_template_id=checkout_template_id,
            customer=customer,
            metadata=metadata,
            reference=reference,
            source=source,
            success_url=success_url,
        )

        checkout_create_input.additional_properties = d
        return checkout_create_input

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
