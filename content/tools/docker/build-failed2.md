---
title: "[Solution] Docker Build Failed — COPY failed"
description: "Fix Docker COPY failed error during build. Resolve file not found and permission issues in Dockerfile."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Build Failed — COPY failed: file not found

This error occurs when a `COPY` or `ADD` instruction in the Dockerfile references a file or directory that doesn't exist in the build context.

## Common Causes

- File or directory doesn't exist in the build context
- Typo in the source path in Dockerfile
- `.dockerignore` excludes the required file
- Build context doesn't include the necessary files

## How to Fix

### Verify File Exists in Build Context

```bash
ls -la <file-path>
```

### Check .dockerignore

```bash
cat .dockerignore
```

### Build with Correct Context

```bash
docker build -t <image> -f Dockerfile /path/to/context
```

### Use Multi-Stage Build

```dockerfile
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

### Use Absolute Paths

```dockerfile
COPY /absolute/path/to/file /container/path
```

## Examples

```bash
# Example 1: Missing file
docker build -t myapp .
# COPY failed: file not found: src/index.js
# Fix: verify src/index.js exists in build context

# Example 2: .dockerignore issue
cat .dockerignore
# node_modules
# Fix: remove pattern from .dockerignore or copy from different path

# Example 3: Wrong build context
docker build -t myapp ./src
# Fix: docker build -t myapp .
```

## Related Errors

- [No Space Left]({{< relref "/tools/docker/no-space" >}}) — disk space exhausted
- [Layer Cache]({{< relref "/tools/docker/layer-cache" >}}) — cache not found during build
