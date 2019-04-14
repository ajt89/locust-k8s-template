FROM python:3.7.3-slim-stretch

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /load
COPY . .

EXPOSE 8089 5557 5558

CMD locust $LOCUST_OPTS -H $TARGET_URL $MODE
