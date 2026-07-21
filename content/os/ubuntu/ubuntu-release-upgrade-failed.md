---
title: "Ubuntu Release Upgrade Failed"
description: "Ubuntu release upgrade (e.g., 22.04 to 24.04) fails during process"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Release Upgrade Failed

Ubuntu release upgrade (e.g., 22.04 to 24.04) fails during process

## Common Causes

- Package dependency resolution failure during upgrade
- Third-party PPA incompatible with new release
- Insufficient disk space for upgrade
- Kernel packages conflict preventing upgrade

## How to Fix

1. Check free space: `df -h /`
2. Remove third-party PPAs before upgrade
3. Use `do-release-upgrade -d` for development release
4. Check upgrade logs: `cat /var/log/dist-upgrade/main.log`

## Examples

```bash
# Check available disk space
df -h /

# Start release upgrade
sudo do-release-upgrade

# Check upgrade logs
cat /var/log/dist-upgrade/main.log | tail -50
```
