from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.checkout_template import CheckoutTemplate
from ...models.checkout_template_update_input import CheckoutTemplateUpdateInput


def _get_kwargs(
    merchant_id: str,
    checkout_template_id: str,
    *,
    body: CheckoutTemplateUpdateInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/2024-03-01/{merchant_id}/checkout-templates/{checkout_template_id}".format(
            merchant_id=merchant_id,
            checkout_template_id=checkout_template_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CheckoutTemplate]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CheckoutTemplate.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CheckoutTemplate]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    merchant_id: str,
    checkout_template_id: str,
    *,
    client: AuthenticatedClient,
    body: CheckoutTemplateUpdateInput,
) -> Response[Union[Any, CheckoutTemplate]]:
    """Update a checkout template

     Update a checkout template

    Args:
        merchant_id (str):
        checkout_template_id (str):
        body (CheckoutTemplateUpdateInput): The input for updating a checkout template. Example:
            {'name': 'My Checkout Template Updated', 'amountType': 'FIXED', 'enabledPaymentMethods':
            ['CARD', 'PAY_BY_BANK'], 'notifyCustomer': False, 'notifyMerchant': False,
            'customerFields': {'required': ['GIVEN_NAME', 'SURNAME', 'EMAIL'], 'optional':
            ['PHONE_NUMBER']}, 'paymentMethodSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckoutTemplate]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        checkout_template_id=checkout_template_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_id: str,
    checkout_template_id: str,
    *,
    client: AuthenticatedClient,
    body: CheckoutTemplateUpdateInput,
) -> Optional[Union[Any, CheckoutTemplate]]:
    """Update a checkout template

     Update a checkout template

    Args:
        merchant_id (str):
        checkout_template_id (str):
        body (CheckoutTemplateUpdateInput): The input for updating a checkout template. Example:
            {'name': 'My Checkout Template Updated', 'amountType': 'FIXED', 'enabledPaymentMethods':
            ['CARD', 'PAY_BY_BANK'], 'notifyCustomer': False, 'notifyMerchant': False,
            'customerFields': {'required': ['GIVEN_NAME', 'SURNAME', 'EMAIL'], 'optional':
            ['PHONE_NUMBER']}, 'paymentMethodSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckoutTemplate]
    """

    return sync_detailed(
        merchant_id=merchant_id,
        checkout_template_id=checkout_template_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    merchant_id: str,
    checkout_template_id: str,
    *,
    client: AuthenticatedClient,
    body: CheckoutTemplateUpdateInput,
) -> Response[Union[Any, CheckoutTemplate]]:
    """Update a checkout template

     Update a checkout template

    Args:
        merchant_id (str):
        checkout_template_id (str):
        body (CheckoutTemplateUpdateInput): The input for updating a checkout template. Example:
            {'name': 'My Checkout Template Updated', 'amountType': 'FIXED', 'enabledPaymentMethods':
            ['CARD', 'PAY_BY_BANK'], 'notifyCustomer': False, 'notifyMerchant': False,
            'customerFields': {'required': ['GIVEN_NAME', 'SURNAME', 'EMAIL'], 'optional':
            ['PHONE_NUMBER']}, 'paymentMethodSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckoutTemplate]]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        checkout_template_id=checkout_template_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_id: str,
    checkout_template_id: str,
    *,
    client: AuthenticatedClient,
    body: CheckoutTemplateUpdateInput,
) -> Optional[Union[Any, CheckoutTemplate]]:
    """Update a checkout template

     Update a checkout template

    Args:
        merchant_id (str):
        checkout_template_id (str):
        body (CheckoutTemplateUpdateInput): The input for updating a checkout template. Example:
            {'name': 'My Checkout Template Updated', 'amountType': 'FIXED', 'enabledPaymentMethods':
            ['CARD', 'PAY_BY_BANK'], 'notifyCustomer': False, 'notifyMerchant': False,
            'customerFields': {'required': ['GIVEN_NAME', 'SURNAME', 'EMAIL'], 'optional':
            ['PHONE_NUMBER']}, 'paymentMethodSettings': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckoutTemplate]
    """

    return (
        await asyncio_detailed(
            merchant_id=merchant_id,
            checkout_template_id=checkout_template_id,
            client=client,
            body=body,
        )
    ).parsed
