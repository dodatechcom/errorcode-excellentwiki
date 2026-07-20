---
title: "[Solution] Docker build ENV instruction error"
description: "Fix 'ENV instruction error' in Docker build. Resolve Dockerfile environment variable syntax issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build ENV instruction error

Error: failed to parse Dockerfile: ENV must have two arguments

This error occurs when the ENV instruction in the Dockerfile has an incorrect format. ENV requires either KEY=VALUE pairs or KEY VALUE format.

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
