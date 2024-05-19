start:
	docker compose up -d && python3 api.py

flask:
	flask --app api --debug run 

	