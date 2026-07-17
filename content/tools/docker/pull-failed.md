---
title: "[Solution] Docker Pull Failed — error pulling image"
description: "Fix Docker image pull failed error. Resolve network, authentication, and registry issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Pull Failed — Error pulling image

This error occurs when Docker cannot download an image from the registry. Issues range from network problems to authentication failures.

## Common Causes

- Network connectivity issues
- Registry authentication required
- Image doesn't exist or has been removed
- Rate limiting on Docker Hub

## How to Fix

### Check Network Connection

```bash
ping registry-1.docker.io
```

### Login to Docker Hub

```bash
docker login
```

### Check Image Exists

```bash
docker search <image-name>
```

### Use a Mirror Registry

```bash
docker pull mirror.registry.io/<image>:<tag>
```

### Retry with Backoff

```bash
docker pull <image>:<tag>
# Wait and retry
docker pull <image>:<tag>
```

### Check Docker Hub Rate Limit

```bash
curl -s -I -u username:token https://hub.docker.com/v2/repositories/library/nginx/tags/
```

## Examples

```bash
# Example 1: Network issue
docker pull nginx:latest
# Error: net/http: TLS handshake timeout
# Fix: check network connection and proxy settings

# Example 2: Authentication required
docker pull private.registry.io/my-app:v1
# Error: unauthorized: authentication required
# Fix: docker login private.registry.io

# Example 3: Rate limited
docker pull nginx:latest
# Error: toomanyrequests: You have reached your pull rate limit
# Fix: docker login (authenticated pulls have higher limits)
```

## Related Errors

- [Image Not Found]({{< relref "/tools/docker/image-not-found" >}}) — image doesn't exist locally
- [Permission Denied]({{< relref "/tools/docker/permission-denied3" >}}) — Docker daemon permission issues
