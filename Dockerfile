FROM python:3.10-bullseye

RUN apt-get update
RUN apt -y install cron
RUN apt -y install systemctl
RUN systemctl enable cron
RUN apt install -y uwsgi
RUN apt install -y uwsgi-plugin-python3
RUN service uwsgi stop
RUN apt install -y nginx

WORKDIR /qrsave_app

COPY requirements.txt .
COPY manage.py .
COPY migrate.sh .
COPY qrsave-test.conf /etc/nginx/sites-enabled/qrsave-test.conf
COPY uwsgi_params .
COPY run.sh .

RUN chmod 777 migrate.sh
RUN chmod 777 run.sh

RUN pip3 install -r requirements.txt

COPY qrsave/ qrsave/
COPY qr/ qr/
COPY apphome/ apphome/

COPY django.ini /etc/uwsgi/apps-enabled/django.ini

EXPOSE 80
CMD ["./run.sh"]
