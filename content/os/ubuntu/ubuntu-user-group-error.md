---
title: "Ubuntu User Group Membership Error"
description: "User cannot access resources due to incorrect group membership"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu User Group Membership Error

User cannot access resources due to incorrect group membership

## Common Causes

- User not added to required group
- Group does not exist
- Secondary group not effective until re-login
- File ownership does not match group

## How to Fix

1. Check groups: `groups <username>`
2. Add to group: `sudo usermod -aG <group> <username>`
3. Check group exists: `getent group <group>`
4. Verify file permissions: `ls -la /path/to/file`

## Examples

```bash
# Check user groups
groups admin

# Add user to docker group
sudo usermod -aG docker admin

# Verify group membership
getent group docker
```
