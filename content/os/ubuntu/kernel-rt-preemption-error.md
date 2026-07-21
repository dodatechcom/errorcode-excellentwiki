---
title: "Real-Time Kernel Preemption Error"
description: "PREEMPT_RT kernel fails to maintain real-time guarantees"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Real-Time Kernel Preemption Error

PREEMPT_RT kernel fails to maintain real-time guarantees

## Common Causes

- Non-RT-compatible driver loaded on RT kernel
- Long-held spinlocks preventing preemption
- Interrupt handlers running too long
- Priority inversion in RT tasks

## How to Fix

1. Check RT patch status: `uname -v` should show PREEMPT_RT
2. Identify long latencies: `cyclictest -t1 -p99 -i1000 -l10000`
3. Check for non-RT drivers: `lsmod` and driver documentation
4. Tune kernel parameters for RT performance

## Examples

```bash
# Check if running RT kernel
uname -v | grep PREEMPT_RT

# Run cyclictest to measure latency
sudo cyclictest -t1 -p99 -i1000 -l10000 -m
```
