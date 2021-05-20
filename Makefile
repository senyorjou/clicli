POETRY ?= poetry
.PHONY: clean install install-dev format lint


clean:
	find . -name '__pycache__' | xargs rm -rf
	find . -type f -name "*.pyc" -delete

install-dev:
	$(POETRY) install

install:
	$(POETRY) install  --no-dev

format:
	$(POETRY) run isort .
	$(POETRY) run black .

lint:
	$(POETRY) run isort --check-only .
	$(POETRY) run black --check .
	$(POETRY) run flake8 --config setup.cfg
