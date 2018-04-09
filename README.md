# django-simple-test
Just a test for django

## How to run:

### Usin Docker:

`sudo docker build . --tag simple-django:test`

`sudo docker run -d -p 8080:80 --name ckll -t simple-django:test`

Go to http://localhost:8080/admin/

username: admin
password: qweqwe123123

#### Stop docker

`sudo docker ps`

`sudo docker stop <IMAGE_ID>`

### Running in local machine

`python3 -m venv ./venv`

`source ./venv/bin/activate`

`cd simple-django-test`

`python manage.py migrate`

`python manage.py loaddata ../data/base_data.json`

Go to http://localhost:8000/admin/

username: admin
password: qweqwe123123
