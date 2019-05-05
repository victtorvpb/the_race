install:
	$(info ************  Not command ************)
execute:
	python3 execute.py
test:
	python -m unittest -v tests/tests_read_file_race.py tests/tests_the_race.py

