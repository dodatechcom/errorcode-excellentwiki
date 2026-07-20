---
title: "[Solution] Docker Compose include error"
description: "Fix 'include error' in Docker Compose. Resolve issues when including external compose files."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose include error

Error: include: file <path> not found

This error occurs when a compose file's `include` directive references a file that does not exist.

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
