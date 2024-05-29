from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


import datetime
from dateutil.parser import isoparse


T = TypeVar("T", bound="StartEnd")


@_attrs_define
class StartEnd:
    """Date range for the export.

    Attributes:
        end (datetime.datetime):
        start (datetime.datetime):
    """

    end: datetime.datetime
    start: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end = self.end.isoformat()

        start = self.start.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end = isoparse(d.pop("end"))

        start = isoparse(d.pop("start"))

        start_end = cls(
            end=end,
            start=start,
        )

        start_end.additional_properties = d
        return start_end

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
