---
title: "[Solution] Docker Container OOM Killed — Out of Memory"
description: "Fix Docker container OOM (Out of Memory) killed errors on Linux. Resolve memory limit issues, OOM killer, and container memory management."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Docker Container OOM Killed — Out of Memory

A Docker container OOM killed error occurs when the Linux OOM (Out of Memory) killer terminates a container because it exceeded its memory limit or the host ran out of memory. The error reads:

> "container [name] exceeded memory limit"

Or in `docker inspect`:

> "OOMKilled": true

## What This Error Means

Docker uses Linux cgroups to enforce memory limits on containers. When a container's memory usage exceeds its configured limit, the kernel's OOM killer selects the container's process as the victim and sends `SIGKILL`. If no memory limit is set, the host's OOM killer may still kill the container when the host runs out of memory.

## Common Causes

- Container memory limit set too low for the workload
- Memory leak in the application
- No memory limit set (uses host memory freely, then gets OOM'd by host)
- Node running too many containers
- JVM not aware of container memory limits (pre-Java 10)

## How to Fix

### Check Container Memory Usage

```bash
# Real-time memory stats
docker stats --no-stream

# Check OOM status
docker inspect <container> | grep -i oom

# Check memory limits
docker inspect <container> | grep -i memory
```

### Increase Memory Limit

```bash
# Set memory limit on run
docker run --memory=2g --memory-swap=4g myimage

# Update in docker-compose.yml
# services:
#   app:
#     deploy:
#       resources:
#         limits:
#           memory: 2G
```

### Detect Memory Leaks

```bash
# Monitor memory usage over time
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}"

# Use heaptrack or valgrind inside the container
docker run --rm -it --entrypoint sh myimage
```

### Configure JVM for Containers

```bash
# Java 10+ automatically detects container memory limits
# For older JVMs, set explicitly:
docker run -e JAVA_OPTS="-XX:MaxRAMPercentage=75.0" myimage
```

### Increase Host Memory or Swap

```bash
# Add swap space
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### Use --oom-kill-disable (Temporary)

```bash
# Disable OOM killer for a specific container (dangerous)
docker run --oom-kill-disable --memory=2g myimage
```

## Related Errors

- [k8s OOMKilled]({{< relref "/os/linux/linux-k8s-oom-killed" >}}) — Kubernetes pod OOM killed
- [OOM Killer]({{< relref "/os/linux/oom-killer" >}}) — Linux OOM killer events
- [Docker Healthcheck Failed]({{< relref "/os/linux/linux-docker-healthcheck" >}}) — Container health check failures
