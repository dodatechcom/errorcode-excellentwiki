---
title: "APT Pinning Precedence Error"
description: "Error caused by conflicting APT pinning priorities in preferences files"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# APT Pinning Precedence Error

Error caused by conflicting APT pinning priorities in preferences files

## Common Causes

- Multiple pinning files with conflicting priority values
- Incorrect pin priority syntax in /etc/apt/preferences.d/
- Pin-Priority value exceeds maximum of 1000
- Circular dependencies between package pins

## How to Fix

1. Check all pinning files: `ls /etc/apt/preferences.d/`
2. Review pin priorities with `apt-cache policy <package>`
3. Ensure no Pin-Priority exceeds 1000
4. Remove or fix conflicting pin files
5. Run `apt-get update` and test

## Examples

```bash
# Check current pinning priorities
apt-cache policy nginx

# List all pinning files
ls -la /etc/apt/preferences.d/

# Example conflicting pin file
cat /etc/apt/preferences.d/nginx-pin
```
