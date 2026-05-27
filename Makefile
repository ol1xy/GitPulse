.PHONY: shell

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

shell: $(VENV)/bin/activate
	@echo "entering venv, type exit to quit"
	@PATH=$(shell pwd)/$(VENV)/bin:$$PATH bash

.env:
	@echo "GITHUB_TOKEN=your_fine_grained_token_here" > .env

create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep

install-dep: $(VENV)/bin/activate .env
	$(PIP) install -r requirements.txt

install: $(VENV)/bin/activate
	$(PIP) install -e .

test-pytest: $(VENV)/bin/activate
	$(PYTHON) -m pytest
	
test: install-dep install test-pytest