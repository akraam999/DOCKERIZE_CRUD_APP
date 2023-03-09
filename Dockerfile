
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /sdd
COPY requirements.txt /sdd/
RUN pip install -r requirements.txt
COPY . /sdd/
CMD ["python","manage.py","runserver","0.0.0.0:8080"]
EXPOSE 8080
# syntax=docker/dockerfile:1

