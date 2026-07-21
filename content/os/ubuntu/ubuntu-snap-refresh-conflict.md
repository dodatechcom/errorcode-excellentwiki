---
title: "Ubuntu Snap Refresh Conflict Error"
description: "Snap package refresh conflicts with running processes or other snaps"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Snap Refresh Conflict Error

Snap package refresh conflicts with running processes or other snaps

## Common Causes

- Snap being refreshed has active services
- Another snap has exclusive lock on resource
- Refresh pending but not applied
- Hold preventing automatic refresh

## How to Fix

1. Check snap refresh: `snap refresh --list`
2. Hold refresh: `snap hold <snap-name>`
3. Refresh manually: `sudo snap refresh <snap-name>`
4. Check active connections: `snap connections <snap-name>`

## Examples

```bash
# Check pending refreshes
snap refresh --list

# Hold snap refresh
sudo snap hold my-snap

# Force refresh
sudo snap refresh my-snap
```
