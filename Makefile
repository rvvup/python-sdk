.PHONY: generate-client

clean:
	poetry run black .
	poetry run flake8

generate-openapi:
	poetry run openapi-python-client update --config openapi/config.yaml --path openapi/openapi.yaml

ping:
	poetry run python3 ping.py

tag:
	git tag $(poetry version -s)
	git push origin --tags

gen-2:
	docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
        -i /local/openapi/openapi.yaml \
        -g python \
        -o /local/out