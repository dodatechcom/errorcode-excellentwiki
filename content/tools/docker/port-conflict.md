---
title: "[Solution] Docker Port Conflict — port is already allocated"
description: "Fix Docker port already allocated error. Resolve port binding conflicts when running containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Port Conflict — port is already allocated

This error occurs when a container tries to bind to a host port that is already in use by another process or container.

## Common Causes

- Another container is already using the same port
- A host service is using the port (e.g., nginx, apache)
- Previous container didn't release the port properly
- Port mapping conflict in docker-compose

## How to Fix

### Find Process Using the Port

```bash
lsof -i :<port>
```

### Find Docker Container Using Port

```bash
docker ps --filter "publish=<port>"
```

### Stop Conflicting Container

```bash
docker stop <container-id>
```

### Use Different Host Port

```bash
docker run -p <new-port>:80 <image>
```

### Use Random Port

```bash
docker run -P <image>
```

### Check All Port Bindings

```bash
docker port <container>
```

## Examples

```bash
# Example 1: Port 80 already in use
docker run -p 80:80 nginx
# Error: port is already allocated
# Fix: docker run -p 8080:80 nginx

# Example 2: Find conflicting container
docker ps --filter "publish=80"
# CONTAINER ID   IMAGE   PORTS
# abc123         nginx   0.0.0.0:80->80/tcp
# Fix: docker stop abc123

# Example 3: Check host process
lsof -i :80
# Fix: stop the host process or use different port
```

## Related Errors

- [Network Error]({{< relref "/tools/docker/network-error2" >}}) — network not found
- [Compose Error]({{< relref "/tools/docker/compose-error" >}}) — docker compose configuration error
