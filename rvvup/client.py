import logging
import os
from typing import Dict, Any, Optional

import httpx
import jwt
from openapi_client import Configuration, ApiClient

from .checkout_templates import CheckoutTemplates
from .checkouts import Checkouts
from .events import Events
from .orders import Orders
from .payment_links import PaymentLinks
from .payment_methods import PaymentMethods
from .payment_sessions import PaymentSessions
from .statements import Statements
from .webhooks import Webhooks


class RvvupClient:
    REDACTED = "***REDACTED***"

    def __init__(
        self,
        auth_token: str = None,
        user_agent: str = "rvvup-python-sdk/0.1.0",
        endpoint: str = None,
        merchant_id: str = None,
        logger: Optional[logging.Logger] = None,
        debug: bool = False,
    ):
        if not auth_token:
            token = os.environ["RVVUP_API_KEY"]

            if token is not None and len(token) > 0:
                auth_token = token
            else:
                raise ValueError("Unable to initialize SDK, missing JWT")

        self.auth_token = auth_token
        self.user_agent = user_agent

        payload = jwt.decode(auth_token, options={"verify_signature": False})

        # allow overrides but prefer payload
        self.endpoint = endpoint if endpoint is not None else payload.get("aud")
        self.merchant_id = (
            merchant_id if merchant_id is not None else payload.get("merchantId")
        )

        self.orders = Orders(self)
        self.webhooks = Webhooks(self)
        self.events = Events(self)
        self.payment_methods = PaymentMethods(self)
        self.checkout_templates = CheckoutTemplates(self)
        self.checkouts = Checkouts(self)
        self.payment_links = PaymentLinks(self)
        self.payment_sessions = PaymentSessions(self)
        self.statements = Statements(self)

        self.logger = logger or logging.getLogger(__name__)
        self.debug = debug

    def ping(self) -> str:
        query = """
        query ping {
          ping {
            pong
          }
        }
        """
        response = self.graphql(query)
        return f"{response['data']['ping']['pong']}"

    def api_client(self):

        configuration = Configuration(
            access_token=self.auth_token,
            host=self.endpoint.replace("/graphql", ""),
        )

        api_client = ApiClient(configuration)
        return api_client

    def graphql(
        self,
        query: str,
        variables: Optional[Dict[str, Any]] = None,
        input_options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        data = {"query": query}
        if variables:
            data["variables"] = variables

        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.auth_token}",
            "User-Agent": self.user_agent,
        }

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
                self.log("GraphQL response error", debug_data)
                error_string = "\n".join(
                    [
                        f"{i + 1}: {error['message']}"
                        for i, error in enumerate(response_data["errors"])
                    ]
                )
                raise Exception(error_string)

            if self.debug:
                self.log("Successful GraphQL request", debug_data)

            return response_data

        self.log(f"Unexpected HTTP response code {debug_data}", debug_data)

        if 500 <= response.status_code < 600:
            raise Exception(
                "Network error returned via the API. "
                "Please use the same idempotency key if you retry."
            )

        raise Exception(f"Unexpected HTTP response code {debug_data}", debug_data)

    def log(self, message: str, context: Dict[str, Any]) -> None:
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
