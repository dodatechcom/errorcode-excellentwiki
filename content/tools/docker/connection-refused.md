---
title: "[Solution] Docker Connection Refused — connection refused"
description: "Fix Docker connection refused error. Resolve network and service connection issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# connection refused

This error occurs when a container or the Docker daemon refuses a network connection. The target service is not listening on the expected port or address.

## Common Causes

- Service inside container not running
- Wrong port number
- Service listening on localhost instead of 0.0.0.0
- Container not exposed ports correctly
- Firewall blocking connections
- Docker daemon not accepting connections

## How to Fix

### Check Container Ports

```bash
docker ps
# Look at PORTS column
```

### Check Service Inside Container

```bash
docker exec <container> netstat -tlnp
```

### Verify Container Is Running

```bash
docker ps -a --filter name=<container>
```

### Check Port Mapping

```bash
docker port <container>
```

### Test Connection from Host

```bash
curl http://localhost:8080
```

### Verify Service Binds to 0.0.0.0

```bash
docker exec <container> netstat -tlnp
# Should show 0.0.0.0:80 not 127.0.0.1:80
```

## Examples

```bash
# Example 1: Check if container is running
docker ps
# If empty, container stopped

# Example 2: Check service binding
docker exec my-container netstat -tlnp
# tcp 0.0.0.0:8080 -- service bound correctly

# Example 3: Test connection
curl http://localhost:8080
# If connection refused, check container logs
docker logs my-container
```

## Related Errors

- [Container is not running]({{< relref "/tools/docker/container-is-not-running" >}}) — related error
- [Port already allocated]({{< relref "/tools/docker/port-already-allocated" >}}) — related error
