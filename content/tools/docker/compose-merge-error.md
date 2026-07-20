---
title: "[Solution] Docker Compose merge error"
description: "Fix 'merge error' in Docker Compose. Resolve compose YAML merge tag issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Compose merge error

Error: cannot merge <key> and <key>

This error occurs when a compose file has conflicting keys that cannot be merged.

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
