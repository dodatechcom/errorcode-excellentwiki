---
title: "[Solution] Linux: kernel-rcu-preempt-stall-v2 -- RCU preempt stall isolated CPU"
description: "Fix Linux kernel RCU preempt stall errors. RCU stall on CPU isolated with isolcpus parameter."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel RCU Preempt Stall (Isolated CPU)

RCU preempt stall on an isolated CPU occurs when isolcpus prevents quiescent state reporting.

## Common Causes

- CPU isolation via isolcpus preventing RCU callback
- Real-time kernel patches conflicting with RCU
- Long-running kernel path without context switch
- IRQ affinity pinning RCU callbacks to isolated CPU
- Hypervisor delaying vCPU scheduling

## How to Fix

### 1. Check CPU Isolation

```bash
cat /proc/cmdline | tr ' ' '\\n' | grep -E "isolcpus|nohz_full"
cat /sys/devices/system/cpu/isolated
```

### 2. Adjust RCU Configuration

```bash
sudo sysctl kernel.rcu_cpu_stall_timeout=30
echo 0 | sudo tee /sys/module/rcutree/parameters/jiffies_till_first_fqs
```

### 3. Review IRQ Affinity

```bash
cat /proc/interrupts | head -5
cat /proc/irq/<irq_num>/smp_affinity_list
```

## Examples

```bash
$ cat /sys/devices/system/cpu/isolated
2-3
$ sudo dmesg | grep -i "rcu.*stall"
[7777.222] rcu: INFO: rcu_preempt detected stalls on CPUs/tasks:
[7777.223] rcu: 2-!: (1 GPs behind) idle=c03/1 softirq=445/446
```
