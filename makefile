run:
	@python ./onboarding/manage.py runserver

test:
	@cd onboarding && pytest -s

coverage:
	@cd onboarding && pytest --cov=recipes

migrate:
	@python ./onboarding/manage.py makemigrations
	@python ./onboarding/manage.py migrate

clean:
	@find . -name *.pyc -delete
	
up:
	@docker-compose -f ./dockerize/docker-compose.yml up -d

down:
	@docker-compose -f ./dockerize/docker-compose.yml down 

stop: 
	@docker-compose -f ./dockerize/docker-compose.yml stop

build: 
	@docker-compose -f ./dockerize/docker-compose.yml build 

rebuild: 
	@docker-compose -f ./dockerize/docker-compose.yml build --no-cache

bootstrap: migrate
	@python ./onboarding/manage.py load_fixtures
	
