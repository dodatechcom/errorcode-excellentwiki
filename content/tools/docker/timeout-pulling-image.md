---
title: "[Solution] Docker timeout pulling image"
description: "Fix 'timeout pulling image' error. Resolve Docker pull failures when image download times out."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker timeout pulling image

Error response from daemon: Get <url>: net/http: TLS handshake timeout

This error occurs when a Docker image pull takes longer than the configured timeout.

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
