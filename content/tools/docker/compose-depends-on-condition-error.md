---
title: "[Solution] Docker Compose depends_on condition error"
description: "Fix 'depends_on condition error' in Docker Compose. Resolve compose service dependency condition issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose depends_on condition error

Error: depends_on condition <condition> is not valid

This error occurs when the `condition` field under `depends_on` has an invalid value.

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
