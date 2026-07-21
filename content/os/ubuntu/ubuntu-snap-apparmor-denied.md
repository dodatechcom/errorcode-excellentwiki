---
title: "Ubuntu Snap AppArmor Denial"
description: "Snap application denied access by AppArmor profile"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Snap AppArmor Denial

Snap application denied access by AppArmor profile

## Common Causes

- AppArmor profile for snap is overly restrictive
- Snap interface not providing required permissions
- File path not included in AppArmor rules
- Snap trying to access system services without permission

## How to Fix

1. Check AppArmor logs: `sudo journalctl -k | grep apparmor`
2. Check snap connections: `snap connections <snap>`
3. Use devmode for testing: `snap install --devmode <snap>`
4. Report to snap developer for profile update

## Examples

```bash
# Check AppArmor denials
sudo journalctl -k | grep -i 'apparmor.*DENIED'

# Check snap connections
snap connections my-snap

# Install snap in dev mode (less secure)
sudo snap install --devmode my-snap
```
