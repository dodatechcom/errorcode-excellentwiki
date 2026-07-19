---
title: "[Solution] Docker Container Removal Stuck — container removal stuck in Removing state"
description: "Fix Docker container stuck in removing state. Force clean stuck containers."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

# container is in use / removal operation in progress

This error occurs when a container gets stuck in the "Removal" state and cannot be fully removed. Docker waits for resources to be released but they remain locked.

## Common Causes

- Container has active network connections
- Volume mount still in use by another process
- Docker daemon busy with other operations
- Container process holding file locks
- Overlay filesystem mount cannot be unmounted

## How to Fix

### Force Remove

```bash
docker rm -f <container>
```

### Stop Docker and Remove

```bash
sudo systemctl stop docker
sudo rm -rf /var/lib/docker/containers/<container-id>
sudo systemctl start docker
```

### Kill Container Process

```bash
# Find container PID
docker inspect <container> --format '{{.State.Pid}}'
# Kill it
sudo kill -9 <PID>
docker rm <container>
```

### Remove with Timeout

```bash
docker rm -t 0 <container>
```

### Prune All Containers

```bash
docker container prune -f
```

### Check for Stuck Mounts

```bash
mount | grep docker
```

## Examples

```bash
# Example 1: Force remove stuck container
docker rm -f stuck-container

# Example 2: Stop Docker and clean
sudo systemctl stop docker
sudo rm -rf /var/lib/docker/containers/stuck-container-id
sudo systemctl start docker

# Example 3: Kill process
docker inspect stuck-container --format '{{.State.Pid}}'
# 12345
sudo kill -9 12345
docker rm stuck-container
```

## Related Errors

- [Container removal failed]({{< relref "/tools/docker/container-removal-failed" >}}) — related error
- [Unable to remove filesystem]({{< relref "/tools/docker/unable-to-remove-filesystem" >}}) — related error
