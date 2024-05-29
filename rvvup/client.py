import json
import logging
from typing import Dict, Any, Optional

import httpx

from openapi.rvvup import AuthenticatedClient
from openapi.rvvup.api.webhooks import list_webhooks, create_webhook, update_webhook
from openapi.rvvup.models import (
    WebhookCreateInput,
    WebhookUpdateInput,
    WebhookEventType,
    WebhookStatus,
)


class RvvupClient:
    REDACTED = "***REDACTED***"

    def __init__(
        self,
        endpoint: str,
        merchant_id: str,
        auth_token: str,
        user_agent: str,
        logger: Optional[logging.Logger] = None,
        debug: bool = False,
    ):
        if not merchant_id or not auth_token or not endpoint:
            raise ValueError("Unable to initialize SDK, missing init parameters")

        self.endpoint = endpoint
        self.merchant_id = merchant_id
        self.auth_token = auth_token
        self.user_agent = user_agent
        self.logger = logger or logging.getLogger(__name__)
        self.debug = debug

        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}",
            "User-Agent": user_agent,
        }

    def get_available_payment_methods(
        self,
        cart_total: Optional[str] = None,
        currency: Optional[str] = None,
        input_options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        query = """
        query merchant ($id: ID!, $total: MoneyInput) {
            merchant (id: $id) {
                paymentMethods (search: {includeInactive: false, total: $total}) {
                    edges {
                        node {
                            name
                            displayName
                            description
                            summaryUrl
                            assets {
                                assetType
                                url
                                attributes
                            }
                            limits {
                                total {
                                    min
                                    max
                                    currency
                                }
                                expiresAt
                            }
                            settings {
                                assets {
                                    assetType
                                    url
                                    attributes
                                }
                                ... on PaypalPaymentMethodSettings {
                                    checkout {
                                        button {
                                            enabled
                                            layout {
                                                value
                                            }
                                            color {
                                                value
                                            }
                                            shape {
                                                value
                                            }
                                            label {
                                                value
                                            }
                                            tagline
                                            size
                                        }
                                        payLaterMessaging {
                                            enabled
                                            layout {
                                                value
                                            }
                                            logoType {
                                                value
                                            }
                                            logoPosition {
                                                value
                                            }
                                            textColor {
                                                value
                                            }
                                            textSize
                                            textAlignment {
                                                value
                                            }
                                            color {
                                                value
                                            }
                                            ratio {
                                                value
                                            }
                                        }
                                    }
                                    product {
                                        button {
                                            enabled
                                            layout {
                                                value
                                            }
                                            color {
                                                value
                                            }
                                            shape {
                                                value
                                            }
                                            label {
                                                value
                                            }
                                            tagline
                                            size
                                        }
                                        payLaterMessaging {
                                            enabled
                                            layout {
                                                value
                                            }
                                            logoType {
                                                value
                                            }
                                            logoPosition {
                                                value
                                            }
                                            textColor {
                                                value
                                            }
                                            textSize
                                            textAlignment {
                                                value
                                            }
                                            color {
                                                value
                                            }
                                            ratio {
                                                value
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        total = None
        if cart_total and currency:
            total = {
                "amount": cart_total,
                "currency": currency,
            }

        variables = {
            "id": self.merchant_id,
            "total": total,
        }

        try:
            response = self._do_request(query, variables, input_options)
        except Exception as e:
            self._log("Could not complete request {error}", {"error": str(e)})
            return {}

        response_methods = (
            response.get("data", {})
            .get("merchant", {})
            .get("paymentMethods", {})
            .get("edges", [])
        )
        methods = []
        for response_method in response_methods:
            method = response_method["node"]
            methods.append(
                {
                    "name": method["name"],
                    "displayName": method["displayName"],
                    "description": method["description"],
                    "summaryUrl": method["summaryUrl"],
                    "assets": method["assets"],
                    "limits": method["limits"],
                    "settings": method.get("settings"),
                }
            )

        return methods

    def create_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        mutation OrderCreate($input: OrderCreateInput!) {
            orderCreate(input: $input) {
                id
                status
                redirectToCheckoutUrl
                dashboardUrl
                paymentSummary {
                    paymentActions {
                        type
                        method
                        value
                    }
                }
            }
        }
        """
        return self._do_request(query, order_data)

    def update_express_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        mutation orderExpressUpdate ($input: OrderExpressUpdateInput!) {
            orderExpressUpdate(input: $input) {
                id
                type
                externalReference
                status
                dashboardUrl
                paymentSummary {
                    paymentActions {
                        type
                        method
                        value
                    }
                }
            }
        }
        """
        response = self._do_request(query, order_data)
        return response.get("data", {}).get("orderExpressUpdate", False)

    def get_order(self, order_id: str) -> Dict[str, Any]:
        query = """
        query order ($id: ID!, $merchant: IdInput!) {
            order (id: $id, merchant: $merchant) {
                id
                type
                externalReference
                total {
                    amount
                    currency
                }
                redirectToStoreUrl
                redirectToCheckoutUrl
                status
                dashboardUrl
            }
        }
        """
        variables = {
            "id": order_id,
            "merchant": {
                "id": self.merchant_id,
            },
        }

        response = self._do_request(query, variables)
        return response.get("data", {}).get("order", False)

    def is_order_refundable(self, order_id: str) -> bool:
        query = """
        query order ($id: ID!, $merchant: IdInput!) {
            order (id: $id, merchant: $merchant) {
                paymentSummary {
                    isRefundable
                }
            }
        }
        """
        variables = {
            "id": order_id,
            "merchant": {
                "id": self.merchant_id,
            },
        }
        response = self._do_request(query, variables)
        return (
            response.get("data", {})
            .get("order", {})
            .get("paymentSummary", {})
            .get("isRefundable", False)
        )

    def refund_order(
        self, order_id: str, amount: float, reason: str, idempotency: str
    ) -> Dict[str, Any]:
        query = """
        mutation orderRefund ($input: OrderRefundInput!) {
            orderRefund (input: $input) {
                id
                externalReference
                payments {
                  refunds {
                    id
                    status
                    reason
                  }
                }
            }
        }
        """
        variables = {
            "input": {
                "id": order_id,
                "merchant": {
                    "id": self.merchant_id,
                },
                "amount": {
                    "amount": amount,
                    "currency": "GBP",
                },
                "reason": reason,
                "idempotencyKey": idempotency,
            },
        }
        response = self._do_request(query, variables)
        return response.get("data", {}).get("orderRefund", False)

    def ping(self) -> bool:
        query = """
        query ping {
          ping {
            pong
          }
        }
        """
        response = self._do_request(query)
        return f"{response['data']['ping']['pong']}"

    def register_webhook(self, url: str) -> None:
        query = """
        mutation merchantWebhookCreate($input: WebhookCreateInput!) {
            merchantWebhookCreate(input: $input) {
                url
            }
        }
        """
        variables = {
            "input": {
                "url": url,
                "merchant": {
                    "id": self.merchant_id,
                },
            },
        }
        response = self._do_request(query, variables)
        if response.get("data", {}).get("merchantWebhookCreate", {}).get("url") != url:
            raise Exception("Response does not match specified URL")

    def create_event(
        self, event_type: str, reason: str, data: Optional[Dict[str, Any]] = None
    ) -> None:
        query = """
        mutation eventCreate($input: AuditLogCreateInput!) {
            eventCreate(input: $input) {
                id
            }
        }
        """
        variables = {
            "input": {
                "actionType": event_type,
                "merchant": {
                    "id": self.merchant_id,
                },
                # The resource the event refers to (order, merchant etc)
                "resourceId": self.merchant_id,
                "reason": reason,
                "currentData": data or {},
            },
        }
        self._do_request(query, variables)

    def refund_create(self, input: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        mutation refundCreate ($input: RefundCreateInput!) {
            refundCreate (input: $input) {
                id
                amount {
                    amount
                    currency
                }
                status
            }
        }
        """
        variables = {
            "input": {
                "orderId": input["orderId"],
                "merchantId": self.merchant_id,
                "amount": {
                    "amount": input["amount"],
                    "currency": input["currency"],
                },
                "reason": input["reason"],
                "idempotencyKey": input["idempotencyKey"],
            },
        }
        response = self._do_request(query, variables)
        return response.get("data", {}).get("refundCreate", False)

    def get_order_refunds(self, order_id: str) -> Dict[str, Any]:
        query = """
        query order ($id: ID!, $merchant: IdInput!) {
            order (id: $id, merchant: $merchant) {
                id
                payments {
                    id
                    refunds {
                        id
                        status
                        reason
                        amount {
                            amount
                            currency
                        }
                    }
                }
            }
        }
        """
        variables = {
            "id": order_id,
            "merchant": {
                "id": self.merchant_id,
            },
        }
        response = self._do_request(query, variables)
        return response.get("data", {}).get("order", {}).get("payments", False)

    def list_webhooks(self):
        result = list_webhooks.sync_detailed(
            self.merchant_id, client=self._rest_httpx_client()
        )
        return json.loads(result.content)

    def create_webhook(
        self, url: str, subscribed_events: list[str], headers: Dict[str, Any] = {}
    ) -> Dict[str, Any]:

        webhook = WebhookCreateInput(
            headers=headers,
            subscribed_events=subscribed_events,
            url=url,
        )
        result = create_webhook.sync_detailed(
            self.merchant_id,
            client=self._rest_httpx_client(),
            body=webhook,
        )
        return json.loads(result.content)

    def update_webhook(
        self,
        webhook_id: str,
        url: str,
        subscribed_events: list[str],
        status: str,
        headers: Dict[str, Any] = {},
    ) -> Dict[str, Any]:

        subscribed_events_enums = []
        for subscribed_event in subscribed_events:
            subscribed_events_enums.append(WebhookEventType(subscribed_event))

        webhook = WebhookUpdateInput(
            url=url,
            headers=headers,
            subscribed_events=subscribed_events_enums,
            status=WebhookStatus(status),
        )
        result = update_webhook.sync_detailed(
            self.merchant_id,
            webhook_id,
            client=self._rest_httpx_client(),
            body=webhook,
        )
        return json.loads(result.content)

    def _do_request(
        self,
        query: str,
        variables: Optional[Dict[str, Any]] = None,
        input_options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"query": query}
        if variables:
            data["variables"] = variables

        headers = self.headers.copy()

        if input_options and "headers" in input_options:
            headers.update(input_options.pop("headers"))

        options = {
            "json": data,
            "headers": headers,
        }

        if input_options:
            options.update(input_options)

        with httpx.Client() as client:
            response = client.post(self.endpoint, **options)
            response_data = response.json()

        debug_data = {
            "code": response.status_code,
            "requestHeaders": self._sanitise_request_headers(headers),
            "requestBody": self._sanitise_request_body(data),
            "responseHeaders": dict(response.headers),
            "responseBody": response_data,
        }

        if response.status_code == 200:
            if "errors" in response_data:
                self._log("GraphQL response error", debug_data)
                error_string = "\n".join(
                    [
                        f"{i + 1}: {error['message']}"
                        for i, error in enumerate(response_data["errors"])
                    ]
                )
                raise Exception(error_string)

            if self.debug:
                self._log("Successful GraphQL request", debug_data)

            return response_data

        self._log(f"Unexpected HTTP response code {debug_data}", debug_data)

        if 500 <= response.status_code < 600:
            raise Exception(
                "Network error returned via the API. "
                "Please use the same idempotency key if you retry."
            )

        raise Exception(f"Unexpected HTTP response code {debug_data}", debug_data)

    def _rest_httpx_client(self) -> AuthenticatedClient:
        c = AuthenticatedClient(
            base_url=self.endpoint.replace("/graphql", ""),
            token=self.auth_token,
        )

        return c

    def _log(self, message: str, context: Dict[str, Any]) -> None:
        if self.logger:
            self.logger.debug(message, extra=context)

    def _sanitise_request_body(self, request: Dict[str, Any]) -> Dict[str, Any]:
        redactable_keys = ["customer", "billingAddress", "shippingAddress"]
        if "variables" not in request or "input" not in request["variables"]:
            return request
        for key in redactable_keys:
            if key in request["variables"]["input"]:
                request["variables"]["input"][key] = self.REDACTED
        return request

    def _sanitise_request_headers(self, headers: Dict[str, Any]) -> Dict[str, Any]:
        if "Authorization" in headers:
            headers["Authorization"] = self.REDACTED
        return headers
