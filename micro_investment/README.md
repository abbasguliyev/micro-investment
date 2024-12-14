# Micro Investment Backend
## Install
[https://github.com/abbasguliyev/micro-investment](https://github.com/abbasguliyev/micro-investment)
## Configuration
create .env file inside src folder, then copy and paste the contents from the .env.example file. \
## Run with Docker
docker-compose build \
docker-compose run --rm web python3 manage.py migrate \
docker-compose run --rm web python3 manage.py createsuperuser \
docker-compose up

