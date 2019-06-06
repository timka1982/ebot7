init:
	( \
  		apt install python3-venv; \
		python3 -m pip install --user virtualenv; \
		python3 -m venv coding_challenge; \
		. coding_challenge/bin/activate; \
		pip3 install -r requirements.txt; \
		python3 utils/generate_data.py; \
	)

test:
	nosetests tests

start:
	python3 main.py

multi:
	python3 resources/process_manager.py


