---
title: "[Solution] Linux: kernel-rcu-sched-stall — RCU scheduler stall detected"
description: "Fix Linux kernel-rcu-sched-stall errors. RCU scheduler stall detected with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["kernel-error"]
weight: 10
---
# Linux: RCU Stall Detected

An RCU (Read-Copy-Update) stall occurs when a CPU remains in a quiescent state for too long, preventing RCU grace periods from completing.

## Common Causes

- CPU interrupts disabled for too long
- Real-time kernel preemption mode causing scheduling delays
- Hardware issues preventing interrupt delivery
- KVM or hypervisor not scheduling the vCPU
- Infinite loop in kernel code with preemption disabled

## How to Fix

### 1. Identify the Stalled CPU

```bash
dmesg | grep -i "rcu.*stall\|stall.*rcu" | tail -20
```

### 2. Check for Interrupt Issues

```bash
cat /proc/interrupts | head -20
```

### 3. Adjust RCU Settings

```bash
# Increase RCU stall timeout (ms)
sudo sysctl -w kernel.rcu_cpu_stall_timeout=60
```

### 4. Check Hypervisor (if virtualized)

If running in a VM, ensure the hypervisor is not overcommitting CPUs.

## Examples

```bash
$ dmesg | grep -i "rcu.*stall"
[12345.678] INFO: rcu_sched detected stalls on CPUs/tasks:
[12345.678]  2-...!: (0 ticks this GP) idle=abc/1/0x4000000000000000 softirq=1234/1235 fqs=0
[12345.678]   (detected by 0, t=21002 jiffies, g=-123, q=456)
```
