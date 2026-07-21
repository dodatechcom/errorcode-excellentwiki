---
title: "Ubuntu HWE Kernel Support End Error"
description: "Hardware Enablement kernel no longer receives updates for current release"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu HWE Kernel Support End Error

Hardware Enablement kernel no longer receives updates for current release

## Common Causes

- HWE kernel reached end of life for current Ubuntu version
- Security patches no longer available for HWE kernel
- Need to upgrade to next HWE stack
- System using deprecated kernel branch

## How to Fix

1. Check HWE status: `apt-cache policy linux-generic-hwe-$(lsb_release -rs)`
2. Upgrade to new HWE: `sudo apt-get install linux-generic-hwe-$(lsb_release -rs)`
3. Check support dates: Ubuntu release cycle documentation
4. Consider upgrading to next LTS if HWE not available

## Examples

```bash
# Check current kernel
uname -r

# Check HWE package availability
apt-cache search linux-generic-hwe

# Upgrade to latest HWE
sudo apt-get update && sudo apt-get install linux-generic-hwe-$(lsb_release -rs)
```
