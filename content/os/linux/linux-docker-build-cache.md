---
title: "[Solution] Docker Build Cache Error — Fix BuildKit Cache Failures"
description: "Fix Docker build cache errors on Linux. Resolve BuildKit cache mount failures, layer cache corruption, and --cache-from issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["docker", "build", "cache", "buildkit", "layer", "dockerfile"]
weight: 5
---

# Docker Build Cache Error — Fix BuildKit Cache Failures

A Docker build cache error occurs when `docker build` fails due to a corrupted or inaccessible build cache. The error reads:

> "error: failed to solve: error getting build cache: reference not found"

Or:

> "WARNING: buildx: cache export error: No such image"

## What This Error Means

Docker builds images in layers. Each Dockerfile instruction creates a new layer, and Docker caches these layers to speed up subsequent builds. When the cache becomes corrupted, references are lost, or the cache export/import fails, the build fails. BuildKit (the default builder in Docker 23+) uses a more sophisticated cache backend that can encounter these issues.

## Common Causes

- Docker buildx builder cache corrupted
- `--cache-from` referencing a deleted image
- BuildKit cache export to a registry that is unreachable
- Disk space exhaustion in the Docker cache directory
- Corrupted local layer store
- Incompatible cache format between Docker versions

## How to Fix

### Clear the Build Cache

```bash
# Prune all build cache
docker builder prune -a -f

# Prune only unused cache (safer)
docker builder prune -f

# Check cache usage
docker system df
```

### Rebuild Without Cache

```bash
# Build with no cache
docker build --no-cache -t myimage .

# Or for BuildKit
DOCKER_BUILDKIT=1 docker build --no-cache -t myimage .
```

### Fix BuildKit Cache Export

```bash
# Check BuildKit builder
docker buildx ls

# Create a fresh builder
docker buildx create --name mybuilder --use
docker buildx inspect --bootstrap

# Build and push with cache
docker buildx build --cache-to type=registry,ref=myregistry/myimage:cache --push -t myimage .
```

### Clean Docker Data Directory

```bash
# Check Docker data directory usage
docker system df -v

# Remove all unused data
docker system prune -a -f --volumes

# Check disk space
df -h /var/lib/docker
```

### Reset Docker Layer Store

```bash
# Stop Docker
sudo systemctl stop docker

# Remove layer store (destroys all images)
sudo rm -rf /var/lib/docker/image
sudo rm -rf /var/lib/docker/overlay2

# Start Docker (will recreate empty store)
sudo systemctl start docker
```

### Use --mount=type=cache in Dockerfile

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.21
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go build -o /app .
```

## Related Errors

- [Docker Image Not Found]({{< relref "/os/linux/linux-docker-image-not-found" >}}) — Image pull or build failures
- [Docker Pull Timeout]({{< relref "/os/linux/linux-docker-pull-timeout" >}}) — Image pull timeout errors
- [Docker Build Cache Error]({{< relref "/os/linux/linux-docker-build-cache" >}}) — Build cache corruption
