---
title: "[Solution] Docker TLS Handshake Timeout — TLS handshake timeout"
description: "Fix Docker TLS handshake timeout error. Resolve certificate and connection issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

# TLS handshake timeout

This error occurs when Docker cannot complete the TLS (SSL) handshake with a registry or remote Docker daemon. The secure connection setup fails before completing.

## Common Causes

- Slow or unstable network connection
- Firewall blocking HTTPS traffic
- Proxy server interfering with TLS
- Registry server overloaded
- Incorrect TLS certificate configuration
- Docker daemon TLS configuration issues

## How to Fix

### Check Network to Registry

```bash
curl -v https://registry-1.docker.io/v2/ 2>&1 | head -20
```

### Configure Docker Proxy

```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo tee /etc/systemd/system/docker.service.d/http-proxy.conf <<EOF
[Service]
Environment="HTTP_PROXY=http://proxy:8080"
Environment="HTTPS_PROXY=http://proxy:8080"
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### Disable TLS Verification (Insecure)

```json
{
  "insecure-registries": ["myregistry.com:5000"]
}
```

### Increase Timeouts

```bash
# Check Docker daemon logs
sudo journalctl -u docker.service --no-pager -n 50
```

### Test Registry Connection

```bash
openssl s_client -connect registry-1.docker.io:443
```

## Examples

```bash
# Example 1: Test registry connectivity
curl -v https://registry-1.docker.io/v2/
# TLS handshake timeout
# Fix: check proxy/firewall

# Example 2: Configure proxy
export HTTPS_PROXY=http://proxy:8080
docker pull nginx

# Example 3: Add insecure registry
# Edit /etc/docker/daemon.json
# {"insecure-registries": ["myregistry:5000"]}
sudo systemctl restart docker
```

## Related Errors

- [I/O timeout]({{< relref "/tools/docker/i-o-timeout" >}}) — related error
- [Context canceled]({{< relref "/tools/docker/context-canceled" >}}) — related error
