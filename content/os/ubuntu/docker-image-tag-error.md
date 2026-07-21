---
title: "Docker Image Tag Error"
description: "Docker image tag operation fails or tag references wrong image"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Image Tag Error

Docker image tag operation fails or tag references wrong image

## Common Causes

- Image does not exist locally or in registry
- Tag format invalid (must be lowercase, no special chars)
- Registry authentication required but not logged in
- Tag already exists on different image digest

## How to Fix

1. List images: `docker images`
2. Check registry login: `docker login <registry>`
3. Verify tag format: lowercase letters, numbers, dashes, underscores, dots, slashes
4. Force tag: `docker tag <image> <new-tag> --force`

## Examples

```bash
# List all images
docker images

# Tag an image
docker tag myapp:latest myregistry.com/myapp:v1.0

# Push tagged image
docker push myregistry.com/myapp:v1.0
```
