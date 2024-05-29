.PHONY: generate-client

clean:
	poetry run black .
	poetry run flake8

generate-openapi:
	poetry run openapi-python-client update --config openapi/config.yaml --path openapi/openapi.yaml

ping:
	poetry run python3 ping.py

