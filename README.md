# fast-api-docker

## Development

```shell
uv run fastapi dev
```

## Dockerfile

Build
```shell
docker build -t fast-api-docker .
```

Run
```shell
docker run -d -p 8000:80 fast-api-docker
```
