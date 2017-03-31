init:
	python manage.py makemigrations
	python manage.py migrate
	echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

run:
	python manage.py runserver 0.0.0.0:8000

test:
	python manage.py test

docker-rebuild:
	docker-compose down
	docker-compose up -d --build

docker-init:
	docker-compose up -d
	docker exec web python manage.py makemigrations
	docker exec web python manage.py migrate
	docker exec web echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell