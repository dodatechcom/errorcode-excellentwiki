---
title: "[Solution] Docker read from stdin error"
description: "Fix 'read from stdin' error. Resolve Docker build issues when reading Dockerfiles from standard input."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker read from stdin error

Error: docker: failed to read from stdin

This error occurs when Docker cannot read the build context from stdin.

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
