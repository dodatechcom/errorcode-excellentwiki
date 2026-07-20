---
title: "[Solution] Linux: brk-error — brk/mmap failed"
description: "Fix Linux brk-error errors. brk/mmap failed with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---

# Linux: Brk (Heap) Error

BRK errors occur when the program break (heap) cannot be extended due to memory limits or fragmentation.

## Common Causes

- Process memory limit (ulimit) too low
- System-wide vm.overcommit_memory policy blocking allocation
- Memory fragmentation preventing large allocations
- ASLR (Address Space Layout Randomization) conflicts
- Container or cgroup memory limit hit

## How to Fix

### 1. Check Process Limits

```bash
ulimit -a
cat /proc/<pid>/limits | grep "max memory"
```

### 2. Check Memory Status

```bash
cat /proc/meminfo
free -h
cat /proc/sys/vm/overcommit_memory
```

### 3. Increase Limits

```bash
ulimit -m unlimited
# In systemd service file:
# LimitMEMLOCK=infinity
```

## Examples

```bash
$ ulimit -a | grep memory
max memory size         (kbytes, -m)  unlimited
$ cat /proc/sys/vm/overcommit_memory
2
# Strict overcommit - allocate more swap or set to 1
$ sudo sysctl vm.overcommit_memory=1
```
