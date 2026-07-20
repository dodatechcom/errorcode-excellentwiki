---
title: "[Solution] Docker export container failed"
description: "Fix 'docker export failed' error. Resolve container filesystem export failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker export container failed

Error: cannot export container <name>

This error occurs when Docker cannot export a container's filesystem. The container may be in a state that prevents export.

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
