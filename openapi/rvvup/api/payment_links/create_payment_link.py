from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.payment_link import PaymentLink
from ...types import Unset
from ...models.payment_link_create_input import PaymentLinkCreateInput


def _get_kwargs(
    merchant_id: str,
    *,
    body: PaymentLinkCreateInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/2024-03-01/{merchant_id}/payment-links".format(
            merchant_id=merchant_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PaymentLink]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaymentLink.from_dict(response.json())

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
) -> Response[Union[Any, PaymentLink]]:
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
    body: PaymentLinkCreateInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PaymentLink]]:
    """Create new payment link

     Creates a new payment link. User can choose whether to make it reusable

    Args:
        merchant_id (str):
        idempotency_key (Union[Unset, str]):
        body (PaymentLinkCreateInput): The input for creating a payment link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaymentLink]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_id: str,
    *,
    client: AuthenticatedClient,
    body: PaymentLinkCreateInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PaymentLink]]:
    """Create new payment link

     Creates a new payment link. User can choose whether to make it reusable

    Args:
        merchant_id (str):
        idempotency_key (Union[Unset, str]):
        body (PaymentLinkCreateInput): The input for creating a payment link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaymentLink]
    """

    return sync_detailed(
        merchant_id=merchant_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    merchant_id: str,
    *,
    client: AuthenticatedClient,
    body: PaymentLinkCreateInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PaymentLink]]:
    """Create new payment link

     Creates a new payment link. User can choose whether to make it reusable

    Args:
        merchant_id (str):
        idempotency_key (Union[Unset, str]):
        body (PaymentLinkCreateInput): The input for creating a payment link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaymentLink]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_id: str,
    *,
    client: AuthenticatedClient,
    body: PaymentLinkCreateInput,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PaymentLink]]:
    """Create new payment link

     Creates a new payment link. User can choose whether to make it reusable

    Args:
        merchant_id (str):
        idempotency_key (Union[Unset, str]):
        body (PaymentLinkCreateInput): The input for creating a payment link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaymentLink]
    """

    return (
        await asyncio_detailed(
            merchant_id=merchant_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
