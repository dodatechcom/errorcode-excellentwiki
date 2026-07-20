---
title: "[Solution] Docker Network Error — Network not found"
description: "Fix Docker 'Network not found' error. Create and manage networks for container-to-container communication."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "networking", "bridge", "containers"]
severity: "error"
weight: 6
---

# ERROR: Network not found

## Error Message

```
Error: Network myapp_default not found

Error response from daemon: network myapp_default not found: not found
```

This error occurs when a container or Compose project references a Docker network that does not exist. Containers cannot start if their required network has not been created first.

## Common Causes

- The network was removed while containers were still attached to it
- `docker compose down` removed the project network
- The network name is misspelled in the Compose file or run command
- You are referencing a network from a different Compose project that is not running

## Solutions

### Solution 1: Create the Network and Recreate Containers

Create the missing network with the exact name your Compose file expects, then restart the containers.

```bash
docker network create myapp_default
docker compose up -d
```

### Solution 2: Let Compose Create the Network

Define the network explicitly in your Compose file so `docker compose up` creates it automatically. This is the recommended approach for new projects.

```yaml
services:
  web:
    image: nginx:alpine
    networks:
      - frontend
  api:
    image: node:20
    networks:
      - frontend
      - backend

networks:
  frontend:
  backend:
```

```bash
docker compose up -d
```

### Solution 3: Inspect and Recover an Existing Network

Check what networks currently exist and reconnect containers to the correct one if they drifted to the wrong network.

```bash
docker network ls
docker network inspect myapp_default
docker network connect myapp_default my_container
```

### Solution 4: Use the Host Network for Simple Setups

For single-container setups or debugging, use the host network to bypass network configuration entirely.

```bash
docker run --network host myimage
```

## Prevention Tips

- Always define networks in your Compose file rather than relying on automatic creation
- Use `docker compose up --remove-orphans` to clean up stale network references
- Avoid manually removing networks that active Compose projects depend on
- Name your networks explicitly to avoid collisions with default project networks

## Related Errors

- [Docker Port Conflict]({{< relref "/tools/docker/port-conflict" >}}) — port is already allocated
- [Docker DNS Resolution Failed]({{< relref "/tools/docker/dns-resolution-failed" >}}) — DNS lookup failures
