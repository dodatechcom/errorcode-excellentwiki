---
title: "[Solution] Docker Load Error"
description: "Fix Docker load errors. Resolve tar image import failures and corrupted archive issues."
tools: ["docker"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["load", "import", "tar", "image", "archive", "docker"]
weight: 5
---

## What This Error Means

A Docker load error occurs when `docker load` cannot import a Docker image from a tar archive. The archive may be corrupted, incomplete, or in an unexpected format. This command is used to restore images exported with `docker save`.

## Common Causes

- Tar file is corrupted or incomplete (truncated download)
- File is not a valid Docker save archive
- Archive was created with an incompatible Docker version
- Insufficient disk space for image layers
- File permissions prevent reading the tar archive
- Using `docker import` on a `docker save` archive (wrong command)

## How to Fix

### Verify the File Exists and is Valid

```bash
ls -lh my-image.tar
file my-image.tar
```

### Load the Image

```bash
docker load -i my-image.tar
```

### Load from stdin

```bash
docker load < my-image.tar
```

### Load Compressed Archive

```bash
gunzip -c my-image.tar.gz | docker load
```

### Check Docker Disk Space

```bash
docker system df
docker system prune -a
```

### Re-download the Archive

```bash
# If downloaded from a URL, re-download
wget -O my-image.tar <url>
```

## Examples

```bash
# Example 1: Basic load
docker load -i my-image.tar
# Loaded image: my-app:1.0

# Example 2: Load compressed archive
gunzip -c my-image-1.0.tar.gz | docker load
# Loaded image: my-app:1.0

# Example 3: Corrupted file
docker load -i my-image.tar
# Error: invalid tar header
# Fix: re-download or re-save the file

# Example 4: Wrong command
docker import my-image.tar my-app
# This creates a flat image without layers
# Use docker load instead for proper layer preservation
```

## Related Errors

- [Docker Save Error]({{< relref "/tools/docker/docker-save-error" >}}) — image export failure
- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit-error" >}}) — BuildKit build error
- [Docker Volume Error]({{< relref "/tools/docker/docker-volume-error-v2" >}}) — volume mount permission denied
