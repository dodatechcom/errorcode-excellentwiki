---
title: "Docker Volume Permission Denied Error"
description: "Container cannot read or write to mounted volume due to permissions"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Volume Permission Denied Error

Container cannot read or write to mounted volume due to permissions

## Common Causes

- Container user UID/GID does not match host directory owner
- SELinux or AppArmor blocking volume access
- Volume mounted as read-only but container needs write
- Directory permissions too restrictive (e.g., 700)

## How to Fix

1. Check host directory permissions: `ls -la /path/to/volume`
2. Match container user with host: `--user $(id -u):$(id -g)`
3. Fix permissions: `chmod -R 777 /path/to/volume`
4. Check AppArmor: `sudo aa-status | grep docker`

## Examples

```bash
# Check volume permissions
ls -la /opt/myapp/data

# Run container with specific user
docker run -v /opt/myapp/data:/data --user 1000:1000 myimage

# Fix permissions
sudo chown -R 1000:1000 /opt/myapp/data
```
