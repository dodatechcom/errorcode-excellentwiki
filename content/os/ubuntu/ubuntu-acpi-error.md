---
title: "Ubuntu ACPI Configuration Error"
description: "ACPI (Advanced Configuration and Power Interface) errors during boot"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu ACPI Configuration Error

ACPI (Advanced Configuration and Power Interface) errors during boot

## Common Causes

- BIOS ACPI tables contain errors or unsupported methods
- ACPI driver not handling hardware properly
- acpid service not running
- Custom ACPI scripts in /etc/acpi/ not executing

## How to Fix

1. Check errors: `dmesg | grep -i acpi`
2. Check service: `systemctl status acpid`
3. Test events: `acpi_listen`
4. Check scripts: `ls /etc/acpi/events/`

## Examples

```bash
# Check ACPI errors
dmesg | grep -i acpi | head -20

# Check acpid service
systemctl status acpid

# Listen for ACPI events
acpi_listen
```
