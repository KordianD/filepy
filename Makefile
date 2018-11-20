all: clean test

fix:
	autopep8 filepy --recursive --in-place
	autopep8 test --recursive --in-place

test:
	pytest -v
	flake8 . --max-line-length 120
	py.test --cov filepy test

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

.PHONY: clean test
