FROM python:3.7.2-alpine3.9

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
COPY . .

ARG FLASK_APP=/app/app.py
CMD ["flask", "run", "--port", "8080"]
