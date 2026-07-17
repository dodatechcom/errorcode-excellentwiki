---
title: "[Solution] Docker Container OOM Killed — container killed"
description: "Fix Docker container OOM killed errors. Resolve out-of-memory issues in Docker containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["oom", "killed", "memory", "limit", "docker"]
weight: 5
---

A Docker container OOM (Out of Memory) killed error occurs when a container exceeds its memory limit and the Linux kernel terminates it. The container exits with status code 137.

## Common Causes

- Container memory limit is too low for the application
- Memory leak in the application causing gradual memory increase
- Application requires more memory during startup (JVM, Node.js)
- No memory limit set and host runs out of memory
- Multiple containers competing for host memory

## How to Fix

### Check Container Memory Usage

```bash
docker stats <container>
```

### Increase Memory Limit

```bash
docker run -m 2g --memory-swap 4g my-image
```

### Check OOM Kill Events

```bash
docker inspect <container> | grep -i oom
dmesg | grep -i "oom\|kill"
```

### Set Memory Limits in Compose

```yaml
services:
  app:
    image: my-image
    deploy:
      resources:
        limits:
          memory: 2G
```

### Monitor Memory Usage

```bash
docker stats --format "table {{.Name}}\t{{.MemUsage}}"
```

## Examples

```bash
# Example 1: Run with increased memory
docker run -m 4g --memory-swap 8g my-java-app

# Example 2: Check OOM status
docker inspect my-container | grep OOMKilled
# "OOMKilled": true

# Example 3: Set memory limit in compose
# docker-compose.yml
# services:
#   app:
#     image: my-image
#     mem_limit: 2g
```

## Related Errors

- [Docker Healthcheck Fail]({{< relref "/tools/docker/docker-healthcheck-fail" >}}) — Docker healthcheck failed
- [Docker Out of Memory]({{< relref "/tools/docker/docker-out-of-memory" >}}) — container OOM killed
