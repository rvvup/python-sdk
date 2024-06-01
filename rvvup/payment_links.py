from typing import List

from openapi_client.api.payment_links_api import PaymentLinksApi
from openapi_client.models.payment_link import PaymentLink
from openapi_client.models.payment_link_create_input import PaymentLinkCreateInput


class PaymentLinks:

    def __init__(self, client):
        self.client = client
        self.api = PaymentLinksApi(self.client.api_client())

    def create(
        self, paymentLinkCreateInput: PaymentLinkCreateInput, idempotency_key: str
    ) -> PaymentLink:
        result = self.api.create_payment_link(
            self.client.merchant_id, paymentLinkCreateInput, idempotency_key
        )
        return result

    def find(self) -> List[PaymentLink]:
        page = self.api.list_payment_links(self.client.merchant_id)
        return page.results

    def get(self, payment_link_id: str) -> PaymentLink:
        result = self.api.get_payment_link(payment_link_id, self.client.merchant_id)
        return result

    def deactivate(self, payment_link_id: str) -> PaymentLink:
        result = self.api.deactivate_payment_link(
            payment_link_id, self.client.merchant_id
        )
        return result
