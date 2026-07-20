---
title: "[Solution] Docker push denied access"
description: "Fix 'denied: requested access to the resource is denied' error. Resolve Docker push authentication and permission failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker push denied access

denied: requested access to the resource is denied

This error occurs when you try to push an image to a registry that you do not have permission to write to.

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
