---
title: "[Solution] Docker No Matching Manifest — no matching manifest for platform"
description: "Fix Docker no matching manifest error. Resolve platform and architecture mismatches."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# no matching manifest for linux/arm64 in the manifest list entries

This error occurs when the requested image does not have a build for your system's platform or architecture. Common on ARM64 (Apple Silicon) systems pulling images built only for AMD64.

## Common Causes

- Image not built for your CPU architecture (ARM64 vs AMD64)
- Multi-arch manifest missing for your platform
- Using --platform flag incorrectly
- Old image without multi-architecture support

## How to Fix

### Check Your Platform

```bash
docker info --format '{{.Architecture}}'
# or
uname -m
```

### Use Specific Platform

```bash
docker pull --platform linux/amd64 <image>:<tag>
```

### Find Available Platforms

```bash
docker manifest inspect <image>:<tag>
```

### Use QEMU for Emulation

```bash
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

### Build for Multiple Platforms

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t myimage .
```

## Examples

```bash
# Example 1: ARM64 Mac pulling AMD64 image
docker pull --platform linux/amd64 nginx:latest

# Example 2: Check manifest
docker manifest inspect nginx:latest
# Shows available platforms

# Example 3: Build multi-arch
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t myimage:latest .
```

## Related Errors

- [Image not found / manifest unknown]({{< relref "/tools/docker/image-not-found-manifest-unknown" >}}) — related error
- [Docker image not found]({{< relref "/tools/docker/docker-image-not-found" >}}) — related error
