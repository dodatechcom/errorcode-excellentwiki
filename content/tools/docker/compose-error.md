---
title: "[Solution] Docker Compose Error — docker compose error"
description: "Fix Docker Compose errors. Resolve configuration, service, and build issues with docker-compose."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose Error — docker compose configuration error

Docker Compose errors occur when the `docker-compose.yml` file has syntax errors, invalid configurations, or references non-existent resources.

## Common Causes

- YAML syntax errors in docker-compose.yml
- Invalid image name or tag
- Referencing non-existent networks or volumes
- Docker Compose version mismatch

## How to Fix

### Validate Compose File

```bash
docker compose config
```

### Check YAML Syntax

```bash
cat docker-compose.yml | grep -n ":"
```

### Fix Indentation

```yaml
# Correct
services:
  web:
    image: nginx

# Wrong
services:
web:
  image: nginx
```

### Update Docker Compose

```bash
docker compose version
```

### Rebuild and Restart

```bash
docker compose down
docker compose up --build
```

### Check for Deprecated Options

```bash
docker compose up --remove-orphans
```

## Examples

```bash
# Example 1: YAML syntax error
docker compose up
# error: services.web Additional property invalid is not allowed
# Fix: remove invalid property from docker-compose.yml

# Example 2: Indentation issue
docker compose up
# ERROR: Version in "./docker-compose.yml" is invalid
# Fix: fix YAML indentation

# Example 3: Image not found
docker compose up
# Error: No such image: my-app:latest
# Fix: docker compose build
```

## Related Errors

- [Build Failed]({{< relref "/tools/docker/build-failed2" >}}) — COPY failed during build
- [Network Error]({{< relref "/tools/docker/network-error2" >}}) — network not found
