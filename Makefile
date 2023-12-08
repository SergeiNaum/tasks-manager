PORT ?= 8000

install:
	poetry install

dev:
	python manage.py runserver

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

lint:
	poetry run flake8 labels manager statuses task_manager tasks users

build:
	./build.sh

dump:
	python -Xutf8 manage.py dumpdata --indent=2 --exclude taggit -o db.json

loaddata:
	python manage.py loaddata db.json

localeRu:
	../manage.py makemessages -l ru

localeEn:
	../manage.py makemessages -l en

compileMessages:
	./manage.py compilemessages --ignore=.venv

.PHONY: install lint start
