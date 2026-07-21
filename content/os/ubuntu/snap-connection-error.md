---
title: "Snap Connection Interface Error"
description: "Snap package cannot connect to required interface"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Snap Connection Interface Error

Snap package cannot connect to required interface

## Common Causes

- Plug/slot interface not declared in snap
- Manual connection required but not established
- Interface not supported on system
- Conflicting interface connections

## How to Fix

1. Check snap connections: `snap connections <snap-name>`
2. Connect manually: `sudo snap connect <snap>:<plug> <slot>`
3. List available interfaces: `snap interfaces`
4. Review snap documentation for required interfaces

## Examples

```bash
# Check snap connections
snap connections nextcloud

# Manually connect interface
sudo snap connect nextcloud:removable-media :removable-media

# List all interfaces
snap interfaces
```
