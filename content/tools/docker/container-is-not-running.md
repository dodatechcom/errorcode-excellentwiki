---
title: "[Solution] Docker Container Is Not Running — container is not running"
description: "Fix Docker container not running error. Start stopped containers and diagnose why they stopped."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# Error response from daemon: Container <id> is not running

This error occurs when you try to execute a command on a container that has stopped. Docker commands like `docker exec` require a running container.

## Common Causes

- Container crashed due to application error
- Container exited normally after completing its task
- Container was manually stopped
- OOMKilled due to memory limits
- Entrypoint/CMD exited

## How to Fix

### Check Container Status

```bash
docker ps -a
```

### Start the Container

```bash
docker start <container>
```

### Check Why It Stopped

```bash
docker logs <container>
docker inspect <container> --format '{{.State.ExitCode}}'
```

### Restart the Container

```bash
docker restart <container>
```

### Run with Restart Policy

```bash
docker run --restart unless-stopped my-image
```

### Run Interactively to Debug

```bash
docker run -it my-image /bin/sh
```

## Examples

```bash
# Example 1: Container stopped
docker exec my-container ls
# Error: container is not running
docker start my-container
docker exec my-container ls

# Example 2: Check exit code
docker inspect my-container --format '{{.State.ExitCode}}'
# 137 = OOMKilled

# Example 3: Auto-restart
docker run -d --restart unless-stopped nginx
```

## Related Errors

- [Container exited with code]({{< relref "/tools/docker/container-exited" >}}) — related error
- [Health check failed]({{< relref "/tools/docker/docker-healthcheck-fail" >}}) — related error
