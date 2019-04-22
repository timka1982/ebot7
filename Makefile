init:
	pip3 install -r requirements.txt
	python3 utils/generate_data.py

test:
	nosetests tests

start:
	python3 main.py
