---
title: "[Solution] Docker Pull Timeout — Fix Image Pull Failures"
description: "Fix Docker image pull timeout errors on Linux. Resolve registry connection timeouts, slow pulls, and network issues when pulling images."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["docker", "pull", "timeout", "registry", "network", "image"]
weight: 5
---

# Docker Pull Timeout — Fix Image Pull Failures

A Docker pull timeout occurs when `docker pull` cannot download an image from the registry within the default timeout period. The error reads:

> "Error response from daemon: Get "https://registry-1.docker.io/v2/": dial tcp: lookup registry-1.docker.io: no such host"

Or:

> "context deadline exceeded"

## What This Error Means

Docker pulls images from registries (Docker Hub, GHCR, ECR, etc.) over HTTPS. The pull operation requires DNS resolution, TCP connection, TLS handshake, and then data transfer. A timeout can occur at any of these stages. The most common cause is DNS resolution failure or network connectivity issues to the registry.

## Common Causes

- DNS resolution failure for the registry domain
- Network firewall blocking outbound HTTPS (port 443)
- Slow internet connection or bandwidth saturation
- Registry rate limiting (Docker Hub anonymous pulls limited to 100/6hr)
- DNS over HTTPS (DoH) configuration issues
- VPN or proxy interfering with registry connections

## How to Fix

### Configure a Mirror Registry

```json
// /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://mirror.gcr.io",
    "https://docker.m.daocloud.io"
  ]
}
```

```bash
sudo systemctl restart docker
```

### Configure DNS

```bash
# Add reliable DNS servers
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "nameserver 8.8.4.4" | sudo tee -a /etc/resolv.conf

# Or use systemd-resolved
sudo systemctl restart systemd-resolved
```

### Increase Timeout

```bash
# Pull with explicit timeout (Docker 24+)
docker pull --timeout 300s myimage:latest

# Or set daemon-level timeout
# /etc/docker/daemon.json
{
  "default-timeout-seconds": 300
}
```

### Authenticate to Reduce Rate Limits

```bash
# Login to Docker Hub (higher rate limits)
docker login

# Use authenticated pulls
docker pull --authfile ~/.docker/config.json myimage:latest
```

### Check Network Connectivity

```bash
# Test DNS resolution
nslookup registry-1.docker.io

# Test HTTPS connectivity
curl -v https://registry-1.docker.io/v2/

# Check firewall rules
sudo iptables -L -n | grep -E "443|HTTPS"
```

### Use a Local Proxy

```bash
# Configure Docker to use HTTP proxy
# /etc/systemd/system/docker.service.d/http-proxy.conf
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:8080"
Environment="HTTPS_PROXY=http://proxy.example.com:8080"

sudo systemctl daemon-reload
sudo systemctl restart docker
```

## Related Errors

- [Docker Image Not Found]({{< relref "/os/linux/linux-docker-image-not-found" >}}) — Image does not exist in registry
- [Docker Network Bridge Error]({{< relref "/os/linux/linux-docker-network-error" >}}) — Network bridge issues
- [Docker Container OOM Killed]({{< relref "/os/linux/linux-docker-out-of-memory" >}}) — Container memory issues
