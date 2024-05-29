from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.statement_export_request_export_format import (
    StatementExportRequestExportFormat,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_end import StartEnd


T = TypeVar("T", bound="StatementExportRequest")


@_attrs_define
class StatementExportRequest:
    """Request statement export.

    Attributes:
        export_format (StatementExportRequestExportFormat): Format for export.
        disbursement_batch_id (Union[Unset, str]):
        range_ (Union[Unset, StartEnd]): Date range for the export.
    """

    export_format: StatementExportRequestExportFormat
    disbursement_batch_id: Union[Unset, str] = UNSET
    range_: Union[Unset, "StartEnd"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_format = self.export_format.value

        disbursement_batch_id = self.disbursement_batch_id

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exportFormat": export_format,
            }
        )
        if disbursement_batch_id is not UNSET:
            field_dict["disbursementBatchId"] = disbursement_batch_id
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.start_end import StartEnd

        d = src_dict.copy()
        export_format = StatementExportRequestExportFormat(d.pop("exportFormat"))

        disbursement_batch_id = d.pop("disbursementBatchId", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, StartEnd]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = StartEnd.from_dict(_range_)

        statement_export_request = cls(
            export_format=export_format,
            disbursement_batch_id=disbursement_batch_id,
            range_=range_,
        )

        statement_export_request.additional_properties = d
        return statement_export_request

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
