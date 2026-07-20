---
title: "[Solution] Docker push unauthorized"
description: "Fix 'unauthorized: authentication required' error. Resolve Docker push failures when not logged in or token is invalid."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker push unauthorized

unauthorized: authentication required

This error occurs when you try to push to a private registry without authentication or with invalid credentials.

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
