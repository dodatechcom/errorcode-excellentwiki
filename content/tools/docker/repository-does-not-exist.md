---
title: "[Solution] Docker repository does not exist"
description: "Fix 'repository does not exist' error. Resolve Docker pull failures when the repository has been deleted or moved."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker repository does not exist

Error response from daemon: repository <name> not found

This error occurs when the Docker image repository does not exist on the registry. The repository may have been deleted or the URL is incorrect.

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
