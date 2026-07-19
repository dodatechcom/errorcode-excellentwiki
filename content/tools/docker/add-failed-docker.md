---
title: "[Solution] Docker ADD Failed — ADD failed in Dockerfile"
description: "Fix Docker ADD instruction failed error. Resolve URL downloads and file copy issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

# ADD failed: failed to fetch

This error occurs when the ADD instruction in a Dockerfile fails. ADD can copy local files and download URLs, and either operation can fail.

## Common Causes

- Local file does not exist in build context
- URL in ADD is unreachable
- Network timeout during URL download
- Invalid URL format
- File permissions prevent reading

## How to Fix

### For Local Files

```dockerfile
# Verify file exists in build context
COPY ./file.txt /app/
# Prefer COPY over ADD for simple file copies
```

### For URL Downloads

```dockerfile
# Ensure URL is accessible
ADD https://example.com/file.tar.gz /app/
# Check network connectivity during build
```

### Use COPY Instead of ADD

```dockerfile
# ADD extracts archives automatically, COPY does not
# Use COPY unless you need ADD's features
COPY file.tar.gz /app/
RUN tar -xzf /app/file.tar.gz -C /app/
```

### Build with No Cache

```bash
docker build --no-cache .
```

## Examples

```bash
# Example 1: File not in context
ADD config.yml /app/
# Fix: ensure config.yml is in build directory

# Example 2: URL unreachable
ADD https://example.com/file.tar.gz /app/
# Fix: check network and URL validity

# Example 3: Use COPY instead
# Bad:
ADD package.json /app/
# Better:
COPY package.json /app/
```

## Related Errors

- [COPY failed]({{< relref "/tools/docker/copy-failed" >}}) — related error
- [Build failed]({{< relref "/tools/docker/build-failed2" >}}) — related error
