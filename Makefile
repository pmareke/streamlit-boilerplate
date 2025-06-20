.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

pre-requirements:
	@scripts/pre-requirements.sh

.PHONY: local-setup
local-setup: pre-requirements ## Install hooks and packages
	scripts/local-setup.sh
	make install

.PHONY: build
build: pre-requirements ## Generate Docker image
	docker build -t streamlit-boilerplate .

.PHONY: up
up: pre-requirements build ## Run the app inside docker
	docker run -p 8501:8501 streamlit-boilerplate

.PHONY: install
install: pre-requirements ## Install the app packages
	uv python install 3.12.8
	uv python pin 3.12.8
	uv sync --no-install-project

.PHONY: update
update: pre-requirements ## Updates the app packages
	uv lock --upgrade

.PHONY: add-dev-package
add-dev-package: pre-requirements ## Installs a new package in the app. ex: make add-dev-package package=XXX
	uv add --dev $(package)

.PHONY: add-package
add-package: pre-requirements ## Installs a new package in the app. ex: make add-package package=XXX
	uv add $(package)

.PHONY: run
run: pre-requirements ## Runs the app in production mode
	PYTHONPATH=. streamlit run main.py

.PHONY: check-typing
check-typing: pre-requirements  ## Run a static analyzer over the code to find issues
	ty check .

.PHONY: check-lint
check-lint: pre-requirements ## Checks the code style
	ruff check

.PHONY: lint
lint: pre-requirements ## Lints the code format
	ruff check --fix

.PHONY: check-format
check-format: pre-requirements  ## Check format python code
	ruff format --check

.PHONY: format
format: pre-requirements  ## Format python code
	ruff format

.PHONY: checks
checks: pre-requirements check-lint check-format check-typing  ## Run all checks

.PHONY: test-unit
test-unit: pre-requirements ## Run unit tests
	pytest tests/unit -ra -x --durations=5

.PHONY: test-integration
test-integration: pre-requirements ## Run integration tests
	pytest tests/integration -ra -x --durations=5

.PHONY: test
test: test-unit test-integration ## Run all the tests

.PHONY: watch
watch: pre-requirements ## Run all the tests in watch mode
	ptw --runner "pytest tests -ra -x --durations=5"

.PHONY: pre-commit
pre-commit: pre-requirements check-lint check-format check-typing test-unit

.PHONY: pre-push
pre-push: pre-requirements test-integration
