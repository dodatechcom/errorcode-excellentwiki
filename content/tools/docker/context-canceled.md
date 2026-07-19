---
title: "[Solution] Docker Context Canceled — context canceled / deadline exceeded"
description: "Fix Docker context canceled error. Resolve timeouts and operation cancellations."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# context canceled / deadline exceeded

This error occurs when a Docker operation is cancelled before it completes. This often happens during long-running operations like pulls, builds, or pushes that exceed timeout limits.

## Common Causes

- Operation took too long and timed out
- User pressed Ctrl+C cancelling the operation
- Network instability causing timeouts
- Very large image pull/push
- Docker daemon overloaded
- Context deadline set too short

## How to Fix

### Increase Timeout

```bash
# For Docker buildkit
DOCKER_BUILDKIT=1 docker build --timeout=3600s .
```

### Check Network Connection

```bash
ping registry-1.docker.io
curl -I https://registry-1.docker.io/v2/
```

### Retry the Operation

```bash
docker pull <image>
# If failed, retry
docker pull <image>
```

### Use Daemon Configuration

```json
{
  "features": {
    "buildkit": true
  }
}
```

### Check Docker Daemon Health

```bash
docker info
sudo systemctl status docker
```

## Examples

```bash
# Example 1: Large image pull
docker pull tensorflow/tensorflow:latest
# context canceled
# Fix: retry or use --quiet flag

# Example 2: Network timeout
docker build .
# deadline exceeded
# Fix: check network connection

# Example 3: Set timeout
DOCKER_BUILDKIT=1 docker build --progress=plain .
```

## Related Errors

- [Docker pull timeout]({{< relref "/tools/docker/docker-pull-timeout" >}}) — related error
- [Docker BuildKit error]({{< relref "/tools/docker/docker-buildkit-error" >}}) — related error
