---
title: "[Solution] Ubuntu Server: docker-overlay2-error"
description: "Fix Ubuntu docker-overlay2-error. Docker overlay2 storage driver encounters errors."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Docker Overlay2 Error

Docker overlay2 storage driver fails or encounters corruption.

## Common Causes
- Overlay2 filesystem corrupted
- Insufficient inodes
- Kernel does not support overlay2
- /var/lib/docker disk full

## How to Fix
1. Check storage driver
```bash
docker info | grep "Storage Driver"
```
2. Check disk space
```bash
df -h /var/lib/docker
```
3. Clean up Docker
```bash
docker system prune -a
docker volume prune
```

## Examples
```bash
$ docker info | grep "Storage Driver"
 Storage Driver: overlay2
```