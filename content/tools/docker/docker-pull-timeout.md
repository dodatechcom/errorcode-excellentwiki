---
title: "[Solution] Docker Pull Timeout — pull timeout"
description: "Fix Docker pull timeout errors. Resolve image pull failures from registries."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["pull", "timeout", "registry", "download", "docker"]
weight: 5
---

A Docker pull timeout occurs when downloading an image from a registry takes too long. This is common with large images or slow network connections.

## Common Causes

- Slow or unstable network connection
- Large image with many layers to download
- Registry server is overloaded or slow
- Firewall or proxy blocking the connection
- Insufficient disk space to extract layers

## How to Fix

### Check Disk Space

```bash
docker system df
df -h
```

### Use a Mirror Registry

```bash
# Configure daemon mirror
sudo tee /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": ["https://mirror.gcr.io"]
}
EOF
sudo systemctl restart docker
```

### Pull with Timeout Settings

```bash
docker pull --timeout 300s my-image:latest
```

### Clean Up Unused Images

```bash
docker system prune -a
```

### Check Network Connectivity

```bash
curl -v https://registry-1.docker.io/v2/
```

## Examples

```bash
# Example 1: Pull large image
docker pull postgres:15
# timeout: deadline exceeded
# Fix: increase timeout or use mirror

# Example 2: Clean up and retry
docker system prune -a
docker pull nginx:alpine

# Example 3: Configure mirror
sudo systemctl restart docker
docker pull my-image:latest
```

## Related Errors

- [Docker Image Not Found]({{< relref "/tools/docker/docker-image-not-found" >}}) — image not found in registry
- [Docker Build Cache]({{< relref "/tools/docker/docker-build-cache" >}}) — build cache error
