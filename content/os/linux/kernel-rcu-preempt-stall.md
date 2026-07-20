---
title: "[Solution] Linux: kernel-rcu-preempt-stall — RCU preemption stall detected"
description: "Fix Linux kernel-rcu-preempt-stall errors. RCU preemption stall detected with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["kernel-error"]
weight: 10
---
# Linux: RCU Preempt Stall

An RCU preempt stall occurs when a CPU with preemptible RCU has been in a quiescent state for too long.

## Common Causes

- Tasks running with preemption disabled or in real-time priority loops
- Kernel thread blocking for extended periods with preempt disabled
- Virtual machine CPU overcommit causing vCPU scheduling delays
- Interrupt storm preventing task scheduling

## How to Fix

### 1. Check the Stall Message

```bash
dmesg | grep -i "rcu_preempt\|preempt.*stall" | tail -20
```

### 2. Check for Real-Time Issues

```bash
ps -eo pid,comm,rtprio,policy | grep -E "FIFO|RR"
```

### 3. Disable Preempt RCU Boost

```bash
# Boot with rcupdate.rcu_cpu_stall_suppress=1
# To temporarily suppress stalls
sudo sysctl -w kernel.rcu_cpu_stall_suppress=1
```

## Examples

```bash
$ dmesg | grep -i "rcu_preempt"
[12345.678] INFO: rcu_preempt detected stalls on CPUs/tasks:
[12345.678]  3-...!: (0 ticks this GP) idle=abc/0/0x4000000000000000 softirq=0/0 fqs=0
[12345.678]  Tasks blocked on level-0 rcu_node (CPUs 0-3):
[12345.678]   (detected by 1, t=52502 jiffies, g=-789, q=1234)
```
