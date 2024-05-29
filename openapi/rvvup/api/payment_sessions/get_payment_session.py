from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payment_session import PaymentSession
from ...types import Response


def _get_kwargs(
    merchant_id: str,
    checkout_id: str,
    payment_session_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/2024-03-01/{merchant_id}/checkouts/{checkout_id}/payment-sessions/{payment_session_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PaymentSession]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaymentSession.from_dict(response.json())

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
) -> Response[Union[Any, PaymentSession]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    merchant_id: str,
    checkout_id: str,
    payment_session_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, PaymentSession]]:
    """Get a payment session

     Get a payment session by id.

    Args:
        merchant_id (str):
        checkout_id (str):
        payment_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaymentSession]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        checkout_id=checkout_id,
        payment_session_id=payment_session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_id: str,
    checkout_id: str,
    payment_session_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, PaymentSession]]:
    """Get a payment session

     Get a payment session by id.

    Args:
        merchant_id (str):
        checkout_id (str):
        payment_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaymentSession]
    """

    return sync_detailed(
        merchant_id=merchant_id,
        checkout_id=checkout_id,
        payment_session_id=payment_session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    merchant_id: str,
    checkout_id: str,
    payment_session_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, PaymentSession]]:
    """Get a payment session

     Get a payment session by id.

    Args:
        merchant_id (str):
        checkout_id (str):
        payment_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaymentSession]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        checkout_id=checkout_id,
        payment_session_id=payment_session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_id: str,
    checkout_id: str,
    payment_session_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, PaymentSession]]:
    """Get a payment session

     Get a payment session by id.

    Args:
        merchant_id (str):
        checkout_id (str):
        payment_session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaymentSession]
    """

    return (
        await asyncio_detailed(
            merchant_id=merchant_id,
            checkout_id=checkout_id,
            payment_session_id=payment_session_id,
            client=client,
        )
    ).parsed
