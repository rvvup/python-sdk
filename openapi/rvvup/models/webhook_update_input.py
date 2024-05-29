from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_type import WebhookEventType
from ..models.webhook_status import WebhookStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_update_input_headers_type_0 import (
        WebhookUpdateInputHeadersType0,
    )


T = TypeVar("T", bound="WebhookUpdateInput")


@_attrs_define
class WebhookUpdateInput:
    """The input for updating a webhook.

    Attributes:
        headers (Union['WebhookUpdateInputHeadersType0', None, Unset]): Custom headers for the webhook
        status (Union[Unset, WebhookStatus]): The status of the webhook.
        subscribed_events (Union[Unset, List[WebhookEventType]]): The events to subscribe to. Example:
            ['PAYMENT_SUCCEEDED'].
        url (Union[Unset, str]): The URL to send the webhook event to. Example: https://example.com/new/webhook.
    """

    headers: Union["WebhookUpdateInputHeadersType0", None, Unset] = UNSET
    status: Union[Unset, WebhookStatus] = UNSET
    subscribed_events: Union[Unset, List[WebhookEventType]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.webhook_update_input_headers_type_0 import (
            WebhookUpdateInputHeadersType0,
        )

        headers: Union[Dict[str, Any], None, Unset]
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, WebhookUpdateInputHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        subscribed_events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subscribed_events, Unset):
            subscribed_events = []
            for subscribed_events_item_data in self.subscribed_events:
                subscribed_events_item = subscribed_events_item_data.value
                subscribed_events.append(subscribed_events_item)

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if status is not UNSET:
            field_dict["status"] = status
        if subscribed_events is not UNSET:
            field_dict["subscribedEvents"] = subscribed_events
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_update_input_headers_type_0 import (
            WebhookUpdateInputHeadersType0,
        )

        d = src_dict.copy()

        def _parse_headers(
            data: object,
        ) -> Union["WebhookUpdateInputHeadersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = WebhookUpdateInputHeadersType0.from_dict(data)

                return headers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WebhookUpdateInputHeadersType0", None, Unset], data)

        headers = _parse_headers(d.pop("headers", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WebhookStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WebhookStatus(_status)

        subscribed_events = []
        _subscribed_events = d.pop("subscribedEvents", UNSET)
        for subscribed_events_item_data in _subscribed_events or []:
            subscribed_events_item = WebhookEventType(subscribed_events_item_data)

            subscribed_events.append(subscribed_events_item)

        url = d.pop("url", UNSET)

        webhook_update_input = cls(
            headers=headers,
            status=status,
            subscribed_events=subscribed_events,
            url=url,
        )

        webhook_update_input.additional_properties = d
        return webhook_update_input

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
