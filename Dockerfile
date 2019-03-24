FROM python:3.6.8-slim

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /load
COPY . .

EXPOSE 8089 5557 5558

CMD locust $LOCUST_OPTS -H $TARGET_URL $MODE
