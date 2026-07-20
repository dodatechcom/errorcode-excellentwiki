---
title: "[Solution] Docker login credentials error"
description: "Fix 'credentials error' during Docker login. Resolve Docker registry authentication failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker login credentials error

Error: Cannot perform an interactive login from a non TTY device

This error occurs when trying to run `docker login` in a non-interactive environment without providing credentials via stdin.

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
