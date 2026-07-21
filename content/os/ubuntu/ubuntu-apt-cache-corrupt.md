---
title: "Ubuntu APT Package Cache Corrupt"
description: "APT package cache contains corrupted or incomplete files"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu APT Package Cache Corrupt

APT package cache contains corrupted or incomplete files

## Common Causes

- Interrupted download left partial .deb files
- Disk write failure during apt-get update
- Cache directory permissions wrong
- Package index files (InRelease, Packages) corrupted

## How to Fix

1. Clean cache: `sudo apt-get clean`
2. Update package list: `sudo apt-get update`
3. Remove partial files: `sudo rm -rf /var/cache/apt/archives/partial/`
4. Check index: `ls -la /var/lib/apt/lists/`

## Examples

```bash
# Clean APT cache
sudo apt-get clean

# Remove partial downloads
sudo rm -rf /var/lib/apt/lists/partial/

# Update package list
sudo apt-get update
```
