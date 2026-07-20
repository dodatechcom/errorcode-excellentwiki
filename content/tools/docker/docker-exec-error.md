---
title: "[Solution] Docker Exec Error — exec failed"
description: "Fix Docker exec failed error. Run commands inside running containers and debug exec failures."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "exec", "containers", "debugging"]
severity: "error"
weight: 6
---

# ERROR: exec failed

## Error Message

```
Error: exec failed: unable to start container process: exec: "mycommand": executable file not found in $PATH
```

This error occurs when `docker exec` fails to run a command inside a container. The command may not exist, the container may have stopped, or permissions may prevent execution.

## Common Causes

- The command or binary does not exist inside the container
- The container is not running or was stopped between the `docker ps` and `docker exec` calls
- The user specified with `-u` does not have permission to run the command
- The container is a minimal image (like `alpine` or `scratch`) that lacks common shells and utilities
- The container's filesystem is in a read-only or corrupted state

## Solutions

### Solution 1: Verify the Command Exists

Check what binaries are available inside the container before trying to exec into it. Use `which` or list the `/bin` and `/usr/bin` directories.

```bash
docker exec myapp which python3
docker exec myapp ls /usr/bin/
```

### Solution 2: Use sh Instead of bash

Minimal images like Alpine do not include bash. Replace bash with sh for compatibility with lightweight containers.

```bash
docker exec -it myapp sh
```

### Solution 3: Run as the Correct User

Some containers run as non-root users that lack access to certain binaries. Switch to root to run system-level commands.

```bash
docker exec -u root myapp apt-get update
docker exec -u 0 myapp cat /etc/shadow
```

### Solution 4: Install Missing Dependencies

If the command is part of a development toolchain, install it inside the running container. Note that changes are lost unless you commit the container to an image.

```bash
docker exec myapp apk add --no-cache curl
docker exec myapp curl -s http://localhost:8080/health
```

## Prevention Tips

- Use the official Docker image variants with the tools you need pre-installed
- Build a custom image with required debugging tools for production troubleshooting
- Keep a separate debug sidecar container for tools that are not in the main image
- Test exec commands in your CI pipeline to catch missing binaries early

## Related Errors

- [Container Not Running]({{< relref "/tools/docker/container-is-not-running" >}}) — container must be running for exec
- [Docker Socket Permission]({{< relref "/tools/docker/docker-socket-permission" >}}) — permission denied on docker.sock
