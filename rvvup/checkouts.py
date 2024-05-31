from openapi_client.api import CheckoutsApi


class Checkouts:

    def __init__(self, client):
        self.client = client
        self.api = CheckoutsApi(self.client.api_client())

    def create(self, checkout, idempotency_key: str):
        result = self.api.create_checkout(
            merchant_id=self.client.merchant_id,
            checkout_create_input=checkout,
            idempotency_key=idempotency_key,
        )
        return result

    def find(self):
        page = self.api.list_checkouts(self.client.merchant_id)
        return page

    def get(self, checkout_id):
        result = self.api.get_checkout(checkout_id, self.client.merchant_id)
        return result

    def list_checkout_payment_methods(self, checkout_id):
        result = self.api.list_checkout_payment_methods(
            checkout_id, self.client.merchant_id
        )
        return result
