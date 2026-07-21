---
title: "Systemd-Resolved Stub Listener Error"
description: "Stub DNS listener on 127.0.0.53 fails or conflicts"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd-Resolved Stub Listener Error

Stub DNS listener on 127.0.0.53 fails or conflicts

## Common Causes

- Another DNS resolver already listening on 127.0.0.53:53
- systemd-resolved service failed to start
- /etc/resolv.conf not properly symlinked to systemd-resolved
- Port 53 occupied by dnsmasq or other DNS server

## How to Fix

1. Check systemd-resolved status: `systemctl status systemd-resolved`
2. Verify resolv.conf symlink: `ls -la /etc/resolv.conf`
3. Check for port conflicts: `sudo ss -tlnp | grep :53`
4. Restart resolved: `sudo systemctl restart systemd-resolved`

## Examples

```bash
# Check resolved status
systemctl status systemd-resolved

# Verify DNS configuration
resolvectl status

# Fix resolv.conf symlink
sudo ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf
```
