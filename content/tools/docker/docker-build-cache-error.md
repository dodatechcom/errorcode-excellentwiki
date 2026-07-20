---
title: "[Solution] Docker Build Cache Error — failed to load cache"
description: "Fix Docker BuildKit 'failed to solve: failed to load cache' error. Resolve build cache corruption and export issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "buildkit", "build-cache", "dockerfile"]
severity: "error"
weight: 7
---

# ERROR: failed to solve: failed to load cache

## Error Message

```
ERROR: failed to solve: failed to load cache key for stage builder: failed to load cache: invalid cache record
```

This error appears when BuildKit cannot load a cached layer during a Docker image build. The cache has become corrupted or is incompatible with the current build context.

## Common Causes

- The build cache was corrupted by an interrupted build process
- Cache records reference layer IDs that no longer exist on disk
- Disk space ran out during a previous build, leaving partial cache entries
- Switching between different BuildKit cache backends caused metadata mismatch
- Cross-platform builds created cache entries that the current platform cannot read

## Solutions

### Solution 1: Prune the Build Cache

Clearing the entire build cache forces BuildKit to rebuild all layers from scratch. This is the fastest way to resolve cache corruption.

```bash
docker builder prune -af
docker build -t myimage .
```

### Solution 2: Use No-Cache Flag for a Clean Build

Bypass all cache layers for a single build without permanently deleting the cache. Useful for debugging whether the cache is causing the failure.

```bash
docker build --no-cache -t myimage .
```

### Solution 3: Reset BuildKit Backend

If you are using a custom BuildKit cache export or import driver, switching back to the default local driver removes the problematic backend configuration.

```bash
docker buildx rm mybuilder
docker buildx create --name mybuilder --driver docker-container --use
docker buildx inspect --bootstrap
docker build -t myimage .
```

### Solution 4: Free Disk Space

BuildKit needs free disk space to manage cache metadata. Remove unused images, containers, and volumes to reclaim space before rebuilding.

```bash
docker system prune -af
docker builder prune -af
df -h
docker build -t myimage .
```

## Prevention Tips

- Use `docker buildx prune` regularly to keep cache size manageable
- Ensure adequate disk space before large multi-stage builds
- Avoid force-killing Docker daemon during active builds
- Pin BuildKit versions in CI pipelines for consistent cache behavior

## Related Errors

- [Docker Pull Failed]({{< relref "/tools/docker/pull-failed" >}}) — image pull failure
- [Layer Cache Error]({{< relref "/tools/docker/layer-cache" >}}) — cache reuse issues
