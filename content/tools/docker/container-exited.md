---
title: "[Solution] Docker Container Exited — container exited with code"
description: "Fix Docker container exited error. Diagnose why containers stop and how to restart them."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["container-exited", "exit-code", "stopped", "restart", "docker"]
weight: 5
---

# Docker Container Exited — container exited with code X

A container exits when the main process inside it stops. The exit code indicates the reason: 0 is normal, non-zero means an error occurred.

## Common Causes

- Application inside container crashed or encountered an error
- Container finished its task and exited normally
- Insufficient memory causing OOMKilled (exit code 137)
- Missing or incorrect command/entrypoint

## How to Fix

### Check Container Logs

```bash
docker logs <container-id>
```

### Inspect Exit Code

```bash
docker inspect <container-id> --format='{{.State.ExitCode}}'
```

### Check Container Events

```bash
docker events --filter container=<container-id>
```

### Restart Container

```bash
docker start <container-id>
```

### Run Container Interactively for Debugging

```bash
docker run -it <image> /bin/sh
```

### Common Exit Codes

- `0` — Normal exit
- `1` — Application error
- `126` — Permission problem or not executable
- `127` — Command not found
- `137` — OOMKilled (SIGKILL)
- `139` — Segmentation fault (SIGSEGV)
- `143` — Graceful termination (SIGTERM)

## Examples

```bash
# Example 1: Application error
docker logs my-container
# Error: database connection refused
# Fix: ensure database is running and accessible

# Example 2: OOMKilled
docker inspect my-container --format='{{.State.ExitCode}}'
# 137
# Fix: increase memory limit with --memory flag

# Example 3: Command not found
docker run my-image
# container exited with code 127
# Fix: verify ENTRYPOINT or CMD in Dockerfile
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/pod-crash" >}}) — pod keeps crashing in Kubernetes
- [Health Check Failed]({{< relref "/tools/docker/healthcheck-failed" >}}) — container health check failing
