from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook import Webhook
from ...types import Response


def _get_kwargs(
    merchant_id: str,
    webhook_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/2024-03-01/{merchant_id}/webhooks/{webhook_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Webhook]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Webhook.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
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
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Webhook]]:
    """Get a webhook by id

     Get a webhook by id

    Args:
        merchant_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Webhook]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Webhook]]:
    """Get a webhook by id

     Get a webhook by id

    Args:
        merchant_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Webhook]
    """

    return sync_detailed(
        merchant_id=merchant_id,
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    merchant_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Webhook]]:
    """Get a webhook by id

     Get a webhook by id

    Args:
        merchant_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Webhook]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Webhook]]:
    """Get a webhook by id

     Get a webhook by id

    Args:
        merchant_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Webhook]
    """

    return (
        await asyncio_detailed(
            merchant_id=merchant_id,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed