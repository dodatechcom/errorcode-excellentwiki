---
title: "Ubuntu Chrony NTP Client Error"
description: "Chrony time synchronization fails to maintain accurate time"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Chrony NTP Client Error

Chrony time synchronization fails to maintain accurate time

## Common Causes

- Chrony service not running
- NTP servers unreachable
- Drift file corrupted
- System clock too far offset from NTP sources

## How to Fix

1. Check status: `systemctl status chrony`
2. Check sources: `chronyc sources -v`
3. Force sync: `sudo chronyc makestep`
4. Check drift: `chronyc tracking`

## Examples

```bash
# Check chrony status
systemctl status chrony

# Check NTP sources
chronyc sources -v

# Force time correction
sudo chronyc makestep
```
