PYTHON ?= python3.12
POETRY ?= poetry
HOST ?= 127.0.0.1
PORT ?= 8000

.PHONY: setup run quality test

setup: ## Crée le venv (.venv) et installe les dépendances
	$(POETRY) config virtualenvs.in-project true --local
	$(POETRY) env use $(PYTHON)
	$(POETRY) install

run: ## Lance l'API en local (Swagger : http://$(HOST):$(PORT)/docs)
	$(POETRY) run uvicorn app.main:app --reload --host $(HOST) --port $(PORT)

quality: ## Formatage + lint (ruff) et typage (mypy)
	$(POETRY) run ruff format .
	$(POETRY) run ruff check --fix .
	$(POETRY) run mypy app tests

test: ## Lance les tests pytest
	$(POETRY) run pytest -v
