export PYTHONPATH = src

test:
	python3 -m unittest -v src/game/tests.py

coverage:
	coverage run -m unittest src/game/tests.py

run:
	python3 src/main.py
