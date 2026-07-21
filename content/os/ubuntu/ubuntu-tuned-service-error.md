---
title: "Ubuntu Tuned Performance Service Error"
description: "Tuned service fails to apply performance profiles"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Tuned Performance Service Error

Tuned service fails to apply performance profiles

## Common Causes

- tuned package not installed
- Profile directory missing or corrupted
- System profile not compatible with hardware
- Tuned-adm command failing with errors

## How to Fix

1. Check status: `systemctl status tuned`
2. List profiles: `tuned-adm list`
3. Apply profile: `sudo tuned-adm profile throughput-performance`
4. Check logs: `journalctl -u tuned`

## Examples

```bash
# Check tuned status
systemctl status tuned

# List available profiles
tuned-adm list

# Apply a profile
sudo tuned-adm profile balanced
```
