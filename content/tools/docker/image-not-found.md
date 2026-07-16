---
title: "[Solution] Docker No Such Image — Error response from daemon: No such image"
description: "Fix Docker 'No such image' error. Resolve missing image issues with docker pull, image naming, and local cache."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["image-not-found", "no-such-image", "daemon", "pull"]
weight: 5
---

# Docker No Such Image — Error response from daemon: No such image

This error occurs when Docker cannot find the specified image locally or in the remote registry. Docker needs to pull the image before it can create or run a container from it.

## Common Causes

- Image has not been pulled from the registry yet
- Typo in the image name or tag
- Image was previously deleted from local cache
- Using a private registry without being logged in

## How to Fix

### Pull the Image

```bash
docker pull <image-name>:<tag>
```

### Verify Image Exists Locally

```bash
docker images
```

### Check for Typos in Image Name

```bash
# List available images and compare
docker images | grep <partial-name>
```

### Login to Private Registry

```bash
docker login <registry-url>
docker pull <registry-url>/<image-name>:<tag>
```

### Rebuild the Image Locally

```bash
docker build -t <image-name>:<tag> .
```

## Examples

```bash
# Example 1: Missing image
docker run nginx:1.25
# Error: No such image: nginx:1.25
# Fix: docker pull nginx:1.25

# Example 2: Typo in image name
docker run my-aplication:latest
# Error: No such image: my-aplication:latest
# Fix: docker run my-application:latest

# Example 3: Private registry
docker pull registry.example.com/my-app:v1
# Error: unauthorized
# Fix: docker login registry.example.com
```

## Related Errors

- [Port In Use]({{< relref "/tools/docker/port-in-use" >}}) — port binding conflicts when running containers
- [ImagePullBackOff]({{< relref "/tools/kubernetes/imagepullbackoff" >}}) — Kubernetes fails to pull the image
