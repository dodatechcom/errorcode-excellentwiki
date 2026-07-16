---
title: "[Solution] Docker Health Check Failed — health check failed"
description: "Fix Docker health check failed error. Diagnose and resolve container health check failures."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["healthcheck-failed", "health-check", "unhealthy", "probe", "docker"]
weight: 5
---

# Docker Health Check Failed — health check failed

A health check fails when the command specified in the Dockerfile or compose file returns a non-zero exit code or times out. Docker marks the container as unhealthy.

## Common Causes

- Application is not responding to health check requests
- Health check command is incorrect or has wrong path
- Application takes too long to start (timing issue)
- Network connectivity issues within the container

## How to Fix

### Check Container Health Status

```bash
docker inspect --format='{{.State.Health.Status}}' <container>
```

### View Health Check Logs

```bash
docker inspect --format='{{json .State.Health}}' <container> | jq
```

### Test Health Check Command Manually

```bash
docker exec <container> <health-check-command>
```

### Increase Timeout and Retries

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

### Disable Health Check Temporarily

```bash
docker run --no-healthcheck <image>
```

### Check Application Logs

```bash
docker logs <container>
```

## Examples

```bash
# Example 1: Health check failing
docker ps
# CONTAINER STATUS: unhealthy
# Fix: check if application is running inside container

# Example 2: Health check timing out
docker inspect --format='{{json .State.Health}}' my-container
# "Log": [{"Output":"curl: (28) Operation timed out"}]
# Fix: increase --start-period or check application startup

# Example 3: Wrong health check path
HEALTHCHECK CMD curl -f http://localhost:3000/health || exit 1
# Fix: verify correct port and path
```

## Related Errors

- [Container Exited]({{< relref "/tools/docker/container-exited" >}}) — container stopped unexpectedly
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/pod-crash" >}}) — pod keeps crashing in Kubernetes
