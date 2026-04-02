.PHONY: up down restart logs shell rebuild dist

up:
	docker compose up --build -d

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

shell:
	docker compose exec jupyterhub bash

rebuild:
	docker compose up --build -d --force-recreate

dist:
	@scripts/build-dist.sh

.PHONY: clean
clean:
	docker compose down -v
