---
title: "[Solution] macOS Docker Error -- Docker Desktop Not Starting or Containers Failing"
description: "Fix macOS Docker error when Docker Desktop fails to start or containers do not run. Resolve Docker issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Docker Error -- Docker Desktop Not Starting or Containers Failing

Docker Desktop on macOS runs containers in a Linux VM. When Docker fails, the VM may not start, containers may crash, or the Docker daemon may be unresponsive.

## Common Causes
- Docker Desktop VM resources are insufficient
- Disk space is full and Docker cannot start
- Docker configuration is corrupted
- HyperKit/Virtualization framework issue
- Docker daemon is not responding

## How to Fix
1. Check available disk space -- Docker needs at least 10 GB free
2. Reset Docker Desktop to factory defaults
3. Increase Docker VM resources in preferences
4. Restart Docker Desktop
5. Check Docker logs for specific error messages

```bash
# Check Docker status
docker info

# Reset Docker Desktop
# Docker Desktop > Troubleshoot > Reset to factory defaults

# Check Docker disk usage
docker system df
```

## Examples

```bash
# View Docker logs
cat ~/Library/Containers/com.docker.docker/Data/log/*.log

# Check Docker daemon status
docker ps
```

This error is common when disk space is full, when the Docker VM has insufficient resources, or when Docker Desktop configuration is corrupted.
