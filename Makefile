clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	flake8
	nosetests

perf:
	# measure duration
	python -m cProfile -o CACHE.prof test_perf_general.py
	snakeviz CACHE.prof 

api:
	openfisca serve --country-package openfisca_country_template --extensions openfisca_extension_template
