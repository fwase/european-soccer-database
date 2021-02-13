.PHONY: packages
packages:
	@pipenv sync

.PHONY: dev-packages
dev-packages:
	@pipenv sync --dev

.PHONY: lint
lint: ISORT_OPTIONS := --check-only
lint: BLACK_OPTIONS := --check
lint: format
	@pipenv run flake8 ./scripts

.PHONY: format
format:
	@pipenv run isort ./scripts $(ISORT_OPTIONS)
	@pipenv run black ./scripts $(BLACK_OPTIONS)
