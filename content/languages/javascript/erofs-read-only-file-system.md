---
title: "[Solution] EROFS — Read-Only File System Error"
description: "Fix EROFS when attempting to write to a read-only mount point or container filesystem."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EROFS — Read-Only File System

Attempting to write to a read-only filesystem.

## Causes

- Docker container filesystem is read-only
- NFS mount is mounted read-only
- Disk mounted with noexec/readonly

## Fix

```bash
# Remount read-write (if you have permission)
sudo mount -o remount,rw /mount/point
```

In Docker, use a volume for writable directories:

```bash
docker run -v /host/writable:/app/writable myimage
```
