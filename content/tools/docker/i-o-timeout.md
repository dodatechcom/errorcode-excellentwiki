---
title: "[Solution] Docker I/O Timeout — i/o timeout"
description: "Fix Docker I/O timeout error. Resolve network and disk timeout issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# i/o timeout

This error occurs when a Docker operation times out waiting for input/output. This can be network I/O (pulling/pushing) or disk I/O (writing layers).

## Common Causes

- Slow network connection to registry
- Disk I/O bottleneck on Docker host
- Registry server slow or overloaded
- Very large image layers
- Network congestion
- DNS resolution taking too long

## How to Fix

### Check Network Speed

```bash
speedtest-cli
ping registry-1.docker.io
```

### Use Faster Registry Mirror

```json
{
  "registry-mirrors": ["https://mirror.gcr.io"]
}
```

### Check Disk I/O

```bash
iostat -x 1 5
```

### Pull with Progress

```bash
docker pull --progress=plain <image>
```

### Increase Docker Daemon Timeouts

```json
{
  "features": {
    "buildkit": true
  },
  "max-concurrent-downloads": 3
}
```

### Check DNS Resolution

```bash
dig registry-1.docker.io
nslookup registry-1.docker.io
```

## Examples

```bash
# Example 1: Network timeout
docker pull nginx:latest
# i/o timeout
# Fix: check network connection

# Example 2: Use mirror
# /etc/docker/daemon.json
{"registry-mirrors": ["https://mirror.gcr.io"]}
sudo systemctl restart docker

# Example 3: Check disk I/O
iostat -x 1 3
# Check %util column for high values
```

## Related Errors

- [TLS handshake timeout]({{< relref "/tools/docker/tls-handshake-timeout" >}}) — related error
- [Context canceled]({{< relref "/tools/docker/context-canceled" >}}) — related error
