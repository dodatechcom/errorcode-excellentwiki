---
title: "LXD Profile Configuration Error"
description: "LXD profile cannot be applied to container or contains invalid config"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Profile Configuration Error

LXD profile cannot be applied to container or contains invalid config

## Common Causes

- Profile contains conflicting device definitions
- Profile tries to use non-existent storage pool or network
- Config key not recognized by current LXD version
- Profile device name already used by container

## How to Fix

1. Check profile: `lxc profile show <profile>`
2. List available devices: `lxc storage list` and `lxc network list`
3. Update profile: `lxc profile edit <profile>`
4. Verify config keys: `lxc config --help`

## Examples

```bash
# Show profile configuration
lxc profile show default

# Edit profile
lxc profile edit default

# Apply profile to container
lxc profile apply mycontainer default
```
