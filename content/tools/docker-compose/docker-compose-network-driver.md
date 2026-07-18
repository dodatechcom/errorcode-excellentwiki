---
title: "[Solution] Docker Compose Network Driver Error — How to Fix"
description: "Fix Docker Compose network driver not supported errors. Resolve driver compatibility, plugin issues, and overlay network failures now."
comments: true
---

## What This Error Means

The `network driver not supported` error occurs when Docker Compose tries to create or use a network with a driver that is not available on the current Docker installation. The specified driver either does not exist, is not installed, or is incompatible with the platform.

A typical error:

```
ERROR: Failed to setup the services network:
network driver not supported: overlay
```

Or:

```
Error response from daemon: could not find driver bridge:
driver not found
```

Or:

```
network error: plugin "overlay" not found
```

Or:

```
ERROR: for myservice  network "myproject_default" not found
failed to create network myproject_default: Error response
from daemon: driver failed programming external connectivity
```

## Why It Happens

Network driver errors occur when:

- **Driver not installed**: The requested driver (such as `overlay` or `macvlan`) requires a plugin that is not installed.
- **Swarm mode not active**: The `overlay` driver requires Docker Swarm, which may not be initialized.
- **Platform limitations**: Some drivers are only available on specific platforms (Linux vs. Docker Desktop).
- **Docker version mismatch**: Older Docker versions may not support newer network drivers.
- **Custom driver configuration**: A third-party network plugin was uninstalled but the compose file still references it.
- **Compose file version conflict**: The compose file specifies a driver using syntax incompatible with the installed Compose version.

## Common Error Messages

### Overlay driver not found

```
ERROR: could not find driver overlay
```

This happens when Docker Swarm is not initialized. The `overlay` driver is only available in swarm mode or when the daemon has swarm capabilities enabled.

### Macvlan driver unsupported

```
Error response from daemon: network driver not supported: macvlan
```

Some Docker Desktop environments and restricted daemon configurations do not support the `macvlan` network driver due to kernel limitations.

### Bridge network creation failure

```
ERROR: Failed to create the Docker network myproject_default
Error response from daemon: could not find driver bridge
```

A corrupted Docker installation or daemon issue prevents the default bridge driver from being recognized.

### Third-party plugin missing

```
ERROR: plugin "weave" not found
```

A custom network plugin was previously installed but has been removed or is no longer available.

## How to Fix It

### Solution 1: Initialize Docker Swarm for overlay networks

If you need the `overlay` driver, initialize swarm mode first.

```bash
# Initialize swarm (single-node)
docker swarm init

# Verify swarm is active
docker info | grep -i swarm

# Now create the network
docker compose up -d
```

If you do not need swarm features, switch to the `bridge` driver instead:

```yaml
networks:
  default:
    driver: bridge
```

### Solution 2: Switch to a supported driver

Replace the unsupported driver with one that is available on your platform.

```yaml
# BEFORE - overlay requires swarm
networks:
  app-network:
    driver: overlay

# AFTER - bridge works everywhere
networks:
  app-network:
    driver: bridge
```

For Docker Desktop on macOS or Windows, use `bridge` instead of `macvlan`:

```yaml
# BEFORE - macvlan not supported on Docker Desktop
networks:
  app-network:
    driver: macvlan

# AFTER - use bridge with port mapping
networks:
  app-network:
    driver: bridge
services:
  web:
    ports:
      - "8080:80"
```

### Solution 3: Install missing network plugins

If you need a custom or third-party driver, install the required plugin.

```bash
# List available network drivers
docker network ls --driver

# Install a plugin (example)
docker plugin install <plugin-name>

# Verify the plugin is available
docker plugin ls
```

### Solution 4: Verify and restart the Docker daemon

Corrupted daemon state can cause driver resolution failures.

```bash
# Check Docker daemon status
sudo systemctl status docker

# Restart the daemon
sudo systemctl restart docker

# Verify available drivers
docker info | grep -A 10 "Network"

# Test network creation manually
docker network create --driver bridge test-net
docker network rm test-net
```

### Solution 5: Remove driver specification and use defaults

Let Docker choose the appropriate driver automatically.

```yaml
# BEFORE - explicit driver that may not exist
networks:
  app-network:
    driver: overlay
    driver_opts:
      encrypted: "true"

# AFTER - let Docker use defaults
networks:
  app-network:
    name: app-network
```

Docker will use the default `bridge` driver for standalone containers and `overlay` when swarm mode is active.

## Common Scenarios

### Development vs. production network drivers

A compose file works locally but fails in production where the network driver is different.

```yaml
# Works locally with bridge
# Fails in production with overlay requirement
networks:
  backend:
    driver: overlay
```

Fix by using environment-specific override files:

```yaml
# docker-compose.yml (base)
networks:
  backend:

# docker-compose.override.yml (development)
networks:
  backend:
    driver: bridge

# docker-compose.prod.yml (production)
networks:
  backend:
    driver: overlay
```

```bash
# Development
docker compose up -d

# Production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Multi-host networking failures

When deploying across multiple hosts, the bridge driver cannot provide container-to-container communication across hosts. You need `overlay`.

```bash
# Initialize swarm on manager node
docker swarm init --advertise-addr 192.168.1.100

# Join worker nodes
docker swarm join --token <token> 192.168.1.100:2377

# Deploy the stack
docker stack deploy -c docker-compose.yml myapp
```

### Docker Desktop limitations

Docker Desktop on macOS and Windows runs in a VM with limited network driver support. `macvlan` and some `overlay` features are unavailable.

```yaml
# docker-compose.yml - cross-platform compatible
networks:
  default:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
```

Use port mapping for host access instead of `macvlan`-style direct network access.

## Prevent It

- **Test network creation independently**: Before relying on a specific driver, verify it exists with `docker network create --driver <driver> test && docker network rm test`. This confirms the driver is available without touching your compose setup.
- **Use override files for environment differences**: Keep the base compose file driver-agnostic and use override files per environment. This prevents a single driver specification from breaking deployments across different Docker hosts.
- **Document Docker version requirements**: Maintain a `.docker-version` or `README` entry specifying the minimum Docker version and required features. Network driver availability varies significantly between Docker CE, Docker Desktop, and Docker EE.
