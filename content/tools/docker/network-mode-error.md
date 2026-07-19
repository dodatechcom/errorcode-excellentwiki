---
title: "[Solution] Docker Network Mode Error — network mode invalid"
description: "Fix Docker network mode error. Configure host, bridge, and none network modes correctly."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

# network mode is invalid

This error occurs when an invalid or unsupported network mode is specified for a Docker container.

## Common Causes

- Invalid network mode string
- Referencing a network mode that does not exist
- Mixing network mode flags incorrectly
- Using deprecated network mode syntax

## How to Fix

### Use Valid Network Modes

```bash
# Host mode - shares host network stack
docker run --network host nginx

# Bridge mode (default) - isolated network
docker run --network bridge nginx

# None - no networking
docker run --network none nginx

# Container - share another container's network
docker run --network container:<other-container> nginx

# Custom network
docker run --network my-custom-network nginx
```

### Verify Network Exists

```bash
docker network ls
```

### Check Current Container Network

```bash
docker inspect <container> --format '{{.HostConfig.NetworkMode}}'
```

## Examples

```bash
# Example 1: Host mode
docker run --network host nginx

# Example 2: Custom network
docker network create my-net
docker run --network my-net nginx

# Example 3: Check container network mode
docker inspect my-container --format '{{.HostConfig.NetworkMode}}'
```

## Related Errors

- [Network not found]({{< relref "/tools/docker/network-not-found" >}}) — related error
- [Docker network error]({{< relref "/tools/docker/docker-network-error" >}}) — related error
