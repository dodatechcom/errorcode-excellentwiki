---
title: "[Solution] Docker bridge network creation failed"
description: "Fix 'bridge creation failed' error. Resolve Docker default bridge network issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker bridge network creation failed

Error: failed to create bridge network

This error occurs when Docker cannot create the default bridge network. This may be due to iptables or kernel module issues.

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
