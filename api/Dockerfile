FROM python:3.10.9-bullseye

WORKDIR /service

RUN apt update && apt -y upgrade && apt -y install lsb-release expect \
build-essential python-dev

RUN curl -O https://repo.mysql.com//mysql-apt-config_0.8.24-1_all.deb

COPY mysql_dpkg.exp .

RUN expect mysql_dpkg.exp

RUN rm mysql-apt-config_0.8.24-1_all.deb mysql_dpkg.exp

RUN apt update && apt -y install mysql-client libmysqlclient-dev

COPY ./requirements.txt /service/requirements.txt

ENV PYTHONPATH /service:$PYTHONPATH

RUN pip install --no-cache-dir --upgrade -r /service/requirements.txt

