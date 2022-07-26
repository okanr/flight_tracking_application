# Flight Tracking Application
This project aims to show how to interact with flight data.

It's an example django application for crud operations. You can create, read, update, delete records via using api endpoints.

## Docker Installation

This repository includes a full-featured docker-compose.yml to start all the necessary services including a Nginx server via Docker.

## Up and Run

At root folder, you can run application with command below.
~~~
docker-compose up
~~~

You can access api via localhost/api

## Testing

For running tests, you can run the command below.

~~~
python manage.py test
~~~