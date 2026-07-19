---
title: "[Solution] Docker No Space Left on Device — no space left on device"
description: "Fix Docker no space left on device error. Clean up Docker images, containers, and build cache."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 2
---

# no space left on device

This error means the disk hosting Docker storage has run out of space. Docker accumulates images, containers, volumes, and build cache that consume disk space over time.

## Common Causes

- Unused Docker images taking up space
- Stopped containers still using disk
- Build cache growing very large
- Container log files filling disk
- Large volumes with data

## How to Fix

### Check Docker Disk Usage

```bash
docker system df
```

### Aggressive Cleanup

```bash
docker system prune -a --volumes
```

### Remove Only Unused Images

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

### Remove Unused Volumes

```bash
docker volume prune
```

### Check Host Disk Space

```bash
df -h /var/lib/docker
```

## Examples

```bash
# Example 1: Full cleanup
docker system df
# TYPE          TOTAL   ACTIVE  SIZE    RECLAIMABLE
# Images        25      3       8.2GB   7.8GB (95%)
docker system prune -a --volumes

# Example 2: Remove dangling images only
docker image prune
# Deleted: sha256:abc123...

# Example 3: Check specific path
du -sh /var/lib/docker/overlay2/
```

## Related Errors

- [No space left on device]({{< relref "/tools/docker/no-space" >}}) — related error
- [Docker out of memory]({{< relref "/tools/docker/docker-out-of-memory" >}}) — related error
