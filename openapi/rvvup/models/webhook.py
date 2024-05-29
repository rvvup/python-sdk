from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from ..models.webhook_event_type import WebhookEventType
from ..models.webhook_status import WebhookStatus

if TYPE_CHECKING:
    from ..models.webhook_headers import WebhookHeaders


T = TypeVar("T", bound="Webhook")


@_attrs_define
class Webhook:
    """
    Attributes:
        headers (WebhookHeaders): Custom headers for the webhook.
        id (str): The unique ID of the webhook.
        merchant_id (str): The ID of the merchant that the webhook belongs to.
        status (WebhookStatus): The status of the webhook.
        subscribed_events (List[WebhookEventType]): The events that the webhook is subscribed to.
        url (str): The URL to send the webhook events to.
    """

    headers: "WebhookHeaders"
    id: str
    merchant_id: str
    status: WebhookStatus
    subscribed_events: List[WebhookEventType]
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers = self.headers.to_dict()

        id = self.id

        merchant_id = self.merchant_id

        status = self.status.value

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
                "id": id,
                "merchantId": merchant_id,
                "status": status,
                "subscribedEvents": subscribed_events,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_headers import WebhookHeaders

        d = src_dict.copy()
        headers = WebhookHeaders.from_dict(d.pop("headers"))

        id = d.pop("id")

        merchant_id = d.pop("merchantId")

        status = WebhookStatus(d.pop("status"))

        subscribed_events = []
        _subscribed_events = d.pop("subscribedEvents")
        for subscribed_events_item_data in _subscribed_events:
            subscribed_events_item = WebhookEventType(subscribed_events_item_data)

            subscribed_events.append(subscribed_events_item)

        url = d.pop("url")

        webhook = cls(
            headers=headers,
            id=id,
            merchant_id=merchant_id,
            status=status,
            subscribed_events=subscribed_events,
            url=url,
        )

        webhook.additional_properties = d
        return webhook

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
