---
title: "Snap Desktop File Integration Error"
description: "Snap application not appearing in desktop application menu"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Snap Desktop File Integration Error

Snap application not appearing in desktop application menu

## Common Causes

- Desktop file not installed by snap
- Desktop file does not pass validation
- Icon not found or wrong path in desktop file
- Desktop database not updated

## How to Fix

1. Check desktop file: `ls /var/lib/snapd/desktop/applications/`
2. Validate: `desktop-file-validate *.desktop`
3. Update desktop database: `sudo update-desktop-database`
4. Check snap info: `snap info <snap-name> | grep apps`

## Examples

```bash
# List snap desktop files
ls /var/lib/snapd/desktop/applications/

# Update desktop database
sudo update-desktop-database /var/lib/snapd/desktop/applications/

# Check snap apps
snap info my-snap | grep -A5 apps
```
