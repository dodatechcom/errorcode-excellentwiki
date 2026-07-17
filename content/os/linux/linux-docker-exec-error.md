---
title: "[Solution] Docker Exec Error — Fix Container Exec Failures"
description: "Fix docker exec errors on Linux. Resolve 'exec failed', 'container not running', and command execution failures inside containers."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["docker", "exec", "container", "interactive", "shell", "process"]
weight: 5
---

# Docker Exec Error — Fix Container Exec Failures

A Docker exec error occurs when `docker exec` fails to run a command inside a running container. The error reads:

> "Error: No such container: <name>"

Or:

> "exec failed: unable to start container process: exec: \"sh\": executable file not found in $PATH"

## What This Error Means

`docker exec` creates a new process inside an existing running container. It requires the container to be in a running state and the specified command or shell to exist in the container's filesystem. Common failures include the container not running, the shell not being installed, or permission issues.

## Common Causes

- Container is stopped or exited (not running)
- Shell (`sh`, `bash`) not available in minimal containers (Alpine, distroless, scratch)
- Command binary not found in container PATH
- Container PID namespace isolation preventing exec
- User does not have permission to exec as the specified user
- Container has no `/proc` or `/sys` mounted

## How to Fix

### Ensure Container Is Running

```bash
# Check container status
docker ps -a | grep <container>

# Start a stopped container
docker start <container>

# Restart a container
docker restart <container>
```

### Use --interactive and --tty

```bash
# Interactive shell with TTY
docker exec -it <container> sh

# For bash (if installed)
docker exec -it <container> bash

# As a specific user
docker exec -it --user root <container> sh
```

### Install a Shell in Minimal Containers

```dockerfile
# In Dockerfile, add a shell for debugging
FROM alpine:latest
RUN apk add --no-cache bash
CMD ["/bin/bash"]
```

### Use docker run Instead of exec

```bash
# Run a new container with the same image
docker run --rm -it --entrypoint sh <image>

# Or override entrypoint
docker run --rm -it --entrypoint /bin/sh <image>
```

### Check Container Filesystem

```bash
# Inspect container filesystem
docker inspect <container> | grep -i "path"

# List files in container
docker exec <container> ls /bin/

# Check if sh exists
docker exec <container> test -f /bin/sh && echo "sh exists"
```

### Use nsenter for Containers Without Sh

```bash
# Find the container's PID
PID=$(docker inspect --format '{{.State.Pid}}' <container>)

# Use nsenter to enter the container's namespace
sudo nsenter -t $PID -m -u -i -n -p -- /bin/sh
```

## Related Errors

- [Docker Container OOM Killed]({{< relref "/os/linux/linux-docker-out-of-memory" >}}) — Container memory issues
- [Docker Healthcheck Failed]({{< relref "/os/linux/linux-docker-healthcheck" >}}) — Container health check failures
- [Docker Socket Permission Denied]({{< relref "/os/linux/linux-docker-socket-permission" >}}) — Docker daemon access issues
