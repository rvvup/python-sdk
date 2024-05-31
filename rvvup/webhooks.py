from pprint import pprint
from typing import Dict, Any

from openapi_client.api.webhooks_api import WebhooksApi
from openapi_client.models.webhook import Webhook
from openapi_client.models.webhook_create_input import WebhookCreateInput
from openapi_client.models.webhook_event_type import WebhookEventType
from openapi_client.models.webhook_status import WebhookStatus
from openapi_client.models.webhook_update_input import WebhookUpdateInput


class Webhooks:

    def __init__(self, client):
        self.client = client
        self.api = WebhooksApi(self.client.api_client())

    def find(self):
        page = self.api.list_webhooks(self.client.merchant_id)
        return page.results

    def get(self, webhook_id: str):
        result = self.api.get_webhook(self.client.merchant_id, webhook_id)
        pprint(result)
        return result

    def create(
        self, url: str, subscribed_events: list[WebhookEventType], headers=None
    ) -> Webhook:
        webhook = WebhookCreateInput(
            url=url,
            subscribed_events=subscribed_events,
            status=WebhookStatus.ENABLED,
            headers={},
        )

        result = self.api.create_webhook(
            self.client.merchant_id,
            webhook,
        )

        return result

    def update(
        self,
        webhook_id: str,
        url: str,
        subscribed_events: list[WebhookEventType],
        status: WebhookStatus,
        headers=None,
    ) -> Dict[str, Any]:
        if headers is None:
            headers = {}

        webhook = WebhookUpdateInput(
            url=url,
            subscribed_events=subscribed_events,
            status=status,
        )

        result = self.api.update_webhook(
            self.client.merchant_id,
            webhook_id,
            webhook,
        )
        return result
