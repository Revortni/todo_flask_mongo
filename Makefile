start:
	python3 api.py

flask:
	flask --app api --debug run 

mongo:
	docker compose up -d