FROM python:3.10-bullseye

RUN apt-get update
RUN apt -y install cron
RUN apt -y install systemctl
RUN systemctl enable cron
RUN apt install -y uwsgi
RUN apt install -y uwsgi-plugin-python3
RUN service uwsgi stop

WORKDIR /qrsave_app

COPY requirements.txt .
COPY manage.py .
COPY start.sh .

RUN pip3 install -r requirements.txt

COPY qrsave/ qrsave/
COPY qr/ qr/
COPY django.ini /etc/uwsgi/apps-enabled/django.ini

RUN chmod +x start.sh

EXPOSE 8000
CMD ["start.sh"]
