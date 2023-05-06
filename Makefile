.PHONY: help all run clean
.DEFAULT_GOAL := run

PYTHON := python3.11
PIP    := pip3.11

help: ## Show help text
	@echo "Description:"
	@echo "  Quick build tool"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: clean install run ## Install libs and run the script

install: ## Install libs
	$(PIP) install python-dotenv pytz python-dateutil twitter

outdated: ## Show the outdated libs
	$(PIP) list --outdated

run: ## Run the script (default)
	$(PYTHON) main.py

clean: ## Delete the existing libs
	rm -rf ./__pycache__

