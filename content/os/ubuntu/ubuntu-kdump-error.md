---
title: "Ubuntu Kdump Crash Dump Error"
description: "Kdump fails to capture memory dump after kernel crash"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Kdump Crash Dump Error

Kdump fails to capture memory dump after kernel crash

## Common Causes

- Kdump reserved memory too small
- Kdump service not running
- vmcore not saved to expected location
- Second kernel (capture kernel) failed to boot

## How to Fix

1. Check kdump: `systemctl status kdump`
2. View reserved memory: `cat /proc/cmdline | grep crashkernel`
3. Test: `echo c > /proc/sysrq-trigger` (dangerous - triggers crash)
4. Check logs: `journalctl -u kdump`

## Examples

```bash
# Check kdump status
systemctl status kdump

# Check crashkernel reservation
cat /proc/cmdline | grep -o 'crashkernel=[^ ]*'

# View kdump logs
journalctl -u kdump -n 50
```
