---
title: "[Solution] Docker Compose secret not found"
description: "Fix 'secret not found' error in Docker Compose. Resolve compose secret reference issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose secret not found

Error: secret '<name>' not found

This error occurs when a service references a secret that is not defined in the `secrets` section of the compose file.

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
