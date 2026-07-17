---
title: "[Solution] Docker Image Not Found — image not found in registry"
description: "Fix Docker image not found errors. Resolve image pull failures from registries."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A Docker image not found error occurs when Docker cannot find the specified image in the registry. The image name, tag, or registry address may be incorrect.

## Common Causes

- Typo in the image name or tag
- The image was removed from the registry
- Using wrong registry (e.g., Docker Hub vs private registry)
- Image exists but under a different organization/user
- Tag does not exist (using `latest` when it was never pushed)

## How to Fix

### Verify Image Exists

```bash
docker search <image-name>
```

### Check Available Tags

```bash
curl -s "https://hub.docker.com/v2/repositories/library/<image>/tags/" | jq
```

### Pull with Full Registry Path

```bash
docker pull docker.io/library/nginx:latest
docker pull ghcr.io/owner/image:tag
```

### Login to Private Registry

```bash
docker login <registry-url>
docker pull <registry-url>/<image>:<tag>
```

### Check Local Images

```bash
docker images | grep <image>
```

## Examples

```bash
# Example 1: Image tag not found
docker pull my-app:1.0
# Error: manifest for my-app:1.0 not found
# Fix: check available tags on registry

# Example 2: Wrong registry
docker pull my-company/my-app:latest
# Fix: docker pull registry.example.com/my-company/my-app:latest

# Example 3: Login to private registry
docker login registry.example.com
docker pull registry.example.com/my-app:latest
```

## Related Errors

- [Docker Pull Timeout]({{< relref "/tools/docker/docker-pull-timeout" >}}) — Docker pull timeout
- [Docker Build Cache]({{< relref "/tools/docker/docker-build-cache" >}}) — build cache error
