TARGET_URL = http://127.0.0.1:5000
TAG = active
DOCKER_HOST = ajt89


clean-locust:
	- rm -rf .venv

setup-locust:
	- python3 -m venv .venv; \
	. .venv/bin/activate; \
	pip install -r requirements.txt

update-locust:
	- . venv/bin/activate; \
	pip install -r requirements.txt

start-locust:
	- deactivate; \
	. venv/bin/activate; \
	pkill locust; \
	locust -H $(TARGET_URL)

build-docker-locust:
	- docker build -t $(DOCKER_HOST)/locust-k8s-template:$(TAG) .

push-tag-docker-locust:
	- docker push $(DOCKER_HOST)/locust-k8s-template:$(TAG)

clean-flask:
	- rm -rf app/.venv

setup-flask:
	- python3 -m venv app/.venv; \
	. app/.venv/bin/activate; \
	pip install -r app/requirements.txt

update-flask:
	- . app/venv/bin/activate; \
	pip install -r app/requirements.txt

start-flask:
	- . app/venv/bin/activate; \
	export FLASK_APP=app/app.py; \
	flask run

build-docker-flask:
	- docker build -t $(DOCKER_HOST)/simple-flask-app:$(TAG) app/

push-tag-docker-flask:
	- docker push $(DOCKER_HOST)/simple-flask-app:$(TAG)

