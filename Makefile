# Makefile for mold

.PHONY: help predoc

help:
	cat Makefile


# Generate the rst files from the json schema files

doc:
    python extract_document_schema.py
	python extract_resource_schema.py
	cd docs && make html
