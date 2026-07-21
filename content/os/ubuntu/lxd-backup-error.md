---
title: "LXD Container Backup Error"
description: "LXD container backup creation or restoration fails"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# LXD Container Backup Error

LXD container backup creation or restoration fails

## Common Causes

- Insufficient disk space for backup file
- Backup format not supported by target LXD version
- Container has running processes causing inconsistent backup
- Database corruption preventing backup metadata

## How to Fix

1. Create backup: `lxc export <container> /path/to/backup.tar.gz`
2. Stop container first: `lxc stop <container>`
3. Restore backup: `lxc import /path/to/backup.tar.gz`
4. Check LXD database: `lxc query /1.0 --request GET`

## Examples

```bash
# Stop container before backup
lxc stop mycontainer

# Create backup
lxc export mycontainer /var/backups/mycontainer.tar.gz

# Restore backup
lxc import /var/backups/mycontainer.tar.gz
```
