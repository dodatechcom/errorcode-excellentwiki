---
title: "LXD Proxy Device Error"
description: "LXD proxy device fails to forward traffic between host and container"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Proxy Device Error

LXD proxy device fails to forward traffic between host and container

## Common Causes

- Proxy listen address already in use on host
- Target container port not listening
- Protocol mismatch (TCP vs UDP)
- Firewall blocking proxy traffic

## How to Fix

1. Check proxy status: `lxc config show <container> | grep proxy`
2. Test target port: `lxc exec <container> -- ss -tlnp | grep <port>`
3. Verify listen address: `sudo ss -tlnp | grep <host-port>`
4. Check firewall: `sudo ufw status`

## Examples

```bash
# Add proxy device
lxc config device add mycontainer myproxy proxy listen=tcp:0.0.0.0:8080 connect=tcp:127.0.0.1:80

# Check proxy device
lxc config show mycontainer

# Remove proxy device
lxc config device remove mycontainer myproxy
```
