from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.item_restriction import ItemRestriction
from typing import Union

if TYPE_CHECKING:
    from ..models.money_input import MoneyInput


T = TypeVar("T", bound="ItemInput")


@_attrs_define
class ItemInput:
    """An item that the customer is purchasing.

    Attributes:
        name (str): The name of the item.
        price (MoneyInput):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        quantity (str): The quantity of the item being purchased.
        sku (str): Stock keeping unit - the unique identifier for the item.
        total (MoneyInput):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        price_with_tax (Union[Unset, MoneyInput]):  Example: {'amount': '100.00', 'currency': 'GBP'}.
        restriction (Union[Unset, ItemRestriction]): Indicator of restrictions on the item. Some payment methods are
            unavailable for restricted items.
        tax (Union[Unset, MoneyInput]):  Example: {'amount': '100.00', 'currency': 'GBP'}.
    """

    name: str
    price: "MoneyInput"
    quantity: str
    sku: str
    total: "MoneyInput"
    price_with_tax: Union[Unset, "MoneyInput"] = UNSET
    restriction: Union[Unset, ItemRestriction] = UNSET
    tax: Union[Unset, "MoneyInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        price = self.price.to_dict()

        quantity = self.quantity

        sku = self.sku

        total = self.total.to_dict()

        price_with_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_with_tax, Unset):
            price_with_tax = self.price_with_tax.to_dict()

        restriction: Union[Unset, str] = UNSET
        if not isinstance(self.restriction, Unset):
            restriction = self.restriction.value

        tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "price": price,
                "quantity": quantity,
                "sku": sku,
                "total": total,
            }
        )
        if price_with_tax is not UNSET:
            field_dict["priceWithTax"] = price_with_tax
        if restriction is not UNSET:
            field_dict["restriction"] = restriction
        if tax is not UNSET:
            field_dict["tax"] = tax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money_input import MoneyInput

        d = src_dict.copy()
        name = d.pop("name")

        price = MoneyInput.from_dict(d.pop("price"))

        quantity = d.pop("quantity")

        sku = d.pop("sku")

        total = MoneyInput.from_dict(d.pop("total"))

        _price_with_tax = d.pop("priceWithTax", UNSET)
        price_with_tax: Union[Unset, MoneyInput]
        if isinstance(_price_with_tax, Unset):
            price_with_tax = UNSET
        else:
            price_with_tax = MoneyInput.from_dict(_price_with_tax)

        _restriction = d.pop("restriction", UNSET)
        restriction: Union[Unset, ItemRestriction]
        if isinstance(_restriction, Unset):
            restriction = UNSET
        else:
            restriction = ItemRestriction(_restriction)

        _tax = d.pop("tax", UNSET)
        tax: Union[Unset, MoneyInput]
        if isinstance(_tax, Unset):
            tax = UNSET
        else:
            tax = MoneyInput.from_dict(_tax)

        item_input = cls(
            name=name,
            price=price,
            quantity=quantity,
            sku=sku,
            total=total,
            price_with_tax=price_with_tax,
            restriction=restriction,
            tax=tax,
        )

        item_input.additional_properties = d
        return item_input

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
