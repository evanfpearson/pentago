export PYTHONPATH = src

test:
	python3 -m unittest -v src/game/tests.py

coverage:
	coverage run --source src/game -m unittest src/game/tests.py
	coverage report

run:
	python3 src/main.py
