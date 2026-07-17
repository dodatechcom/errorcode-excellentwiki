---
title: "[Solution] Docker Image Not Found — Fix Image Pull Failures"
description: "Fix 'docker image not found' errors on Linux. Resolve 'image not found', 'manifest unknown', and 'name unknown' errors when pulling Docker images."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Docker Image Not Found — Fix Image Pull Failures

A Docker image not found error occurs when `docker pull` or `docker run` cannot find the specified image in the registry. The error reads:

> "Error response from daemon: manifest for <image>:<tag> not found: manifest unknown"

Or:

> "name unknown: repository name not known to registry"

## What This Error Means

Docker images are stored in registries (Docker Hub, GHCR, ECR, etc.) and referenced by name, tag, and digest. When the image does not exist, has been deleted, or the tag is wrong, the registry returns a "not found" error. This is different from a network timeout — the registry was reached but the image was not found.

## Common Causes

- Incorrect image name or tag (typo, case sensitivity)
- Image was deleted or renamed in the registry
- Tag does not exist (using `latest` on a repo that has no `latest` tag)
- Private image requires authentication
- Registry URL is incorrect (e.g., missing `docker.io/` prefix)
- Image moved to a different namespace or organization

## How to Fix

### Verify the Image Exists

```bash
# Search Docker Hub
docker search nginx

# Check specific tags on Docker Hub
curl -s "https://hub.docker.com/v2/repositories/library/nginx/tags/?page_size=10" | jq

# Check a specific registry
curl -s "https://registry.hub.docker.com/v2/repositories/library/nginx/tags/latest" | jq
```

### Check Image Name and Tag

```bash
# List local images
docker images

# Pull with explicit tag
docker pull nginx:1.25-alpine

# Pull by digest (most specific)
docker pull nginx@sha256:abc123...
```

### Authenticate for Private Images

```bash
# Login to the registry
docker login

# Or with specific registry
docker login ghcr.io
docker login registry.gitlab.com

# Check stored credentials
cat ~/.docker/config.json
```

### Use Full Registry URL

```bash
# Docker Hub (implicit)
docker pull nginx

# Docker Hub (explicit)
docker pull docker.io/library/nginx

# GitHub Container Registry
docker pull ghcr.io/owner/image:tag

# Amazon ECR
docker pull 123456789.dkr.ecr.us-east-1.amazonaws.com/myimage:tag
```

### Check for Typos

```bash
# Common mistakes
# Wrong: docker pull NGINX     (case sensitive)
# Right: docker pull nginx

# Wrong: docker pull nginx:lts  (no lts tag)
# Right: docker pull nginx:stable
```

## Related Errors

- [Docker Pull Timeout]({{< relref "/os/linux/linux-docker-pull-timeout" >}}) — Network timeout pulling images
- [Docker Build Cache Error]({{< relref "/os/linux/linux-docker-build-cache" >}}) — Build cache issues
- [k8s ImagePullBackOff]({{< relref "/os/linux/linux-k8s-image-pull" >}}) — Kubernetes image pull failures
