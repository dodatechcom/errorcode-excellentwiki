---
title: "Kernel SysRq Key Not Working"
description: "Magic SysRq key combinations not functioning on Ubuntu"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Kernel SysRq Key Not Working

Magic SysRq key combinations not functioning on Ubuntu

## Common Causes

- SysRq disabled in kernel config
- /proc/sys/kernel/sysrq set to 0
- Keyboard not sending SysRq signal
- Virtual terminal not receiving key

## How to Fix

1. Check setting: `cat /proc/sys/kernel/sysrq`
2. Enable SysRq: `echo 1 | sudo tee /proc/sys/kernel/sysrq`
3. Make permanent: `echo 'kernel.sysrq=1' | sudo tee /etc/sysctl.d/10-magic-sysrq.conf`
4. Test with: `echo s | sudo tee /proc/sysrq-trigger`

## Examples

```bash
# Check SysRq status
cat /proc/sys/kernel/sysrq

# Enable SysRq
echo 1 | sudo tee /proc/sys/kernel/sysrq

# Emergency sync to disk
echo s | sudo tee /proc/sysrq-trigger
```
