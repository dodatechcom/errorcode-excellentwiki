---
title: "Sail container error"
description: "Laravel Sail throws container errors when the Docker development environment fails to start"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sail", "docker", "container", "development", "compose"]
weight: 5
---

This error occurs when Laravel Sail's Docker containers fail to start, build, or communicate properly. It is typically surfaced as a Docker Compose error during `./vendor/bin/sail up`.

## Common Causes

- Docker is not running on the host machine
- Port already in use by another service
- Docker Compose file syntax errors
- Volume mount permissions denied
- Insufficient disk space for Docker images

## How to Fix

1. Check if Docker is running:

```bash
docker info
docker compose version
```

2. Verify port availability:

```bash
# Check if port 80 is in use
lsof -i :80

# Use a different port
./vendor/bin/sail up -d --port=8080:80
```

3. Rebuild containers after dependency changes:

```bash
./vendor/bin/sail build --no-cache
./vendor/bin/sail up -d
```

4. Fix volume permission issues:

```bash
# Reset Docker volumes
./vendor/bin/sail down -v
./vendor/bin/sail up -d

# Or fix permissions directly
sudo chown -R $USER:$USER storage bootstrap/cache
```

## Examples

```bash
# Error: Bind for 0.0.0.0:3306 failed: port is already allocated
# Fix: Change the MySQL port in docker-compose.yml
services:
    mysql:
        ports:
            - "3307:3306"
```

## Related Errors

- [Vapor error]({{< relref "/frameworks/laravel/vapor-error" >}})
- [Deployer error]({{< relref "/frameworks/laravel/deployer-error" >}})
