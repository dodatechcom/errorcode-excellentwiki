---
title: "[Solution] Linux: kernel-tainted — Fix kernel tainted warning"
description: "Fix Linux kernel-tainted errors. Warning kernel tainted with non-GPL module loaded."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---

# Fix kernel tainted warning — Fix kernel tainted warning

Warning kernel tainted with non-GPL module loaded. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Non-GPL module loaded
- Proprietary driver
- Unsigned module
- Test code

## How to Fix

### 1. Check Taint
```bash
cat /proc/sys/kernel/tainted
```

### 2. Check Modules
```bash
dmesg | grep -i tainted
lsmod | grep -i proprietary
```

### 3. Unload Module
```bash
sudo modprobe -r <module>
```

### 4. Check Log
```bash
dmesg | grep taint
```

## Common Scenarios

- Kernel tainted
- Non-GPL module loaded
- Proprietary driver

## Prevent It

- Use open source modules
- Check module compatibility
- Monitor taint status
