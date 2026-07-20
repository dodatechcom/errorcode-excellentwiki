---
title: "[Solution] Docker system prune failed"
description: "Fix 'docker system prune failed' error. Resolve Docker cleanup failures when removing unused resources."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker system prune failed

Error: docker system prune failed

This error occurs when Docker cannot complete a prune operation. Resources may be in use or locked.

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
