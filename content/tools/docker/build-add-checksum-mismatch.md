---
title: "[Solution] Docker build ADD checksum mismatch"
description: "Fix 'ADD checksum mismatch' error. Resolve Docker build failures when downloaded file checksums do not match expected values."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker build ADD checksum mismatch

ERROR: failed to solve: failed to fetch: checksum mismatch

This error occurs when the ADD instruction downloads a file but the checksum does not match the expected value specified with `--checksum`.

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
