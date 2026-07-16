---
title: "[Solution] Docker COPY failed: file not found in context"
description: "Fix Docker COPY failed file not found errors. Resolve missing files, incorrect paths, and build context issues."
tools: ["docker"]
error-types: ["build-error"]
severities: ["error"]
tags: ["copy", "dockerfile", "build-context", "file-not-found", "build"]
weight: 5
---

# Docker COPY failed: file not found in context

The COPY or ADD instruction cannot find the specified file in the build context. Docker only has access to files within the directory passed to `docker build`.

## Common Causes

- File path is incorrect or case-sensitive mismatch
- File is excluded by .dockerignore
- File does not exist in the build context directory
- Multi-stage build referencing a stage name that does not exist

## How to Fix

### Verify File Exists in Build Context

```bash
ls -la <path-to-file>
# Ensure the file is in the directory you're building from
```

### Check .dockerignore

```bash
cat .dockerignore
# Remove entries that exclude the file you need
```

### Use Absolute Path in COPY

```dockerfile
# Instead of relative paths
COPY ./src/config.json /app/config.json
```

### Check for Case Sensitivity

```bash
# Linux is case-sensitive
ls -la Dockerfile  # exists
COPY DockerFile /app/  # wrong case - will fail
```

### Build from Correct Directory

```bash
# Build from the project root
docker build -f docker/Dockerfile .

# Not from docker/ directory
```

## Examples

```bash
# Example 1: Wrong directory
docker build -f Dockerfile ./src/
# error: COPY failed: file not found: src/main.js
# Fix: build from project root: docker build .

# Example 2: .dockerignore exclusion
cat .dockerignore
# *.env
# config/
COPY config/app.json /app/
# error: file not found: config/app.json
# Fix: remove config/ from .dockerignore

# Example 3: Case mismatch on Linux
COPY Myfile.txt /app/
# error: file not found
ls myfile.txt  # lowercase
# Fix: use exact filename case
```

## Related Errors

- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit" >}}) — BuildKit failed to solve
- [Docker Multi-Stage Error]({{< relref "/tools/docker/docker-multi-stage" >}}) — stage not found
- [Build Failed]({{< relref "/tools/docker/build-failed2" >}}) — general Docker build failures
