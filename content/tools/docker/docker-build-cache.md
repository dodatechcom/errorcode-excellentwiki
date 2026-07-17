---
title: "[Solution] Docker Build Cache Error — build cache error"
description: "Fix Docker build cache errors. Resolve cache-related issues during Docker image builds."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["build", "cache", "layer", "docker", "buildkit"]
weight: 5
---

A Docker build cache error occurs when the build cache is corrupted or incompatible. This can cause builds to fail or produce unexpected results.

## Common Causes

- Corrupted build cache from an interrupted build
- Cache mount points not available during build
- BuildKit cache backend issues
- Insufficient disk space for cache storage
- Cross-platform build cache incompatibility

## How to Fix

### Prune Build Cache

```bash
docker builder prune
```

### Clear All Build Cache

```bash
docker builder prune -a
```

### Disable Build Cache

```bash
docker build --no-cache -t my-image .
```

### Check BuildKit Status

```bash
DOCKER_BUILDKIT=1 docker build -t my-image .
```

### Set Cache Export/Import

```bash
docker build --cache-from type=registry,ref=my-image:latest -t my-image .
```

## Examples

```bash
# Example 1: Clear and rebuild
docker builder prune -a
docker build -t my-image .

# Example 2: Build without cache
docker build --no-cache -t my-image .

# Example 3: Use BuildKit for better caching
DOCKER_BUILDKIT=1 docker build --progress=plain -t my-image .
```

## Related Errors

- [Docker Image Not Found]({{< relref "/tools/docker/docker-image-not-found" >}}) — image not found in registry
- [Docker Pull Timeout]({{< relref "/tools/docker/docker-pull-timeout" >}}) — Docker pull timeout
