---
title: "[Solution] Docker Port Already In Use — Bind for 0.0.0.0:80: address already in use"
description: "Fix Docker port conflict error. Resolve 'address already in use' when binding container ports."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Port Already In Use — Bind for 0.0.0.0:80: address already in use

This error means the host port you are trying to bind to a container is already occupied by another process or another container.

## Common Causes

- Another container is already using the same host port
- A host service (like nginx or apache) is listening on that port
- A previous container was not properly removed
- Multiple containers mapping to the same host port

## How to Fix

### Find What Is Using the Port

```bash
sudo lsof -i :80
sudo ss -tlnp | grep :80
sudo netstat -tlnp | grep :80
```

### Stop the Conflicting Container

```bash
docker ps
docker stop <container-name>
```

### Use a Different Host Port

```bash
docker run -p 8080:80 <image-name>
```

### Remove Stopped Containers

```bash
docker ps -a
docker rm <container-name>
```

### Kill the Conflicting Process

```bash
sudo kill -9 <pid>
```

## Examples

```bash
# Example 1: Port 80 already in use
docker run -p 80:80 nginx
# Error: Bind for 0.0.0.0:80: address already in use
# Fix: use different port
docker run -p 8080:80 nginx

# Example 2: Previous container still running
docker ps -a
# CONTAINER ID   IMAGE   STATUS
# abc123         nginx   Exited (0) 5 minutes ago
docker rm abc123
docker run -p 80:80 nginx
```

## Related Errors

- [Image Not Found]({{< relref "/tools/docker/image-not-found" >}}) — missing Docker image
- [Upstream Error]({{< relref "/tools/nginx/upstream-error" >}}) — Nginx 502 when upstream container is down
