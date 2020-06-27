FROM python:3.6.10-alpine3.12

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
COPY . .

ARG FLASK_APP=/app/app.py

EXPOSE 8080

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
