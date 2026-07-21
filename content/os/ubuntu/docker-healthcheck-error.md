---
title: "Docker Healthcheck Configuration Error"
description: "Docker container health check fails or not defined"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Healthcheck Configuration Error

Docker container health check fails or not defined

## Common Causes

- HEALTHCHECK instruction missing in Dockerfile
- Health check interval too short causing flapping
- Health check command not found in container
- Health check timeout too low

## How to Fix

1. Check health: `docker inspect --format='{{.State.Health.Status}}' <container>`
2. Add healthcheck: `HEALTHCHECK --interval=30s --timeout=10s CMD curl -f http://localhost/ || exit 1`
3. View health logs: `docker inspect <container> | jq '.[0].State.Health'`
4. Disable healthcheck: `--no-healthcheck` flag

## Examples

```bash
# Check container health
docker inspect --format='{{json .State.Health}}' mycontainer | jq

# Run with healthcheck
docker run --health-cmd='curl -f http://localhost/' --health-interval=30s myimage

# View health check logs
docker inspect mycontainer | jq '.[0].State.Health.Log'
```
