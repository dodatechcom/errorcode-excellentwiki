---
title: "[Solution] Docker Build cache error / corruption"
description: "Fix Docker build cache errors and corruption. Resolve cache mount failures, stale layers, and rebuild issues."
tools: ["docker"]
error-types: ["build-error"]
severities: ["error"]
tags: ["build-cache", "cache", "layer", "corruption", "rebuild"]
weight: 5
---

# Docker Build cache error / corruption

Build cache errors occur when Docker's layer cache becomes corrupted or stale. This causes builds to fail with cache mount errors or produce incorrect layer reuse.

## Common Causes

- Interrupted build left cache in inconsistent state
- Docker engine upgrade invalidated old cache format
- Disk corruption in Docker's storage directory
- Concurrent builds competing for the same cache layers

## How to Fix

### Clear Build Cache

```bash
# Remove all build cache
docker builder prune

# Remove all unused data (cache, images, networks)
docker system prune -a --volumes

# Remove cache older than 24 hours
docker builder prune --filter "until=24h"
```

### Rebuild Without Cache

```bash
docker build --no-cache -t my-app .
```

### Prune BuildKit Cache

```bash
# If using BuildKit
docker buildx prune -a
docker buildx prune --all --type=regular
```

### Check Docker Storage Driver

```bash
docker info | grep "Storage Driver"
# Should show overlay2 or similar stable driver
```

### Reset Docker Storage

```bash
# Nuclear option - removes everything
sudo systemctl stop docker
sudo rm -rf /var/lib/docker
sudo systemctl start docker
```

## Examples

```bash
# Example 1: Cache mount failure
docker build .
# ERROR: failed to solve: failed to mount cache: ...
# Fix: docker builder prune && docker build .

# Example 2: Stale layers after upgrade
docker build .
# error: cache import not found
# Fix: docker builder prune -a && docker build --no-cache .

# Example 3: Concurrent build conflict
docker build . &
docker build . &
# Error: error creating build cache
# Fix: run builds sequentially or use buildx builders
```

## Related Errors

- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit" >}}) — BuildKit failed to solve
- [No Space Left]({{< relref "/tools/docker/no-space" >}}) — disk space exhausted
- [Build Failed]({{< relref "/tools/docker/build-failed2" >}}) — general build failures
