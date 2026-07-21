---
title: "[Solution] Ubuntu Server: ubuntu-kernel-rcu-stall-error"
description: "Fix Ubuntu ubuntu-kernel-rcu-stall-error. RCU stall detected in kernel."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel RCU Stall Error

RCU stall detected in kernel.

## Common Causes
- CPU stuck in loop with preemption disabled
- Long-running kernel code blocking RCU
- Hardware issue causing CPU hang

## How to Fix
1. Check RCU stall messages
```bash
dmesg | grep -i "rcu.*stall"
```
2. Check CPU usage
```bash
top -bn1 | head -20
mpstat -P ALL 1 3
```
3. Check for softlockup
```bash
dmesg | grep -i "softlockup"
```

## Examples
```bash
$ dmesg | grep -i "rcu.*stall"
[  123.456] rcu: INFO: rcu_preempt detected stalls on CPUs/tasks:
```