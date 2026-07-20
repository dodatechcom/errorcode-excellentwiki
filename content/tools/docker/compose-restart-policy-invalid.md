---
title: "[Solution] Docker Compose restart policy invalid"
description: "Fix 'restart policy invalid' error in Docker Compose. Resolve compose restart configuration issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose restart policy invalid

Error: invalid restart policy '<policy>'

This error occurs when the `restart` policy in a compose file has an invalid value. Valid values: no, always, on-failure, unless-stopped.

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
