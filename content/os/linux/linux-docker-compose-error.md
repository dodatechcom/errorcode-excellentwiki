---
title: "[Solution] docker-compose: Network Error — Failed to Create Network"
description: "Fix docker-compose network errors. Resolve 'Failed to create the docker network' and bridge network creation failures in docker-compose."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# docker-compose: Network Error — Failed to Create Network

The docker-compose network error occurs when `docker-compose up` fails to create the required Docker network. The error message reads:

> "ERROR: Failed to create the docker network"

Or:

> "driver failed programming external connectivity on network: failed to set up sandbox"

## What This Error Means

Docker Compose creates a default network for each project (named `<project>_default`). When the Docker daemon cannot create this network — due to subnet conflicts, IPAM pool exhaustion, or bridge driver failures — `docker-compose up` fails before any containers start.

## Common Causes

- IP subnet conflict with existing Docker networks or host networks
- Docker IPAM pool exhausted (too many networks)
- Docker bridge interface in a bad state
- iptables rules blocking Docker network setup
- Docker daemon not running or corrupted

## How to Fix

### Remove Unused Docker Networks

```bash
# List all networks
docker network ls

# Remove unused networks
docker network prune -f

# Remove a specific project network
docker-compose down
docker network rm <project>_default
```

### Check for Subnet Conflicts

```bash
# List all Docker networks and their subnets
docker network inspect $(docker network ls -q) | grep -A2 "Subnet"

# Check host network
ip addr show docker0
ip route | grep docker
```

### Restart Docker Daemon

```bash
sudo systemctl restart docker
sudo systemctl status docker
```

### Fix IPAM Pool

```bash
# Check IPAM configuration
docker network inspect bridge | grep -A10 "IPAM"

# Remove all networks and containers
docker-compose down -v --remove-orphans
docker network prune -f
```

### Configure Custom Subnet in docker-compose.yml

```yaml
version: "3.8"
services:
  app:
    image: nginx
    networks:
      - custom

networks:
  custom:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
          gateway: 172.28.0.1
```

### Fix iptables Rules

```bash
# Flush Docker iptables rules
sudo iptables -F
sudo iptables -t nat -F
sudo systemctl restart docker
```

## Related Errors

- [Docker Network Bridge Error]({{< relref "/os/linux/linux-docker-network-error" >}}) — Bridge network configuration issues
- [Docker Socket Permission Denied]({{< relref "/os/linux/linux-docker-socket-permission" >}}) — Docker daemon access issues
- [Docker Container OOM Killed]({{< relref "/os/linux/linux-docker-out-of-memory" >}}) — Container memory limits exceeded
