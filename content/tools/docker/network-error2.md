---
title: "[Solution] Docker Network Error — network not found"
description: "Fix Docker network not found error. Create and manage Docker networks for container communication."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Network Error — network not found

This error occurs when a container tries to connect to a Docker network that doesn't exist. Networks must be created before containers can use them.

## Common Causes

- Network was not created before running the container
- Network name typo
- Network was removed while containers were running
- Using compose without specifying network explicitly

## How to Fix

### List Available Networks

```bash
docker network ls
```

### Create a New Network

```bash
docker network create <network-name>
```

### Connect Container to Network

```bash
docker network connect <network-name> <container>
```

### Run Container with Specific Network

```bash
docker run --network <network-name> <image>
```

### Inspect Network

```bash
docker network inspect <network-name>
```

### Create Bridge Network

```bash
docker network create --driver bridge my-network
```

## Examples

```bash
# Example 1: Container can't reach another container
docker run --network my-net my-app
# Error: network my-net not found
# Fix: docker network create my-net

# Example 2: Docker Compose network issue
docker compose up
# Error: network myproject_default not found
# Fix: docker compose up --build

# Example 3: Inspect existing networks
docker network ls
# NETWORK ID     NAME      DRIVER
# abc123         bridge    bridge
# def456         host      host
```

## Related Errors

- [Port Conflict]({{< relref "/tools/docker/port-conflict" >}}) — port is already allocated
- [Compose Error]({{< relref "/tools/docker/compose-error" >}}) — docker compose configuration error
