---
title: "[Solution] Docker Compose Build Cache Error — How to Fix"
description: "Fix Docker Compose build cache corruption errors. Resolve cache misses, stale layers, rebuild failures, and BuildKit cache issues fast."
comments: true
---

## What This Error Means

The build cache error occurs when Docker's build cache becomes corrupted, inconsistent, or produces unexpected results. This leads to build failures, stale images, or incorrect layer reuse that causes applications to run with outdated code or dependencies.

A typical error:

```
ERROR: failed to solve: error from node: build cache
is corrupted: unlink /var/lib/docker/cache/...
```

Or:

```
failed to solve with frontend dockerfile.v0:
failed to read dockerfile: error getting dockerfile:
could not parse build cache from ...
```

Or:

```
warning: Cache import import ... failed: ...
```

Or:

```
ERROR: no cache directory in session
```

## Why It Happens

Build cache errors occur when:

- **Cache directory corruption**: The Docker build cache directory on the host filesystem becomes corrupted due to disk errors or interrupted builds.
- **Interrupted build process**: A build was killed or crashed mid-layer, leaving incomplete cache entries.
- **Disk space exhaustion**: The Docker daemon runs out of disk space, causing cache writes to fail partially.
- **Stale cache after base image update**: A base image was updated but the cached build layers still reference the old digest.
- **BuildKit cache conflicts**: Multiple concurrent builds compete for the same cache entries, causing race conditions.
- **Cache mount corruption**: Named cache mounts used with `--mount=type=cache` become inconsistent after filesystem errors.

## Common Error Messages

### Corrupted cache directory

```
ERROR: failed to solve: error from node: build cache
is corrupted: unlinkat /var/lib/docker/overlay2/...:
directory not empty
```

The overlay filesystem cache has leftover files from a failed operation.

### Cache import failure

```
failed to solve with frontend dockerfile.v0:
failed to create LLB definition:
error resolving cache import: content digest not found
```

A cached layer references a blob that no longer exists in the local registry.

### Cache mount failure

```
ERROR: failed to solve: error getting build cache:
could not load cache mount:
mount source path not found
```

A named cache mount directory was deleted or is inaccessible.

### Concurrent build cache conflict

```
ERROR: failed to solve: error writing build cache:
error persisting cache: concurrent write on same key
```

Two simultaneous builds try to write to the same cache entry.

## How to Fix It

### Solution 1: Prune the build cache

Remove all or selective build cache entries to eliminate corruption.

```bash
# Remove all build cache
docker builder prune -a

# Remove build cache older than 24 hours
docker builder prune -a --filter "until=24h"

# Remove all unused images, containers, and cache
docker system prune -a --volumes

# Check cache size before pruning
docker system df
```

### Solution 2: Disable BuildKit cache temporarily

Build without caching to bypass corrupted cache entries.

```bash
# Build without cache
docker compose build --no-cache

# Or disable BuildKit entirely
DOCKER_BUILDKIT=0 docker compose build

# Check if BuildKit is causing issues
docker buildx ls
```

### Solution 3: Reset the BuildKit builder

Remove and recreate the BuildKit build instance.

```bash
# Stop the default BuildKit builder
docker buildx stop

# Remove the builder
docker buildx rm mybuilder 2>/dev/null

# Create a fresh builder
docker buildx create --name mybuilder --use

# List builders to confirm
docker buildx ls

# Rebuild
docker compose build
```

### Solution 4: Clear Docker overlay2 cache manually

For severe corruption, manually clean the overlay2 cache directory.

```bash
# Stop Docker daemon
sudo systemctl stop docker

# Remove overlay2 cache
sudo rm -rf /var/lib/docker/overlay2/*

# Remove buildkit cache
sudo rm -rf /var/lib/docker/buildkit

# Restart Docker
sudo systemctl start docker

# Rebuild images
docker compose build --no-cache
```

### Solution 5: Fix named cache mount issues

Named cache mounts used in Dockerfiles can become stale.

```dockerfile
# Dockerfile with cache mount
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

```bash
# Clear specific cache mounts
docker builder prune -f --filter "type=exec.cachemount"

# Or use a unique cache ID per build
docker compose build --no-cache --build-arg CACHE_BUST=$(date +%s)
```

### Solution 6: Add cache-busting to force layer rebuild

Force specific layers to rebuild when cache is stale.

```dockerfile
# Add a build argument that changes to invalidate cache
ARG CACHE_BUST=1
RUN pip install -r requirements.txt

# Or use ADD with a changing file
ADD --chmod=755 https://example.com/dep-v${VERSION}.tar.gz /tmp/
RUN cd /tmp && tar xzf dep-v${VERSION}.tar.gz
```

```bash
# Pass the cache-bust argument
docker compose build --build-arg CACHE_BUST=$(date +%s)
```

## Common Scenarios

### Base image updated but build uses stale cache

A base image like `python:3.11` was updated with security patches, but Docker uses the cached layer and does not pull the new version.

```dockerfile
# Cache invalidation may not trigger if only the digest changes
FROM python:3.11
```

Force a fresh pull:

```bash
# Pull the latest image explicitly
docker pull python:3.11

# Build with no cache
docker compose build --no-cache

# Or pin to a specific digest
FROM python:3.11@sha256:abc123...
```

### Concurrent CI builds corrupt cache

Multiple CI runners share the same Docker host and their builds interfere with each other's cache.

```yaml
# .github/workflows/build.yml
jobs:
  build:
    runs-on: self-hosted
    steps:
      - name: Clean build cache
        run: docker builder prune -f --filter "until=1h"

      - name: Build
        run: docker compose build
```

Use BuildKit inline cache for CI:

```yaml
services:
  api:
    build:
      context: .
      args:
        BUILDKIT_INLINE_CACHE: 1
```

### Docker Desktop cache corruption on macOS

Docker Desktop on macOS stores cache in a VM disk image that can become corrupted after force-quit or disk pressure.

```bash
# Reset Docker Desktop to factory defaults
# Docker Desktop > Settings > Resources > Reset to factory defaults

# Or prune everything
docker system prune -a --volumes

# If persistent, reset the VM
rm -rf ~/Library/Containers/com.docker.docker/Data/vms/*
```

## Prevent It

- **Use `--no-cache` periodically in CI**: Even when builds normally rely on cache, schedule periodic full rebuilds with `--no-cache` to prevent stale layers from accumulating and causing inconsistent builds.
- **Implement cache-busting strategies for dependencies**: When requirements files change, use `ARG CACHE_BUST` or change the requirements file name to force a clean layer rebuild. This ensures dependency updates are never masked by stale cache.
- **Monitor Docker disk usage**: Add `docker system df` to monitoring scripts and set alerts when cache usage grows beyond expected thresholds. Uncontrolled cache growth both wastes disk space and increases the likelihood of corruption.
