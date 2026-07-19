---
title: "[Solution] Docker COPY Failed — COPY failed / ADD failed"
description: "Fix Docker COPY failed error during build. Resolve file permission and path issues in Dockerfile."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

# COPY failed: file not found in context or excluded by .dockerignore

This error occurs during `docker build` when the COPY or ADD instruction cannot find the source file or directory. It may also fail due to permissions or .dockerignore exclusions.

## Common Causes

- File or directory does not exist in build context
- File is excluded by .dockerignore
- Incorrect relative path in Dockerfile
- File permissions prevent reading
- Symlinks pointing outside build context

## How to Fix

### Verify File Exists in Build Context

```bash
ls -la <file-path>
```

### Check .dockerignore

```bash
cat .dockerignore
```

### Use Absolute Path in Container

```dockerfile
COPY ./src/ /app/src/
ADD config.json /app/config/
```

### Build with Verbose Output

```bash
docker build --progress=plain .
```

### Verify Build Context

```bash
docker build -f Dockerfile .
# Check the sending build context size
```

### Fix Permissions

```bash
chmod 644 <file>
```

## Examples

```bash
# Example 1: File not found
COPY config.yml /app/
# Error: file not found in context
# Fix: ensure config.yml exists in build context

# Example 2: .dockerignore excluded file
# .dockerignore contains: *.log
COPY app.log /app/logs/
# Fix: remove from .dockerignore or use different file

# Example 3: Directory not found
COPY src/ /app/
# Fix: ls src/ to verify directory exists
```

## Related Errors

- [Docker copy error]({{< relref "/tools/docker/docker-copy-error" >}}) — related error
- [Build failed]({{< relref "/tools/docker/build-failed2" >}}) — related error
