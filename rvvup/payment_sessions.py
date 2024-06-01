from openapi_client import PaymentSessionsApi, PaymentSessionCreateInput


class PaymentSessions:

    def __init__(self, client):
        self.client = client
        self.api = PaymentSessionsApi(self.client.api_client())

    def create(
        self, checkout_id: str, payment_session_create_input: PaymentSessionCreateInput
    ):
        result = self.api.create_payment_session(
            merchant_id=self.client.merchant_id,
            checkout_id=checkout_id,
            payment_session_create_input=payment_session_create_input,
        )
        return result

    def get(self, checkout_id: str, payment_session_id: str):
        result = self.api.get_payment_session(
            merchant_id=self.client.merchant_id,
            checkout_id=checkout_id,
            payment_session_id=payment_session_id,
        )
        return result
