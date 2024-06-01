from typing import Any

from openapi_client.api.statement_exports_api import StatementExportsApi
from openapi_client.models.statement_export_request import StatementExportRequest


class Statements:

    def __init__(self, client):
        self.client = client
        self.api = StatementExportsApi(self.client.api_client())

    def export(self, export: StatementExportRequest) -> Any:
        return self.api.export_statement_with_http_info(
            self.client.merchant_id, export
        ).data
