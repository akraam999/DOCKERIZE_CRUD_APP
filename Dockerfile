
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /akr
COPY requirements.txt /akr/
RUN pip install -r requirements.txt
COPY . /akr/
CMD ["python","manage.py","runserver","0.0.0.0:8080"]
EXPOSE 8080
# syntax=docker/dockerfile:1

