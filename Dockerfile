# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set environment
WORKDIR /code
COPY Pipfile /code/
COPY Pipfile.lock /code/

# run updates
RUN apt-get update
RUN apt-get upgrade -y

# Upgrade pip
RUN set -ex && pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip --upgrade

# Install pipenv
RUN set -ex && pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pipenv --upgrade

# Install dependencies
RUN set -ex && pipenv lock -r > req.txt && pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r req.txt

# copy files
COPY ./benford/ /code/


