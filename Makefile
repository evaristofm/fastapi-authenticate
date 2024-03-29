
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py devopslib

test:
	python -m pytest -vv --cov=devopslib test_*.py

format:
	black *.py devopslib/*.py

deploy:
	#deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 066851355839.dkr.ecr.us-east-1.amazonaws.com
	docker build -t devops-may-2022 .
	docker tag devops-may-2022:latest 066851355839.dkr.ecr.us-east-1.amazonaws.com/devops-may-2022:latest
	docker push 066851355839.dkr.ecr.us-east-1.amazonaws.com/devops-may-2022:latest

all: install lint test format deploy