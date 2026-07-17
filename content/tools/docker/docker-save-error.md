---
title: "[Solution] Docker Save Error"
description: "Fix Docker save errors. Resolve image export and tar archive creation failures."
tools: ["docker"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["save", "export", "image", "tar", "archive", "docker"]
weight: 5
---

## What This Error Means

A Docker save error occurs when `docker save` cannot export a Docker image to a tar archive. This is used to transfer images between hosts without a registry. Failures typically involve missing images, disk space issues, or permission problems.

## Common Causes

- Image name or tag does not exist locally
- Insufficient disk space for the output tar file
- Output file path is not writable
- Image is too large for available memory
- Docker daemon cannot access the image layer data

## How to Fix

### List Available Images

```bash
docker images
```

### Save a Single Image

```bash
docker save -o my-image.tar my-image:latest
```

### Save Multiple Images

```bash
docker save -o images.tar my-image:latest my-image:dev nginx:alpine
```

### Save by Image ID

```bash
docker save -o my-image.tar abc1234def
```

### Check Disk Space

```bash
df -h
du -sh /var/lib/docker
```

### Compress While Saving

```bash
docker save my-image:latest | gzip > my-image.tar.gz
```

## Examples

```bash
# Example 1: Save and load between hosts
# On host A:
docker save -o my-app.tar my-app:1.0

# Transfer the file
scp my-app.tar user@host-b:/tmp/

# On host B:
docker load -i /tmp/my-app.tar

# Example 2: Save compressed image
docker save my-app:1.0 | gzip > my-app-1.0.tar.gz

# Example 3: Save all images for backup
docker save $(docker images -q) -o all-images.tar
```

## Related Errors

- [Docker Load Error]({{< relref "/tools/docker/docker-load-error" >}}) — image load failure
- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit-error" >}}) — BuildKit build error
- [Docker Compose Error]({{< relref "/tools/docker/docker-compose-error-v2" >}}) — docker compose up failed
