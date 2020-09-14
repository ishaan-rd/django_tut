FROM ubuntu
RUN apt update && apt install -y python3 python3-pip
RUN python3 --version

ADD ./django_tut /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 800

CMD exec gunicorn django_tut.wsgi:application --bind 0.0.0.0:8000 --workers 3
