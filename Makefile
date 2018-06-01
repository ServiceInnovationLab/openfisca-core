#!/bin/bash
.PHONY: all clean test perf api


CORE_PERF_DIR=tests/core/performance


all: test

clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	flake8
	nosetests

perf:
	# measure duration
	python -m cProfile -o ${CORE_PERF_DIR}/CACHE.prof ${CORE_PERF_DIR}/test_perf_general.py
	snakeviz ${CORE_PERF_DIR}/CACHE.prof 

api:
	openfisca serve --country-package openfisca_country_template --extensions openfisca_extension_template
