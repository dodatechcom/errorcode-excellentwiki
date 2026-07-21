---
title: "[Solution] Ubuntu Server: docker-compose-error"
description: "Fix Ubuntu docker-compose-error. docker-compose fails to start services."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Docker Compose Error

docker-compose encounters errors starting services.

## Common Causes
- docker-compose.yml syntax error
- Service dependency not met
- Image pull failure
- Port conflict with existing container

## How to Fix
1. Check compose file syntax
```bash
docker compose config
```
2. Check logs
```bash
docker compose logs <service>
```
3. Rebuild and restart
```bash
docker compose down
docker compose up -d --build
```

## Examples
```bash
$ docker compose config
services.web.image: Image named "myapp" could not be resolved
```