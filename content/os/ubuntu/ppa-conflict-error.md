---
title: "PPA Package Conflict Error"
description: "PPA package conflicts with existing system packages"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PPA Package Conflict Error

PPA package conflicts with existing system packages

## Common Causes

- PPA provides newer version conflicting with system packages
- Multiple PPAs providing same package
- PPA package replaces critical system package
- Dependency resolution fails due to PPA

## How to Fix

1. Check PPA packages: `apt-cache policy <package>`
2. Identify conflicting PPAs: `grep -r ^deb /etc/apt/sources.list.d/`
3. Disable conflicting PPA: `sudo add-apt-repository --remove ppa:user/ppa`
4. Use apt pinning to prefer system packages

## Examples

```bash
# Check which PPA provides a package
apt-cache policy nginx

# List all enabled PPAs
grep -r ^deb /etc/apt/sources.list.d/

# Remove problematic PPA
sudo add-apt-repository --remove ppa:user/ppa-name
```
