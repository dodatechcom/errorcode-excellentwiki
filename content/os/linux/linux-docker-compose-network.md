---
title: "[Solution] Linux docker compose Network Creation Error"
description: "Fix Linux 'docker compose' network creation errors. Resolve network driver issues, IP conflicts, and Docker Compose networking problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: docker compose — network creation error

The `docker compose` network creation error such as `NetworkErrorCode 409: failed to create network` or `could not create network` means Docker Compose could not create the requested network because a network with that name already exists, the driver is unavailable, or IP allocation failed.

## What This Error Means

Docker Compose automatically creates a network for each project (named `<project>_default`). When you run `docker compose up`, it tries to create this network. If a leftover network from a previous run still exists, or if the network driver has issues, creation fails. IPAM (IP Address Management) conflicts can also prevent network creation.

## Common Causes

- Stale network from a previous `docker compose` run
- Network name conflict with a manually created network
- Docker network driver not loaded or unavailable
- IP address pool exhausted
- Subnet overlap with existing Docker or host networks
- Docker daemon restart left orphaned networks

## How to Fix

### 1. Check Existing Networks

```bash
# List all Docker networks
docker network ls

# Inspect the conflicting network
docker network inspect <network-name>

# Check which containers use each network
docker network inspect <network-name> | grep -A5 'Containers'
```

### 2. Remove Stale Networks

```bash
# Remove unused networks
docker network prune -f

# Remove a specific network
docker network rm <network-name>

# Force remove even if in use
docker network disconnect -f <network-name> <container>
docker network rm <network-name>
```

### 3. Fix Compose Project Name

```bash
# Compose uses directory name as project name
# Ensure unique directory names, or set explicitly:
export COMPOSE_PROJECT_NAME=myproject

# Or in docker-compose.yml:
# networks:
#   default:
#     name: myproject-network
```

### 4. Define Custom Network Config

```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    networks:
      - custom-net

networks:
  custom-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
          gateway: 172.28.0.1
```

### 5. Fix IPAM Exhaustion

```bash
# Check IP address usage per network
docker network inspect bridge | grep -A20 'IPAM'

# Remove networks with exhausted pools
docker network prune -f

# Or use a larger subnet in docker-compose.yml
```

### 6. Restart Docker Daemon

```bash
# Restart clears orphaned state
sudo systemctl restart docker

# Recreate the network
docker compose down
docker compose up -d
```

### 7. Specify Network Driver

```bash
# Ensure the required driver is available
docker info | grep -i 'network\|driver'

# Use bridge (default for single host)
# Use overlay for Swarm mode
# Use macvlan for direct network access
```

## Examples

```bash
$ docker compose up -d
[+] Running 0/1
 ✘ Network myproject_default Error  failed to create network myproject_default: Error response from daemon: could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network

$ docker network ls
NETWORK ID     NAME                DRIVER
abc123         myproject_default   bridge
def456         myproject_default   bridge    # Stale from old run

$ docker network rm def456
$ docker compose up -d
[+] Running 2/2
 ✔ Network myproject_default  Created
 ✔ Container myapp            Started
```

## Related Errors

- [Docker network error]({{< relref "/os/linux/linux-docker-network-error" >}}) — General Docker network issues
- [Docker compose volume]({{< relref "/os/linux/linux-docker-compose-volumes" >}}) — Volume mount errors
- [Docker compose error]({{< relref "/os/linux/linux-docker-compose-error" >}}) — General compose errors
