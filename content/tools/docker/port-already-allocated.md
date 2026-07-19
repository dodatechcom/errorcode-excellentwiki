---
title: "[Solution] Docker Port Already Allocated — port is already allocated"
description: "Fix Docker port already allocated error. Free up ports or use dynamic port assignment."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

# port is already allocated

This error occurs when you try to bind a container to a host port that is already in use by another process or container.

## Common Causes

- Another container is using the same port
- Host service using the port (nginx, apache, etc.)
- Previous container not fully cleaned up
- Port left in TIME_WAIT state after restart

## How to Fix

### Find What Is Using the Port

```bash
sudo lsof -i :8080
# or
sudo ss -tlnp | grep 8080
```

### Stop the Conflicting Container

```bash
docker ps --filter publish=8080
docker stop <container>
```

### Use Different Port

```bash
docker run -p 9090:80 nginx
```

### Use Dynamic Port Assignment

```bash
docker run -P nginx
# Check assigned port with: docker ps
```

### Kill Host Process

```bash
sudo kill $(sudo lsof -t -i:8080)
```

## Examples

```bash
# Example 1: Find port conflict
sudo lsof -i :8080
# COMMAND   PID  USER   FD   TYPE DEVICE
# docker   1234 root   6u   IPv4 ...

# Example 2: Use different port
docker run -p 8081:80 nginx

# Example 3: Check all published ports
docker ps --format "{{.Ports}}"
```

## Related Errors

- [Port conflict]({{< relref "/tools/docker/port-conflict" >}}) — related error
- [Port in use]({{< relref "/tools/docker/port-in-use" >}}) — related error
