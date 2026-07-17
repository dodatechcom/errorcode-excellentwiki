---
title: "[Solution] Docker Cache Not Found — cache not found"
description: "Fix Docker cache not found error during build. Optimize layer caching and build performance."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Cache Not Found — cache not found in scope

This error occurs when Docker cannot find a cached layer for a build step. It forces a rebuild of all subsequent layers, slowing down the build process.

## Common Causes

- Previous build layer changed, invalidating cache
- Dockerfile instructions reordered
- Build arguments changed
- `.dockerignore` excludes cached files

## How to Fix

### Order Dockerfile Instructions by Change Frequency

```dockerfile
# Install dependencies first (rarely changes)
COPY package*.json ./
RUN npm install

# Then copy source code (changes often)
COPY . .
```

### Use BuildKit Cache Mounts

```dockerfile
# syntax=docker/dockerfile:1
RUN --mount=type=cache,target=/root/.cache/npm npm install
```

### Use Docker Build Cache from Registry

```bash
docker build --cache-from registry/image:tag -t image:tag .
```

### Disable Cache (for debugging)

```bash
docker build --no-cache -t <image> .
```

### Multi-Stage Build with Cache

```dockerfile
FROM node:18 AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
```

## Examples

```bash
# Example 1: Check if cache is being used
docker build -t myapp .
# Step 3/5 : COPY package*.json ./
# ---> Using cache

# Example 2: Force rebuild without cache
docker build --no-cache -t myapp .

# Example 3: Use BuildKit for better caching
DOCKER_BUILDKIT=1 docker build -t myapp .
```

## Related Errors

- [Build Failed]({{< relref "/tools/docker/build-failed2" >}}) — COPY failed during build
- [No Space Left]({{< relref "/tools/docker/no-space" >}}) — disk space exhausted
