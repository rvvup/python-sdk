from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from ..models.webhook_event_type import WebhookEventType
from typing import cast
from typing import Union

if TYPE_CHECKING:
    from ..models.webhook_create_input_headers_type_0 import (
        WebhookCreateInputHeadersType0,
    )


T = TypeVar("T", bound="WebhookCreateInput")


@_attrs_define
class WebhookCreateInput:
    """The input for creating a webhook.

    Attributes:
        headers (Union['WebhookCreateInputHeadersType0', None]): Custom headers for the webhook
        subscribed_events (List[WebhookEventType]): The events to subscribe to. Example: ['PAYMENT_SUCCEEDED',
            'REFUND_SUCCEEDED'].
        url (str): The URL to send the webhook event to. Example: https://example.com/webhook.
    """

    headers: Union["WebhookCreateInputHeadersType0", None]
    subscribed_events: List[WebhookEventType]
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.webhook_create_input_headers_type_0 import (
            WebhookCreateInputHeadersType0,
        )

        headers: Union[Dict[str, Any], None]
        if isinstance(self.headers, WebhookCreateInputHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        subscribed_events = []
        for subscribed_events_item_data in self.subscribed_events:
            subscribed_events_item = subscribed_events_item_data.value
            subscribed_events.append(subscribed_events_item)

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headers": headers,
                "subscribedEvents": subscribed_events,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_create_input_headers_type_0 import (
            WebhookCreateInputHeadersType0,
        )

        d = src_dict.copy()

        def _parse_headers(
            data: object,
        ) -> Union["WebhookCreateInputHeadersType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = WebhookCreateInputHeadersType0.from_dict(data)

                return headers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WebhookCreateInputHeadersType0", None], data)

        headers = _parse_headers(d.pop("headers"))

        subscribed_events = []
        _subscribed_events = d.pop("subscribedEvents")
        for subscribed_events_item_data in _subscribed_events:
            subscribed_events_item = WebhookEventType(subscribed_events_item_data)

            subscribed_events.append(subscribed_events_item)

        url = d.pop("url")

        webhook_create_input = cls(
            headers=headers,
            subscribed_events=subscribed_events,
            url=url,
        )

        webhook_create_input.additional_properties = d
        return webhook_create_input

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
