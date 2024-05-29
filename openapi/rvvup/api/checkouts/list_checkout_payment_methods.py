from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payment_method_details_page import PaymentMethodDetailsPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    merchant_id: str,
    checkout_id: str,
    *,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/2024-03-01/{merchant_id}/checkouts/{checkout_id}/payment-methods",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PaymentMethodDetailsPage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaymentMethodDetailsPage.from_dict(response.json())

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
) -> Response[Union[Any, PaymentMethodDetailsPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    merchant_id: str,
    checkout_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[Any, PaymentMethodDetailsPage]]:
    """Get payment methods for a checkout

     Lists the currently eligible payment methods for a checkout. The payment method status and checkout
    template settings are used to determine the eligible methods.

    Args:
        merchant_id (str):
        checkout_id (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaymentMethodDetailsPage]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        checkout_id=checkout_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_id: str,
    checkout_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, PaymentMethodDetailsPage]]:
    """Get payment methods for a checkout

     Lists the currently eligible payment methods for a checkout. The payment method status and checkout
    template settings are used to determine the eligible methods.

    Args:
        merchant_id (str):
        checkout_id (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaymentMethodDetailsPage]
    """

    return sync_detailed(
        merchant_id=merchant_id,
        checkout_id=checkout_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    merchant_id: str,
    checkout_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[Any, PaymentMethodDetailsPage]]:
    """Get payment methods for a checkout

     Lists the currently eligible payment methods for a checkout. The payment method status and checkout
    template settings are used to determine the eligible methods.

    Args:
        merchant_id (str):
        checkout_id (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaymentMethodDetailsPage]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        checkout_id=checkout_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_id: str,
    checkout_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, PaymentMethodDetailsPage]]:
    """Get payment methods for a checkout

     Lists the currently eligible payment methods for a checkout. The payment method status and checkout
    template settings are used to determine the eligible methods.

    Args:
        merchant_id (str):
        checkout_id (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaymentMethodDetailsPage]
    """

    return (
        await asyncio_detailed(
            merchant_id=merchant_id,
            checkout_id=checkout_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
