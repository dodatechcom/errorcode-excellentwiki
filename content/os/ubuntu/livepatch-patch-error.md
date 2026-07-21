---
title: "Canonical Livepatch Patch Application Error"
description: "Livepatch fails to apply kernel security patch without reboot"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Canonical Livepatch Patch Application Error

Livepatch fails to apply kernel security patch without reboot

## Common Causes

- Livepatch client not properly configured
- Kernel version not supported by livepatch
- Token expired or invalid
- Patch conflicts with loaded kernel modules

## How to Fix

1. Check livepatch status: `canonical-livepatch status`
2. Verify token: `canonical-livepatch status --verbose`
3. Check supported kernel: `uname -r` and livepatch compatibility
4. Apply patches: `sudo canonical-livepatch enable <token>`

## Examples

```bash
# Check livepatch status
canonical-livepatch status

# Enable livepatch with token
sudo canonical-livepatch enable <your-token>

# Check if patches applied
canonical-livepatch status --verbose
```
