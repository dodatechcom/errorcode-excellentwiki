---
title: "[Solution] Docker Address Already in Use — bind: address already in use"
description: "Fix Docker address already in use error. Resolve port binding conflicts."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# bind: address already in use

This error occurs when Docker cannot bind to the specified host address and port because it is already in use. This is similar to port already allocated but specifically refers to address binding.

## Common Causes

- Another container or service is bound to the address:port
- Previous container did not release the port
- Port left in TIME_WAIT state
- Multiple containers trying to bind the same host port

## How to Fix

### Find What Is Using the Address

```bash
sudo ss -tlnp | grep :8080
```

### List All Docker Port Bindings

```bash
docker ps --format "{{.Names}}: {{.Ports}}"
```

### Stop Conflicting Container

```bash
docker stop <container>
```

### Use Different Host Port

```bash
docker run -p 9090:80 nginx
```

### Restart Docker Daemon

```bash
sudo systemctl restart docker
```

### Check for TIME_WAIT Ports

```bash
sudo ss -tan | grep TIME_WAIT | grep :8080
```

## Examples

```bash
# Example 1: Check all bound ports
docker ps --format "{{.Names}}: {{.Ports}}"
# web: 0.0.0.0:8080->80/tcp
# api: 0.0.0.0:3000->3000/tcp

# Example 2: Use dynamic ports
docker run -P nginx
docker ps
# 0.0.0.0:49153->80/tcp

# Example 3: Stop all containers
docker stop $(docker ps -q)
```

## Related Errors

- [Port already allocated]({{< relref "/tools/docker/port-already-allocated" >}}) — related error
- [Port conflict]({{< relref "/tools/docker/port-conflict" >}}) — related error
