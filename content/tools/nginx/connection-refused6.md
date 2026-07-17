---
title: "[Solution] Nginx Connection Refused"
description: "Fix Nginx connection refused error. Resolve upstream connection failures and network issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Nginx Connection Refused

A connection refused error means Nginx tried to connect to an upstream server but the OS rejected the connection. The target port is either not listening or blocked by a firewall.

## Common Causes

- The upstream service is not running on the expected port
- A firewall is blocking the connection
- The upstream service is bound to a different interface (e.g., localhost only)
- The port number in the upstream configuration is wrong

## How to Fix

### Check if the Upstream Port is Listening

```bash
ss -tlnp | grep <port>
netstat -tlnp | grep <port>
```

### Verify the Service is Running

```bash
sudo systemctl status <upstream-service>
```

### Check Firewall Rules

```bash
sudo iptables -L -n
sudo ufw status
```

### Confirm Binding Address

```bash
# If service only binds to 127.0.0.1, remote connections are refused
ss -tlnp | grep 8080
# 127.0.0.1:8080  ← only accessible locally
```

### Fix Nginx Upstream Configuration

```nginx
upstream backend {
    server 127.0.0.1:8080;  # must match the actual bind address
}
```

## Examples

```bash
# Service not running
# connect() failed (111: Connection refused)
# Fix: sudo systemctl start my-api

# Service bound to localhost but Nginx connects via external IP
# connect() failed (111: Connection refused)
# Fix: change upstream to 127.0.0.1 or reconfigure the app to bind 0.0.0.0
```

## Related Errors

- [Upstream Timed Out]({{< relref "/tools/nginx/upstream-error" >}}) — connection succeeds but response is slow
- [502 Bad Gateway]({{< relref "/tools/nginx/502-bad-gateway" >}}) — invalid response from upstream
