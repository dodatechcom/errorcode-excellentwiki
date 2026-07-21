---
title: "Docker Image Build Cache Error"
description: "Docker build cache becomes corrupted or unavailable"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Image Build Cache Error

Docker build cache becomes corrupted or unavailable

## Common Causes

- Cache directory /var/lib/docker/buildkit corrupted
- Docker BuildKit service not running
- Insufficient disk space for cache
- Cache mount points conflicting with layers

## How to Fix

1. Clear build cache: `docker builder prune`
2. Check BuildKit status: `docker buildx ls`
3. Free disk space: `docker system prune -a`
4. Rebuild without cache: `docker build --no-cache .`

## Examples

```bash
# Prune build cache
docker builder prune -a

# Check available builders
docker buildx ls

# Build without cache
docker build --no-cache -t myimage .
```
