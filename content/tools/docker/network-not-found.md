---
title: "[Solution] Docker Network Not Found — network not found"
description: "Fix Docker network not found error. Create and configure Docker networks properly."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# network not found

This error occurs when a container references a Docker network that does not exist. The network may have been deleted, never created, or has a typo in its name.

## Common Causes

- Network was deleted or never created
- Typo in network name
- Using a network from a removed docker-compose project
- Container referencing network from different compose file

## How to Fix

### List Available Networks

```bash
docker network ls
```

### Create the Network

```bash
docker network create my-network
```

### Create with Subnet

```bash
docker network create --subnet=172.20.0.0/16 my-network
```

### Connect to Existing Network

```bash
docker network connect my-network <container>
```

### Create Bridge Network

```bash
docker network create --driver bridge my-bridge
```

## Examples

```bash
# Example 1: List networks
docker network ls
# NETWORK ID     NAME      DRIVER
# abc123         bridge    bridge
# def456         host      host

# Example 2: Create and use network
docker network create my-app-net
docker run --network my-app-net nginx

# Example 3: Fix compose network
docker-compose up -d
# Creates network from compose file automatically
```

## Related Errors

- [Docker network error]({{< relref "/tools/docker/docker-network-error" >}}) — related error
- [Network configuration error]({{< relref "/tools/docker/docker-network-error-v2" >}}) — related error
