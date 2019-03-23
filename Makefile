LOCUST_CLASS = WebsiteUserA
TARGET_URL = http://127.0.0.1:5000

setup-locust:
	- virtualenv -p python3.7 venv; \
	. venv/bin/activate venv; \
	pip install -r requirements.txt

update-locust:
	- . venv/bin/activate; \
	pip install -r requirements.txt

start-locust:
	- deactivate; \
	. venv/bin/activate; \
	pkill locust; \
	locust -H $(TARGET_URL) --no-reset-stats $(LOCUST_CLASS)

setup-flask:
	- virtualenv -p python3.7 app/venv; \
	. app/venv/bin/activate; \
	pip install -r app/requirements.txt

update-flask:
	- . app/venv/bin/activate; \
	pip install -r app/requirements.txt

start-flask:
	- . app/venv/bin/activate; \
	export FLASK_APP=app/app.py; \
	flask run
