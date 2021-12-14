FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
# The enviroment variable ensures python output to the terminal without buffering
ENV PYTHONUNBUFFERED 1
RUN mkdir /mifosmediators

# packages required for setting up WSGI
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libc-dev python3-dev default-libmysqlclient-dev
RUN apt-get -y install git

WORKDIR /mifosmediators
ADD ./requirements.txt /mifosmediators/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /mifosmediators/
