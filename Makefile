# Makefile for mold

.PHONY: help predoc

help:
	cat Makefile


# Generate the rst files from the json schema files

predoc:
	python extract_schema.py
