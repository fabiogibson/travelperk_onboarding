# Setup

## Install dependencies and create datebase

1. pip install pipenv
2. pipenv install --dev
3. make migrate

+ there is no need for virtual environments.

## Start required containers

1. make up

## Run tests

1. make test

## check coverage

1. make coverage

## Run the project

1. make run

## Stop execution

1. make stop

## Cleaning up

1. make down


# Access


## apis

the following routes will be available when the project is running:

1. http://localhost:8000/api/v1/recipe/
2. http://localhost:8000/api/v1/recipe/{id}/

## django admin console

in order to access the admin you need to create a new user.

1. ./manage.py createsuperuser --username admin
2. fill your email address and password
3. access http://localhost:8000/admin/
