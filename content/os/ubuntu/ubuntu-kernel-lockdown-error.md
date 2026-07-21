---
title: "Ubuntu Kernel Lockdown Mode Error"
description: "Kernel lockdown mode prevents certain administrative operations"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Kernel Lockdown Mode Error

Kernel lockdown mode prevents certain administrative operations

## Common Causes

- Kernel booted in lockdown integrity or confidentiality mode
- Secure Boot triggering kernel lockdown
- Module loading restricted by lockdown policy
- Debugging restricted by lockdown mode

## How to Fix

1. Check lockdown: `cat /sys/kernel/security/lockdown`
2. Disable: add `lockdown=none` to kernel boot params
3. Check Secure Boot: `mokutil --sb-state`
4. Understand: lockdown prevents signing of untrusted modules

## Examples

```bash
# Check lockdown status
cat /sys/kernel/security/lockdown

# Check Secure Boot
mokutil --sb-state

# Disable lockdown (requires boot parameter change)
echo 'GRUB_CMDLINE_LINUX="lockdown=none"' | sudo tee /etc/default/grub.d/lockdown.cfg
sudo update-grub
```
