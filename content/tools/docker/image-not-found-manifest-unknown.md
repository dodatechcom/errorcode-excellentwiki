---
title: "[Solution] Docker Image Not Found — manifest unknown / image not found"
description: "Fix Docker image not found and manifest unknown errors. Pull correct image tags and fix registry access."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

# manifest unknown / image not found

This error occurs when Docker cannot find the requested image or tag in the registry. The image may not exist, may have been removed, or the tag is incorrect.

## Common Causes

- Typo in image name or tag
- Image was removed from registry
- Wrong registry configured
- Image exists in different namespace/repository
- Using a tag that no longer exists

## How to Fix

### Verify Image Exists

```bash
docker pull <image>:<tag>
```

### Search for Image

```bash
docker search <image-name>
```

### Check Available Tags

```bash
# For Docker Hub
curl -s "https://hub.docker.com/v2/repositories/<namespace>/<name>/tags/?page_size=10" | python3 -m json.tool
```

### Check Registry Configuration

```bash
cat /etc/docker/daemon.json
```

### Use Specific Digest Instead of Tag

```bash
docker pull <image>@sha256:<digest>
```

## Examples

```bash
# Example 1: Wrong tag
docker pull nginx:nonexistent
# manifest unknown
# Fix: docker pull nginx:latest

# Example 2: Wrong registry
docker pull myregistry.com/nginx:latest
# Fix: ensure registry URL is correct

# Example 3: Check available tags
curl -s "https://hub.docker.com/v2/repositories/library/nginx/tags/?page_size=5" | python3 -m json.tool
```

## Related Errors

- [Docker image not found]({{< relref "/tools/docker/docker-image-not-found" >}}) — related error
- [Docker pull failed]({{< relref "/tools/docker/pull-failed" >}}) — related error
