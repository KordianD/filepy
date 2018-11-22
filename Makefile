all: clean test

fix:
	autopep8 filepy --recursive --in-place
	autopep8 test --recursive --in-place

test:
	pytest -v
	py.test --cov filepy test
	flake8 . --max-line-length 120
	pylint --rcfile=standard.rc filepy test
	mypy --strict-optional filepy
	pyflakes .

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

.PHONY: clean test
