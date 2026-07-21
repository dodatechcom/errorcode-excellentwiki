---
title: "Systemd Shutdown Hang Error"
description: "System hangs during shutdown waiting for services to stop"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Shutdown Hang Error

System hangs during shutdown waiting for services to stop

## Common Causes

- Service stuck in stopping state with timeout
- Unmount failed for filesystem still in use
- Network filesystem (NFS/CIFS) mount not responding
- Docker containers not stopping gracefully

## How to Fix

1. Check stuck services: `systemctl list-units --state=stopping`
2. Set timeout: `TimeoutStopSec=10s` in service file
3. Force kill: `sudo systemctl kill <service>`
4. Check shutdown logs: `journalctl -b -1 -r -p err`

## Examples

```bash
# Check services stuck stopping
systemctl list-units --state=stopping

# Force stop a stuck service
sudo systemctl kill nginx.service

# Check previous boot shutdown logs
journalctl -b -1 -r | head -50
```
