---
title: "[Solution] Docker DNS Resolution Failed — DNS resolution failed"
description: "Fix Docker DNS resolution failed error. Configure Docker DNS settings properly."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# DNS resolution failed / could not resolve host

This error occurs when a container cannot resolve domain names to IP addresses. DNS resolution is essential for pulling images, accessing APIs, and general network connectivity.

## Common Causes

- Docker DNS configuration issue
- Host DNS settings not inherited by container
- DNS server unreachable from container network
- Docker network misconfiguration
- /etc/resolv.conf not properly configured in container

## How to Fix

### Check DNS in Container

```bash
docker run --rm alpine nslookup google.com
```

### Configure Docker DNS

```bash
# /etc/docker/daemon.json
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}
```

### Use Host DNS

```bash
docker run --dns=host my-image
```

### Specify DNS at Runtime

```bash
docker run --dns 8.8.8.8 --dns 8.8.4.4 my-image
```

### Check Container DNS Config

```bash
docker run --rm alpine cat /etc/resolv.conf
```

### Test DNS Resolution

```bash
docker run --rm alpine ping google.com
```

## Examples

```bash
# Example 1: Check DNS in container
docker run --rm alpine cat /etc/resolv.conf
# nameserver 8.8.8.8

# Example 2: Set DNS
docker run --dns 8.8.8.8 my-app
# Now can resolve domains

# Example 3: Use host DNS
docker run --dns=host my-app
```

## Related Errors

- [Network not found]({{< relref "/tools/docker/network-not-found" >}}) — related error
- [Docker network error]({{< relref "/tools/docker/docker-network-error" >}}) — related error
