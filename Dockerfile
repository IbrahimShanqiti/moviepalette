FROM python:3.10-slim

ENV APP_GROUP=app \
    APP_USER=app


RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \
    && apt-get install -qq ca-certificates gettext git gcc gnupg2 libpq-dev ffmpeg libsm6 libxext6\
    && pip install pipenv \
    && groupadd ${APP_GROUP} \
    && useradd -m -g ${APP_GROUP} ${APP_USER} \
    && echo -n "America/Toronto" > /etc/timezone

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pipenv install --ignore-pipfile --system --deploy

EXPOSE 5000

CMD gunicorn wsgi:app -w 2 -b :5000

