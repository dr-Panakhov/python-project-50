install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check .
	uv run ruff check . --fix

test:
	uv run pytest
	
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml
