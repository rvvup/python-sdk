from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook import Webhook
from ...models.webhook_create_input import WebhookCreateInput
from ...types import Response


def _get_kwargs(
    merchant_id: str,
    *,
    body: WebhookCreateInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/2024-03-01/{merchant_id}/webhooks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Webhook]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Webhook.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Webhook]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    merchant_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookCreateInput,
) -> Response[Union[Any, Webhook]]:
    """Create a new webhook

     Create a new webhook

    Args:
        merchant_id (str):
        body (WebhookCreateInput): The input for creating a webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Webhook]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookCreateInput,
) -> Optional[Union[Any, Webhook]]:
    """Create a new webhook

     Create a new webhook

    Args:
        merchant_id (str):
        body (WebhookCreateInput): The input for creating a webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Webhook]
    """

    return sync_detailed(
        merchant_id=merchant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    merchant_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookCreateInput,
) -> Response[Union[Any, Webhook]]:
    """Create a new webhook

     Create a new webhook

    Args:
        merchant_id (str):
        body (WebhookCreateInput): The input for creating a webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Webhook]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookCreateInput,
) -> Optional[Union[Any, Webhook]]:
    """Create a new webhook

     Create a new webhook

    Args:
        merchant_id (str):
        body (WebhookCreateInput): The input for creating a webhook.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Webhook]
    """

    return (
        await asyncio_detailed(
            merchant_id=merchant_id,
            client=client,
            body=body,
        )
    ).parsed
