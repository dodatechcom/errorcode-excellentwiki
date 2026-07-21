---
title: "Ubuntu Suspend/Resume Failure"
description: "System fails to resume from suspend or S3 sleep state"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Suspend/Resume Failure

System fails to resume from suspend or S3 sleep state

## Common Causes

- GPU driver does not support suspend/resume
- USB device preventing suspend
- BIOS ACPI implementation broken
- Kernel module not handling resume properly

## How to Fix

1. Check logs: `journalctl -b | grep -i suspend`
2. Test suspend: `sudo systemctl suspend`
3. Check GPU: `lspci | grep -i vga`
4. Disable problematic modules: add to `/etc/modprobe.d/`

## Examples

```bash
# Test suspend
sudo systemctl suspend

# Check suspend logs
journalctl -b | grep -i 'suspend\|resume'

# List GPU driver
lspci -nn | grep -i vga
```
