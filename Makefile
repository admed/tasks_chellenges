.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:	## Build project with compose
	docker-compose build

.PHONY: up
up:	## Run project with compose
	docker-compose up

.PHONY: down
down: ## Reset project containers with compose
	docker-compose down

.PHONY: lock
lock:	## Refresh pipfile.lock
	pipenv lock --pre

.PHONY: requirements
requirements:	## Refresh requirements.txt from pipfile.lock
	pipenv lock -r > requirements.txt

.PHONY: test
test:	## Run project tests
	docker-compose run --rm web pytest -vv

.PHONY: py-upgrade
py-upgrade:	## Upgrade project py files with pyupgrade library for python version 3.9
	docker-compose run --rm web pyupgrade --py39-plus `find . -name "*.py"`

.PHONY: lint
lint:  ## Linter project code.
	black --line-length=120 . --exclude="/(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|\.svn|_build|buck-out|build|dist|fixtures)/"
	isort .
	flake8 --config .flake8 .

.PHONY: hook-install
hook-install: ## install pre-commit git hook
	pre-commit install

.PHONY: hook-run
hook-run: ## run pre-commit git hook without committing code
	pre-commit run

.PHONY: hook-uninstall
hook-uninstall: ## uninstall pre-commit git hook
	pre-commit uninstall