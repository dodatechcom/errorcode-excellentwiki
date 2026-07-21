---
title: "Docker Container OOM Killed"
description: "Docker container killed by OOM killer due to memory limit exceeded"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Container OOM Killed

Docker container killed by OOM killer due to memory limit exceeded

## Common Causes

- Memory limit set too low for container workload
- Memory leak in application inside container
- Multiple containers competing for host memory
- No swap limit configured allowing unbounded growth

## How to Fix

1. Check container memory: `docker stats <container>`
2. Increase memory limit: `docker update --memory=2g <container>`
3. Set swap limit: `docker update --memory-swap=4g <container>`
4. Check host memory: `free -h`

## Examples

```bash
# Check container memory usage
docker stats --no-stream

# Increase memory limit
docker update --memory=2g --memory-swap=4g mycontainer

# Check if container was OOM killed
docker inspect mycontainer | grep -i oom
```
