init:
	pip3 install -r requirements.txt

test:
	nosetests tests

start:
	python3 main.py
