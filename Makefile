# usage: type in your terminal make run_tests_with_docker
run_tests_with_docker:
	docker build --pull --rm -f "./docker/Dockerfile.dev" -t api:latest "." && \
	docker run -d p 8080:8080/tcp api:latest && \
	pytest -v tavern_tests/test_*.tavern.yaml 

run_pytest_venv:
	# run pytest tavern api tests
	# require .venv/ to exist: python3 -m venv .venv
	. venv/bin/activate && \
	pip install -r requirements/dev.txt && \
	export ENVIRONMENT=DEV && \
	export MONGODB_HOST="localhost:27017" && \
	export MONGODB_DB_AUTH="admin" && \
	nohup python entry_point.py > output.log & &&\
	pytest -v tavern_tests/test_*.tavern.yaml 

run_python_venv:
	# run the api from python .venv 
	# require .venv/ to exist: python3 -m venv .venv
	. venv/bin/activate && \
	pip install -r requirements/dev.txt && \
	export ENVIRONMENT=DEV && \
	export MONGODB_HOST="localhost:27017" && \
	export MONGODB_DB_AUTH="admin" && \
	python entry_point.py

run_docker_dev:
	# build and run from docker/Dockerfile.dev
	docker build --pull --rm -f "./docker/Dockerfile.dev" -t api:latest "." && \
	docker run -it -p 8080:8080/tcp api:latest

run_docker:
	# build and run from docker/Dockerfile
	docker build --pull --rm -f "./docker/Dockerfile" -t api:latest "." && \
	docker run -it -p 8080:8080/tcp api:latest
