---
title: "[Solution] Docker Image Error — image not found"
description: "Fix Docker 'image not found' error. Pull, rebuild, and resolve missing Docker image issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "images", "pull", "registry"]
severity: "error"
weight: 5
---

# ERROR: image not found

## Error Message

```
Error: No such image: myregistry.com/myapp:latest

Error response from daemon: manifest for myregistry.com/myapp:latest not found: manifest unknown
```

This error occurs when Docker cannot find the specified image in local storage or in the remote registry. The image may not exist, the tag may be wrong, or access may be restricted.

## Common Causes

- The image name or tag is misspelled
- The image was never pushed to the specified registry
- The image tag was overwritten or removed from the registry
- Authentication is required but not configured for the private registry
- The image was deleted locally with `docker rmi`

## Solutions

### Solution 1: Pull the Image Explicitly

Pull the image directly from the registry to get verbose error output. This confirms whether the image exists and whether authentication is needed.

```bash
docker pull myregistry.com/myapp:latest
```

### Solution 2: Rebuild the Image Locally

If the image is built from a local Dockerfile, rebuild it with the correct tag. Use `docker images` to verify available tags afterward.

```bash
docker build -t myregistry.com/myapp:latest .
docker images | grep myapp
```

### Solution 3: Log In to a Private Registry

For private registries, authenticate before pulling. Docker will reject pulls from private registries without valid credentials.

```bash
docker login myregistry.com
# Enter username and password
docker pull myregistry.com/myapp:latest
```

### Solution 4: Use the Correct Tag

Check available tags on the registry to ensure you are referencing an existing version. Many registries remove `latest` or old tags periodically.

```bash
# Check available tags for an image
curl -s "https://hub.docker.com/v2/repositories/library/nginx/tags/?page_size=5" | python3 -m json.tool
docker pull nginx:1.27-alpine
```

## Prevention Tips

- Always specify explicit tags instead of relying on `latest` in production
- Pin base image digests in Dockerfiles for reproducible builds
- Verify image availability in CI pipelines before starting deployment steps
- Keep a local registry mirror for critical base images

## Related Errors

- [Docker Pull Failed]({{< relref "/tools/docker/pull-failed" >}}) — image pull failure
- [Docker Connection Refused]({{< relref "/tools/docker/connection-refused" >}}) — cannot reach Docker daemon
