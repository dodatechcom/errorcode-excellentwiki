---
title: "[Solution] Docker No Space Left — no space left on device"
description: "Fix Docker no space left on device error. Free disk space and clean up Docker resources."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["no-space", "disk-full", "device", "cleanup", "docker"]
weight: 5
---

# Docker No Space Left — no space left on device

This error occurs when the disk running Docker is full. Docker images, containers, and build cache consume significant disk space over time.

## Common Causes

- Accumulated unused Docker images
- Stopped containers taking up space
- Docker build cache growing large
- Log files from containers filling disk

## How to Fix

### System Docker Cleanup

```bash
docker system prune -a
```

### Remove Unused Images

```bash
docker image prune -a
```

### Remove Stopped Containers

```bash
docker container prune
```

### Remove Build Cache

```bash
docker builder prune -a
```

### Check Docker Disk Usage

```bash
docker system df
```

### Remove Unused Volumes

```bash
docker volume prune
```

## Examples

```bash
# Example 1: Check disk usage
docker system df
# TYPE          TOTAL   ACTIVE  SIZE    RECLAIMABLE
# Images        15      3       4.2GB   3.8GB (90%)

# Example 2: Aggressive cleanup
docker system prune -a --volumes
# Will remove all unused images, containers, networks, and volumes

# Example 3: Check host disk space
df -h /var/lib/docker
```

## Related Errors

- [Build Failed]({{< relref "/tools/docker/build-failed2" >}}) — COPY failed during build
- [Layer Cache]({{< relref "/tools/docker/layer-cache" >}}) — cache not found during build
