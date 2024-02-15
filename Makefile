PORT ?= 8000
start: 
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application 

install:
	poetry install

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

lint:
	poetry run flake8 task_manager --exclude migrations

test:
	poetry run python3 manage.py test

translate:
	poetry run python manage.py makemessages -l ru
	poetry run python manage.py compilemessages

render:
	poetry install
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate