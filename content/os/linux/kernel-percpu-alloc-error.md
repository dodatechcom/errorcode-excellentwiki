---
title: "[Solution] Linux: kernel-percpu-alloc-error -- kernel per-CPU allocator failure"
description: "Fix Linux kernel per-CPU allocator failure. Per-CPU memory allocation failure at boot or runtime."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Per-CPU Allocator Failure

Kernel per-CPU allocation failure occurs when the system cannot allocate per-CPU data areas.

## Common Causes

- Per-CPU area exhaustion due to too many modules
- Low memory preventing pcpu allocation at boot
- Kernel boot parameter limiting per-CPU area size
- NUMA misconfiguration reducing per-CPU memory
- Memory hotplug issues affecting per-CPU regions

## How to Fix

### 1. Check Per-CPU Usage

```bash
cat /proc/meminfo | grep -i "percpu"
ls /sys/devices/system/cpu/
```

### 2. Free Unused Modules

```bash
lsmod | awk '$3 == 0 {print $1}' | while read m; do sudo modprobe -r $m 2>/dev/null; done
sudo depmod -a
```

### 3. Increase Available Memory

```bash
sudo swapoff -a && sudo swapon -a
echo 1 | sudo tee /proc/sys/vm/drop_caches
```

## Examples

```bash
$ cat /proc/meminfo | grep Percpu
Percpu:           262144 kB
$ sudo dmesg | grep pcpu
[  0.000000] pcpu-alloc: 0 262144 [0] 262144 alloc percpu chunk
[  1.234567] pcpu_alloc: percpu allocation failed
```
