all: clean test

fix:
	autopep8 filepy --recursive --in-place
	autopep8 test --recursive --in-place

test:
	pytest -vv
	py.test --cov  filepy test --cov-report term-missing
	flake8 filepy test --max-line-length 120
	pylint --rcfile=standard.rc --disable=missing-docstring filepy test
	mypy --strict-optional filepy
	pyflakes .

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

.PHONY: clean test
