---
title: "[Solution] Linux docker build Failed — No Space Left on Device"
description: "Fix Linux 'docker build no space left on device' errors. Free disk space, clean Docker cache, and resolve build failures."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["docker", "build", "no-space", "disk", "image", "layer"]
weight: 5
---

# Linux: docker build — no space left on device

The `no space left on device` error during `docker build` means the host filesystem has run out of disk space. Docker images consist of layers stored on the local filesystem, and the build process creates intermediate layers that consume space even after the final image is created.

## What This Error Means

Docker stores images, containers, and build cache in `/var/lib/docker` by default. During a build, each `RUN` command creates a new layer. Temporary files, package manager caches, and build artifacts within layers all consume disk space. When the filesystem runs dry, the build fails with ENOSPC (no space left on device).

## Common Causes

- Disk filled by Docker images, containers, and build cache
- Build process generates large temporary files (not cleaned up)
- Multiple large images stored locally
- Docker data directory on a small partition
- Log files consuming disk space
- Build context (COPY/ADD) includes unnecessary large files

## How to Fix

### 1. Check Current Disk Usage

```bash
# Check filesystem usage
df -h

# Check Docker-specific usage
docker system df

# Detailed breakdown
docker system df -v
```

### 2. Clean Docker Resources

```bash
# Remove stopped containers
docker container prune -f

# Remove unused images
docker image prune -a -f

# Remove unused volumes
docker volume prune -f

# Remove unused networks
docker network prune -f

# Nuclear option — remove everything unused
docker system prune -a -f --volumes
```

### 3. Clean Build Cache

```bash
# Remove all build cache
docker builder prune -a -f

# Or use buildx
docker buildx prune -a -f
```

### 4. Optimize the Dockerfile

```bash
# Combine RUN commands and clean up in the same layer
# Bad (two layers, cache stays):
# RUN apt-get update
# RUN apt-get install -y gcc

# Good (one layer, cache cleaned):
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Use .dockerignore to exclude unnecessary files
echo -e "node_modules\n.git\n*.log\ntmp/" > .dockerignore
```

### 5. Move Docker Data Directory

```bash
# Stop Docker
sudo systemctl stop docker

# Move data to larger partition
sudo rsync -av /var/lib/docker/ /mnt/larger-disk/docker/

# Configure Docker to use new location
echo '{"data-root": "/mnt/larger-disk/docker"}' | sudo tee /etc/docker/daemon.json

sudo systemctl start docker

# Verify
docker info | grep 'Docker Root Dir'
```

### 6. Clean Non-Docker Files

```bash
# Find large files
sudo du -sh /* | sort -rh | head -10

# Clean journal logs
sudo journalctl --vacuum-size=500M

# Clean package manager cache
sudo apt clean

# Clean log files
sudo find /var/log -name "*.gz" -delete
```

### 7. Use Multi-Stage Builds

```dockerfile
# Stage 1: Build
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# Stage 2: Runtime (much smaller, no build tools)
FROM alpine:3.18
COPY --from=builder /app/myapp /usr/local/bin/
```

## Examples

```bash
$ docker build -t myapp .
Sending build context to Docker daemon  2.048GB
Step 3/10 : RUN apt-get update && apt-get install -y gcc
...
write error: no space left on device

$ docker system df
TYPE            TOTAL   ACTIVE  SIZE      RECLAIMABLE
Images          15      5       12.5GB    8.2GB
Containers      3       2       150MB     100MB
Build Cache     0       0       3.5GB     3.5GB

$ docker system prune -a -f
$ docker builder prune -a -f
$ df -h
Filesystem      Size  Used Avail Use%
/dev/sda1        50G   25G   25G  50%

$ docker build -t myapp .
Successfully built abc123
```

## Related Errors

- [Docker network error]({{< relref "/os/linux/linux-docker-network-error" >}}) — Docker network issues
- [Docker compose network]({{< relref "/os/linux/linux-docker-compose-network" >}}) — Compose network errors
- [Docker build cache]({{< relref "/os/linux/linux-docker-build-cache" >}}) — Build cache issues
