---
title: "Ubuntu Core Dump Configuration Error"
description: "Core dumps not being captured or saved to expected location"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Core Dump Configuration Error

Core dumps not being captured or saved to expected location

## Common Causes

- Core pattern not configured correctly
- Core dump size limit exceeded
- Storage location not writable
- systemd-coredump not installed

## How to Fix

1. Check pattern: `cat /proc/sys/kernel/core_pattern`
2. Check limit: `ulimit -c`
3. View dumps: `coredumpctl list`
4. Configure: `sysctl -w kernel.core_pattern=core.%e.%p.%t`

## Examples

```bash
# Check core dump pattern
cat /proc/sys/kernel/core_pattern

# Check core dump size limit
ulimit -c

# View captured core dumps
coredumpctl list
```
