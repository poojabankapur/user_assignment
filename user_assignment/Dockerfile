# Dockerfile

# Pull base image
FROM python:3.7.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py runserver 0.0.0.0:8000