.PHONY: shell

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

shell: $(VENV)/bin/activate
	@echo "entering venv, type exit to quit"
	@PATH=$(shell pwd)/$(VENV)/bin:$$PATH bash

create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	python3 -m pytest

test: install-dep install test-pytest