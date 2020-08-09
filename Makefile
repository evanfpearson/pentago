export PYTHONPATH = src

test:
	python3 -m unittest -v src/game/tests.py
