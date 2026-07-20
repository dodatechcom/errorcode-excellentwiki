---
title: "[Solution] Docker build unknown instruction"
description: "Fix 'unknown instruction' error in Docker build. Resolve Dockerfile parsing errors."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build unknown instruction

Error: Dockerfile parse error: unknown instruction: <cmd>

This error occurs when the Dockerfile contains an instruction that Docker does not recognize.

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
