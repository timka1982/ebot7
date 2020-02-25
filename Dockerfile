FROM python:3.6

COPY . /app
WORKDIR /app

CMD python main.py --html_path="/app/example.html"
