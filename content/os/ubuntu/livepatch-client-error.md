---
title: "Livepatch Client Service Error"
description: "canonical-livepatch client service fails to start or communicate"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Livepatch Client Service Error

canonical-livepatch client service fails to start or communicate

## Common Causes

- Service not installed: `snap list canonical-livepatch`
- Snapd service not running
- Network connectivity to Livepatch servers blocked
- Snap refresh interfering with livepatch

## How to Fix

1. Check service: `systemctl status snap.canonical-livepatch.canonical-livepatchd.service`
2. Restart service: `sudo snap restart canonical-livepatch`
3. Check snapd: `systemctl status snapd`
4. Verify network: `curl -I https://livepatch.canonical.com`

## Examples

```bash
# Check livepatch service
systemctl status snap.canonical-livepatch.canonical-livepatchd.service

# Restart livepatch
sudo snap restart canonical-livepatch

# Check snap status
snap list canonical-livepatch
```
