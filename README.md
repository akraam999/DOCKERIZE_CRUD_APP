My Project

My Django Rest Framework Application is a simple REST API that allows to manage students. It's built using Django, Django Rest Framework, and Docker.

Requirements :

Docker

Git


Installation

    1- Clone the repository: git clone https://github.com/akraam999/DOCKERIZE_CRUD_APP.git
    2- Install Docker on your machine.
    3- Open the terminal and navigate to the root directory of the project.
    4- execute this command line : dokcer compose up --build
    5- check containers by execute this line command : docker ps
    5 - access to container of postgre : 
        5-1 Run docker exec -it <container_name> bash
        5-2 psql -h localhost -U <postgres_username>
        5-3 CREATE DATABASE <database_name>;
        5-4 ALTER USER <postgres_username> WITH PASSWORD 'new_password';
        5-5 GRANT ALL PRIVILEGES ON DATABASE <database_name> to <postgres_username>;
        5-6 Change username and password for database in setting.py
    6- access to container of django project
    7- run this command python manage.py runserver
    8- open your web browser and navigate to http://localhost:8000. From there, you can use the API to create, view, and delete students.
    
