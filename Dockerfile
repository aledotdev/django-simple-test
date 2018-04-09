FROM ubuntu:16.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get update
RUN apt-get install git python3-venv python3-dev build-essential nginx --yes

ADD ./ /opt/simple_django/
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r /opt/simple_django/requirements.txt

RUN rm -f /opt/simple_django/simple_django/db.sqlite3
RUN /opt/venv/bin/python /opt/simple_django/simple_django/manage.py migrate --no-input
RUN /opt/venv/bin/python /opt/simple_django/simple_django/manage.py loaddata /opt/simple_django/data/base_data.json
RUN /opt/venv/bin/python /opt/simple_django/simple_django/manage.py collectstatic --no-input

ADD ./config/nginx-server /etc/nginx/sites-enabled/default
RUN service nginx restart

EXPOSE 80

ENTRYPOINT service nginx start && /opt/venv/bin/gunicorn --bind 0.0.0.0:8000 --chdir /opt/simple_django/simple_django simple_django.wsgi
