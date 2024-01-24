## setup with docker
- create .env file with the required database informations
- install docker and docker compose
- do docker-compose up --build

## setup without docker
- create .env file with the required database informations
- create virtual enviornment
- python manage.py migrate
- python manage.py runserver