FROM ubuntu:16.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get update
RUN apt-get install git python3-venv python3-dev build-essential nginx --yes

ADD ./ /opt/clarika-test/
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r /opt/clarika-test/requirements.txt

RUN rm -f /opt/clarika-test/clarika_test/db.sqlite3
RUN /opt/venv/bin/python /opt/clarika-test/clarika_test/manage.py migrate --no-input
RUN /opt/venv/bin/python /opt/clarika-test/clarika_test/manage.py loaddata /opt/clarika-test/clarika_test/data/base_data.json
RUN /opt/venv/bin/python /opt/clarika-test/clarika_test/manage.py collectstatic --no-input

ADD ./config/nginx-server /etc/nginx/sites-enabled/default
RUN service nginx restart

EXPOSE 80

ENTRYPOINT service nginx start && /opt/venv/bin/gunicorn --bind 0.0.0.0:8000 --chdir /opt/clarika-test/clarika_test clarika_test.wsgi
