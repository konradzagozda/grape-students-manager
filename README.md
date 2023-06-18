# run project

```sh
docker compose build
docker compose up
```

# run tests

while `docker compose up` is up

```sh
docker compose exec -it web /bin/bash
pytest ./src
pytest ./integration
```
