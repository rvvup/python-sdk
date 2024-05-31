from __future__ import annotations

import re  # noqa: F401
from typing import List

from openapi_client.api.checkout_templates_api import CheckoutTemplatesApi
from openapi_client.models.application_source import ApplicationSource
from openapi_client.models.checkout_amount_type import CheckoutAmountType
from openapi_client.models.checkout_apple_pay_settings_update_input import (
    CheckoutApplePaySettingsUpdateInput,
)
from openapi_client.models.checkout_card_settings_update_input import (
    CheckoutCardSettingsUpdateInput,
)
from openapi_client.models.checkout_customer_fields_input import (
    CheckoutCustomerFieldsInput,
)
from openapi_client.models.checkout_customer_fields_update_input import (
    CheckoutCustomerFieldsUpdateInput,
)
from openapi_client.models.checkout_pay_by_bank_settings_update_input import (
    CheckoutPayByBankSettingsUpdateInput,
)
from openapi_client.models.checkout_payment_method_settings_input import (
    CheckoutPaymentMethodSettingsInput,
)
from openapi_client.models.checkout_payment_method_settings_update_input import (
    CheckoutPaymentMethodSettingsUpdateInput,
)
from openapi_client.models.checkout_template import CheckoutTemplate
from openapi_client.models.checkout_template_create_input import (
    CheckoutTemplateCreateInput,
)
from openapi_client.models.checkout_template_update_input import (
    CheckoutTemplateUpdateInput,
)
from openapi_client.models.payment_method import PaymentMethod
from pydantic import StrictBool


class CheckoutTemplates:

    def __init__(self, client):
        self.client = client
        self.api = CheckoutTemplatesApi(self.client.api_client())

    def create(
        self,
        name: str,
        source: ApplicationSource,
        amount_type: CheckoutAmountType,
        enabled_payment_methods: List[PaymentMethod],
        customer_fields: CheckoutCustomerFieldsInput,
        payment_method_settings: CheckoutPaymentMethodSettingsInput,
        notify_customer: StrictBool = False,
        notify_merchant: StrictBool = False,
    ) -> CheckoutTemplate:
        template = CheckoutTemplateCreateInput(
            name=name,
            source=source,
            amount_type=amount_type,
            enabled_payment_methods=enabled_payment_methods,
            notify_customer=notify_customer,
            notify_merchant=notify_merchant,
            customer_fields=customer_fields,
            payment_method_settings=payment_method_settings,
        )

        result = self.api.create_checkout_template(
            merchant_id=self.client.merchant_id,
            checkout_template_create_input=template,
        )

        return result

    def get(self, checkout_template_id: str) -> CheckoutTemplate:
        template = self.api.get_checkout_template(
            checkout_template_id,
            self.client.merchant_id,
        )
        return template

    def find(self):
        page = self.api.list_checkout_templates(self.client.merchant_id)
        return page.results

    def update(self, template: CheckoutTemplate) -> CheckoutTemplate:
        update = CheckoutTemplateUpdateInput(
            name=template.name,
            source=template.source,
            amount_type=template.amount_type,
            enabled_payment_methods=template.enabled_payment_methods,
            notify_customer=template.notify_customer,
            notify_merchant=template.notify_merchant,
            customer_fields=CheckoutCustomerFieldsUpdateInput(
                optional=template.customer_fields.optional,
                required=template.customer_fields.required,
            ),
            payment_method_settings=CheckoutPaymentMethodSettingsUpdateInput(
                apple_pay=CheckoutApplePaySettingsUpdateInput(
                    capture_type=template.payment_method_settings.apple_pay.capture_type,
                    customer_fields=CheckoutCustomerFieldsUpdateInput(
                        optional=template.payment_method_settings.apple_pay.customer_fields.optional,
                        required=template.payment_method_settings.apple_pay.customer_fields.required,
                    ),
                ),
                card=CheckoutCardSettingsUpdateInput(
                    capture_type=template.payment_method_settings.card.capture_type,
                    customer_fields=CheckoutCustomerFieldsUpdateInput(
                        optional=template.payment_method_settings.card.customer_fields.optional,
                        required=template.payment_method_settings.card.customer_fields.required,
                    ),
                ),
                pay_by_bank=CheckoutPayByBankSettingsUpdateInput(
                    capture_type=template.payment_method_settings.pay_by_bank.capture_type,
                    customer_fields=CheckoutCustomerFieldsUpdateInput(
                        optional=template.payment_method_settings.pay_by_bank.customer_fields.optional,
                        required=template.payment_method_settings.pay_by_bank.customer_fields.required,
                    ),
                ),
            ),
        )

        result = self.api.update_checkout_template(
            template.id,
            merchant_id=self.client.merchant_id,
            checkout_template_update_input=update,
        )

        return result
