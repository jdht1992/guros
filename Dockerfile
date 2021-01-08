# pull official base image
FROM python:3.8.6

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /guros

# install dependencies
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . /guros/
