---
title: "[Solution] Docker build syntax error"
description: "Fix 'syntax error' in Docker build. Resolve Dockerfile syntax parsing errors."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build syntax error

Error: Dockerfile parse error at line <n>: syntax error

This error occurs when the Dockerfile has a syntax error that prevents parsing.

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
