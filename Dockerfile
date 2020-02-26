FROM python:3.6

COPY . /app
WORKDIR /app

RUN chmod +x run_test.sh

RUN export PYTHONPATH=/app

RUN pip install -r requirements.txt

CMD python main.py --html_path="/app/example.html"
