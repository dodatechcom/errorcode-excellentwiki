---
title: "LXD Image Download Error"
description: "Failed to download container images from image servers"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Image Download Error

Failed to download container images from image servers

## Common Causes

- Image server unreachable or down
- Network proxy blocking image downloads
- Insufficient disk space in /var/snap/lxd/
- GPG signature verification failed

## How to Fix

1. Check image server status: `lxc image list images: ubuntu`
2. Try alternative mirror
3. Verify network connectivity: `curl -I https://images.linuxcontainers.org`
4. Clear image cache: `lxc image delete <cached-image>`

## Examples

```bash
# List available Ubuntu images
lxc image list images: ubuntu amd64

# Download specific image
lxc image copy images:ubuntu/22.04 local: --alias ubuntu-jammy

# Check image server connectivity
curl -sI https://images.linuxcontainers.org | head -5
```
