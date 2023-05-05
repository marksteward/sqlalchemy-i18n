.PHONY: test-1.3 test-1.4

test-1.3:
	docker compose run main-1.3 pytest -x; docker compose down

test-1.4:
	docker compose run main-1.4 pytest -x; docker compose down


