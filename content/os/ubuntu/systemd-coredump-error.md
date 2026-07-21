---
title: "Systemd Coredump Error"
description: "Systemd-coredump fails to capture or process core dumps"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Coredump Error

Systemd-coredump fails to capture or process core dumps

## Common Causes

- Core dump size exceeds configured limit
- Storage directory /var/lib/systemd/coredump full
- Process has CAP_DUMPABLE capability dropped
- kernel.core_pattern not set correctly

## How to Fix

1. Check core dump limits: `ulimit -c`
2. Review coredump configuration: `cat /etc/systemd/coredump.conf`
3. List existing dumps: `coredumpctl list`
4. Clean old dumps: `sudo coredumpctl gc`

## Examples

```bash
# List captured core dumps
coredumpctl list

# Show details of specific dump
coredumpctl info <PID>

# Clean old dumps
sudo coredumpctl gc
```
