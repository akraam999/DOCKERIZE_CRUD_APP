
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /test
COPY requirements.txt /test/
RUN pip install -r requirements.txt
COPY . /test/
CMD ["python","manage.py","runserver","0.0.0.0:8080"]
EXPOSE 8080
# syntax=docker/dockerfile:1

