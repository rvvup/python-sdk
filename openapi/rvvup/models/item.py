import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.item_restriction import ItemRestriction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """List of items that the customer is purchasing.

    Attributes:
        created_at (datetime.datetime): The datetime when the item was created.
        id (str): The unique ID for the item.
        name (str): The name of the item.
        price (Money):
        quantity (str): The quantity of the item being purchased.
        restriction (ItemRestriction): Indicator of restrictions on the item. Some payment methods are unavailable for
            restricted items.
        sku (str): Stock keeping unit - the unique identifier for the item.
        total (Money):
        price_with_tax (Union[Unset, Money]):
        tax (Union[Unset, Money]):
    """

    created_at: datetime.datetime
    id: str
    name: str
    price: "Money"
    quantity: str
    restriction: ItemRestriction
    sku: str
    total: "Money"
    price_with_tax: Union[Unset, "Money"] = UNSET
    tax: Union[Unset, "Money"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        price = self.price.to_dict()

        quantity = self.quantity

        restriction = self.restriction.value

        sku = self.sku

        total = self.total.to_dict()

        price_with_tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_with_tax, Unset):
            price_with_tax = self.price_with_tax.to_dict()

        tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
                "price": price,
                "quantity": quantity,
                "restriction": restriction,
                "sku": sku,
                "total": total,
            }
        )
        if price_with_tax is not UNSET:
            field_dict["priceWithTax"] = price_with_tax
        if tax is not UNSET:
            field_dict["tax"] = tax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money

        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        price = Money.from_dict(d.pop("price"))

        quantity = d.pop("quantity")

        restriction = ItemRestriction(d.pop("restriction"))

        sku = d.pop("sku")

        total = Money.from_dict(d.pop("total"))

        _price_with_tax = d.pop("priceWithTax", UNSET)
        price_with_tax: Union[Unset, Money]
        if isinstance(_price_with_tax, Unset):
            price_with_tax = UNSET
        else:
            price_with_tax = Money.from_dict(_price_with_tax)

        _tax = d.pop("tax", UNSET)
        tax: Union[Unset, Money]
        if isinstance(_tax, Unset):
            tax = UNSET
        else:
            tax = Money.from_dict(_tax)

        item = cls(
            created_at=created_at,
            id=id,
            name=name,
            price=price,
            quantity=quantity,
            restriction=restriction,
            sku=sku,
            total=total,
            price_with_tax=price_with_tax,
            tax=tax,
        )

        item.additional_properties = d
        return item

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
