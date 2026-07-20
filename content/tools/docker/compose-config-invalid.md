---
title: "[Solution] Docker Compose config file invalid"
description: "Fix 'config file invalid' error in Docker Compose. Resolve YAML syntax errors in docker-compose files."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose config file invalid

ERROR: yaml: line <n>: did not find expected key

This error occurs when the docker-compose.yml file has YAML syntax errors.

## How to Fix

### Check Docker Status

```bash
docker info
docker system df
```

### View Logs

```bash
docker logs <container>
docker events --since 5m
```

### Restart Docker

```bash
sudo systemctl restart docker
```

## Related Errors

- [Container Not Running]({{< relref "/tools/docker/container-is-not-running" >}}) — container stopped
- [Image Not Found]({{< relref "/tools/docker/docker-image-not-found" >}}) — image missing
