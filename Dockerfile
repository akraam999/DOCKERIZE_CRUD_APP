
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /ui
COPY requirements.txt /ui/
RUN pip install -r requirements.txt
COPY . /ui/ 
CMD ["python","manage.py","runserver","0.0.0.0:8082"]
EXPOSE 8080
# syntax=docker/dockerfile:1

