---
title: "[Solution] Docker Cannot Connect to Docker Daemon — Is the Docker daemon running?"
description: "Fix Docker cannot connect to daemon error. Start Docker daemon and resolve connection issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

# Cannot connect to the Docker daemon. Is the docker daemon running?

This error means the Docker CLI cannot reach the Docker daemon. The daemon process is either not running, not configured, or inaccessible.

## Common Causes

- Docker daemon service is stopped or crashed
- Docker socket file missing or has wrong permissions
- Incorrect DOCKER_HOST environment variable
- Docker Desktop not started (macOS/Windows)
- Systemd service failure on Linux

## How to Fix

### Start Docker Service (Linux)

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Check Docker Service Status

```bash
sudo systemctl status docker
```

### Start Docker Desktop (macOS/Windows)

Open Docker Desktop from your applications menu and wait for it to fully start.

### Check Docker Daemon Logs

```bash
sudo journalctl -u docker.service --no-pager -n 50
```

### Verify Docker Socket Exists

```bash
ls -la /var/run/docker.sock
```

### Restart Docker Daemon

```bash
sudo systemctl restart docker
```

### Check DOCKER_HOST Environment

```bash
echo $DOCKER_HOST
# Should be: unix:///var/run/docker.sock (Linux)
# or: unix:///Users/<user>/.docker/run/docker.sock (macOS)
```

## Examples

```bash
# Example 1: Daemon not running
Cannot connect to the Docker daemon. Is the docker daemon running?
# Fix: sudo systemctl start docker

# Example 2: Permission issue
Cannot connect to the Docker daemon at unix:///var/run/docker.sock
# Fix: sudo usermod -aG docker $USER && newgrp docker

# Example 3: Docker Desktop not started
Cannot connect to the Docker daemon at unix:///var/run/docker.sock
# Fix: Open Docker Desktop application and wait for it to start
```

## Related Errors

- [Socket permission denied]({{< relref "/tools/docker/docker-socket-permission" >}}) — related error
- [Docker socket configuration]({{< relref "/tools/docker/docker-socket" >}}) — related error
