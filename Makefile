init:
	python ./src/manage.py makemigrations
	python ./src/manage.py migrate
	python ./src/manage.py createsuperuser --username admin --email admin@example.com

run:
	python ./src/manage.py runserver 0.0.0.0:8000

test:
	python ./src/manage.py test
