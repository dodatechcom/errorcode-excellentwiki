---
title: "[Solution] Linux docker compose Volume Mount Error"
description: "Fix Linux 'docker compose' volume mount errors. Resolve bind mount failures, permission issues, and volume configuration problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["docker", "docker-compose", "volume", "mount", "bind-mount", "permission"]
weight: 5
---

# Linux: docker compose — volume mount error

The `docker compose` volume mount error such as `Bind mount failed`, `invalid mount config`, or `error while creating mount source path` means Docker Compose could not create or attach a volume/bind mount to a container. This often involves path issues, permissions, or Docker Desktop filesystem limitations.

## What This Error Means

Docker Compose supports two types of volumes: named volumes (Docker-managed) and bind mounts (host directory mapped into the container). Bind mounts require the source path to exist on the host and the Docker daemon to have permission to access it. Named volumes are created by Docker and stored in `/var/lib/docker/volumes/`. Errors occur when paths are wrong, permissions block access, or the host OS cannot support the mount type.

## Common Causes

- Bind mount source path does not exist on host
- Incorrect path syntax (relative vs absolute, missing colon)
- SELinux or AppArmor blocking bind mount access
- Windows/macOS Docker Desktop path mapping issues
- Docker daemon cannot access the directory (permissions)
- Named volume already exists with different configuration
- NFS/CIFS remote filesystem mount issues

## How to Fix

### 1. Verify Source Path Exists

```bash
# Check the host path
ls -la /path/on/host

# Create it if missing
sudo mkdir -p /path/on/host
sudo chmod 755 /path/on/host
```

### 2. Fix Volume Syntax

```yaml
# docker-compose.yml — correct syntax

# Named volume (Docker-managed)
services:
  app:
    volumes:
      - app-data:/app/data

# Bind mount (absolute path required)
services:
  app:
    volumes:
      - /home/user/app/config:/app/config:ro
      - ./src:/app/src

# Named volume definition
volumes:
  app-data:
    driver: local
```

### 3. Fix SELinux Context (RHEL/CentOS/Fedora)

```bash
# Add :z to share the volume between containers
volumes:
  - /path/on/host:/app/data:z

# Add :Z for private unshared label
volumes:
  - /path/on/host:/app/data:Z

# Or disable SELinux for the mount (not recommended for production)
sudo setsebool -P container_manage_cgroup on
```

### 4. Fix Ownership and Permissions

```bash
# Check directory ownership
ls -la /path/on/host

# Fix ownership for the container user
sudo chown -R 1000:1000 /path/on/host

# If using a specific UID in Dockerfile
# USER 1000:1000
# Ensure the host directory is accessible by UID 1000
```

### 5. Fix Named Volume Conflicts

```bash
# List existing volumes
docker volume ls

# Remove orphaned volumes
docker volume prune -f

# Remove specific volume
docker volume rm <volume-name>

# Recreate with compose
docker compose down -v    # -v removes named volumes
docker compose up -d
```

### 6. Fix Relative Path Issues

```bash
# Always use absolute paths or verify relative path
# ./src means relative to docker-compose.yml location

# Debug: check what Docker sees
docker compose config

# This shows the resolved paths
```

### 7. Fix Docker Desktop Issues (macOS/Windows)

```bash
# In Docker Desktop settings:
# Resources -> File Sharing: ensure the path is listed

# For Docker Desktop, bind mounts go through a VM layer
# Performance may be slow for large directories

# Use named volumes instead for better performance
volumes:
  - app-cache:/app/cache

volumes:
  app-cache:
```

## Examples

```bash
$ docker compose up -d
[+] Running 0/1
 ✘ Container myapp  Bind mount failed: '/home/user/config' does not exist

$ ls /home/user/config
ls: cannot access '/home/user/config': No such file or directory

$ mkdir -p /home/user/config
$ docker compose up -d
[+] Running 2/2
 ✔ Network myproject_default  Created
 ✔ Container myapp            Started
```

```yaml
# Before (broken):
services:
  app:
    volumes:
      - config:/app/config    # Named volume, not bind mount

# After (fixed):
services:
  app:
    volumes:
      - /home/user/config:/app/config:ro  # Explicit bind mount
```

## Related Errors

- [Docker compose network]({{< relref "/os/linux/linux-docker-compose-network" >}}) — Network creation errors
- [Docker permission denied]({{< relref "/os/linux/linux-docker-permission-root" >}}) — Docker permission issues
- [Docker compose error]({{< relref "/os/linux/linux-docker-compose-error" >}}) — General compose errors
