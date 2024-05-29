import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_capture_type import PaymentCaptureType
from ..models.payment_decline_reason import PaymentDeclineReason
from ..models.payment_method import PaymentMethod
from ..models.payment_settlement_status import PaymentSettlementStatus
from ..models.payment_status import PaymentStatus
from ..models.payment_void_reason import PaymentVoidReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money
    from ..models.payment_summary import PaymentSummary


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """List of payments that have been made for the payment session.

    Attributes:
        amount (Money):
        capture_type (PaymentCaptureType): The capture type for the payment.
        created_at (datetime.datetime): The datetime when the payment was created.
        id (str): The unique ID for the payment.
        method (PaymentMethod): The payment method.
        payment_session_id (str): The ID of the payment session that the payment was created in.
        settlement_status (PaymentSettlementStatus): The settlement status of the payment.
        status (PaymentStatus): The status of the payment.
        summary (PaymentSummary):
        updated_at (datetime.datetime): The datetime when the payment was last updated.
        authorization_expires_at (Union[Unset, datetime.datetime]): The datetime when the payment's authorization
            expires.
        decline_reason (Union[Unset, PaymentDeclineReason]): The reason the payment was declined.
        void_reason (Union[Unset, PaymentVoidReason]): The reason the payment was voided.
    """

    amount: "Money"
    capture_type: PaymentCaptureType
    created_at: datetime.datetime
    id: str
    method: PaymentMethod
    payment_session_id: str
    settlement_status: PaymentSettlementStatus
    status: PaymentStatus
    summary: "PaymentSummary"
    updated_at: datetime.datetime
    authorization_expires_at: Union[Unset, datetime.datetime] = UNSET
    decline_reason: Union[Unset, PaymentDeclineReason] = UNSET
    void_reason: Union[Unset, PaymentVoidReason] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount.to_dict()

        capture_type = self.capture_type.value

        created_at = self.created_at.isoformat()

        id = self.id

        method = self.method.value

        payment_session_id = self.payment_session_id

        settlement_status = self.settlement_status.value

        status = self.status.value

        summary = self.summary.to_dict()

        updated_at = self.updated_at.isoformat()

        authorization_expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.authorization_expires_at, Unset):
            authorization_expires_at = self.authorization_expires_at.isoformat()

        decline_reason: Union[Unset, str] = UNSET
        if not isinstance(self.decline_reason, Unset):
            decline_reason = self.decline_reason.value

        void_reason: Union[Unset, str] = UNSET
        if not isinstance(self.void_reason, Unset):
            void_reason = self.void_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "captureType": capture_type,
                "createdAt": created_at,
                "id": id,
                "method": method,
                "paymentSessionId": payment_session_id,
                "settlementStatus": settlement_status,
                "status": status,
                "summary": summary,
                "updatedAt": updated_at,
            }
        )
        if authorization_expires_at is not UNSET:
            field_dict["authorizationExpiresAt"] = authorization_expires_at
        if decline_reason is not UNSET:
            field_dict["declineReason"] = decline_reason
        if void_reason is not UNSET:
            field_dict["voidReason"] = void_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.money import Money
        from ..models.payment_summary import PaymentSummary

        d = src_dict.copy()
        amount = Money.from_dict(d.pop("amount"))

        capture_type = PaymentCaptureType(d.pop("captureType"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        method = PaymentMethod(d.pop("method"))

        payment_session_id = d.pop("paymentSessionId")

        settlement_status = PaymentSettlementStatus(d.pop("settlementStatus"))

        status = PaymentStatus(d.pop("status"))

        summary = PaymentSummary.from_dict(d.pop("summary"))

        updated_at = isoparse(d.pop("updatedAt"))

        _authorization_expires_at = d.pop("authorizationExpiresAt", UNSET)
        authorization_expires_at: Union[Unset, datetime.datetime]
        if isinstance(_authorization_expires_at, Unset):
            authorization_expires_at = UNSET
        else:
            authorization_expires_at = isoparse(_authorization_expires_at)

        _decline_reason = d.pop("declineReason", UNSET)
        decline_reason: Union[Unset, PaymentDeclineReason]
        if isinstance(_decline_reason, Unset):
            decline_reason = UNSET
        else:
            decline_reason = PaymentDeclineReason(_decline_reason)

        _void_reason = d.pop("voidReason", UNSET)
        void_reason: Union[Unset, PaymentVoidReason]
        if isinstance(_void_reason, Unset):
            void_reason = UNSET
        else:
            void_reason = PaymentVoidReason(_void_reason)

        payment = cls(
            amount=amount,
            capture_type=capture_type,
            created_at=created_at,
            id=id,
            method=method,
            payment_session_id=payment_session_id,
            settlement_status=settlement_status,
            status=status,
            summary=summary,
            updated_at=updated_at,
            authorization_expires_at=authorization_expires_at,
            decline_reason=decline_reason,
            void_reason=void_reason,
        )

        payment.additional_properties = d
        return payment

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
