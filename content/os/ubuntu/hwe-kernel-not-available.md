---
title: "HWE Kernel Package Not Available"
description: "Hardware Enablement kernel package not found for current release"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# HWE Kernel Package Not Available

Hardware Enablement kernel package not found for current release

## Common Causes

- HWE kernel not yet released for this Ubuntu version
- Restricted repository not enabled
- Hardware Enablement stack not installed
- Package name incorrect for architecture

## How to Fix

1. Check available kernels: `apt-cache search linux-generic-hwe`
2. Enable universe repository
3. Install HWE: `sudo apt-get install linux-generic-hwe-$(lsb_release -rs)`
4. Check Ubuntu release: `lsb_release -a`

## Examples

```bash
# Search for HWE kernel packages
apt-cache search linux-generic-hwe

# Install HWE kernel for current release
sudo apt-get install linux-generic-hwe-$(lsb_release -rs)
```
