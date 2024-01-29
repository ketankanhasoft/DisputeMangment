## setup with docker
- create .env file with the required database informations
- I have placed .env.example file in code, just rename it to .env, i have make sure it has correct information of database.
- install docker and docker compose
- do docker-compose up --build
- open http://127.0.0.1:8000/case-management/ in browser

## setup without docker
- create .env file with the required database informations
- create virtual enviornment
- python manage.py migrate
- python manage.py runserver
- open http://127.0.0.1:8000/case-management/ in browser


NOTE : Provided dockerfile and docker-compose.yml file is working fine with ubuntu and windows.