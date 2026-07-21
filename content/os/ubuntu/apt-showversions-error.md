---
title: "APT Show-Versions Error"
description: "apt-showversions command fails to parse package status"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# APT Show-Versions Error

apt-showversions command fails to parse package status

## Common Causes

- apt-showversions package not installed
- dpkg status file corrupted
- Multiple architectures causing parsing errors
- APT cache out of sync with dpkg database

## How to Fix

1. Install apt-showversions: `sudo apt-get install apt-showversions`
2. Rebuild dpkg database: `sudo dpkg --configure -a`
3. Sync APT cache: `sudo apt-get update`
4. Check dpkg status: `cat /var/lib/dpkg/status | head -100`

## Examples

```bash
# Install the tool
sudo apt-get install apt-showversions

# Show versions of all packages
apt-showversions
```
