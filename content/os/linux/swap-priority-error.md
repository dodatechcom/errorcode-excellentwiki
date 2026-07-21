---
title: "[Solution] Linux: swap-priority-error -- swap priority conflict"
description: "Fix Linux swap priority errors. Swap priority conflict between multiple devices."
os: ["linux"]
error-types: ["swap-error"]
severities: ["warning"]
---

# Linux: Swap Priority Error

Swap priority errors occur when multiple swap devices have conflicting priorities.

## Common Causes

- Multiple swap devices with same priority
- Higher priority swap device full
- Kernel not assigning expected priority values
- zRAM swap conflicting with disk swap
- fstab entries not specifying priority

## How to Fix

### 1. Check Swap Status

```bash
swapon --show
cat /proc/swaps
free -h
```

### 2. Set Swap Priority

```bash
sudo swapoff /dev/sdb1
sudo mkswap -p 10 /dev/sdb1
sudo swapon -p 10 /dev/sdb1
```

### 3. Update fstab

```bash
# /etc/fstab
/dev/sdb1 none swap sw,pri=10 0 0
/dev/sdc1 none swap sw,pri=5 0 0
sudo swapon -a
```

## Examples

```bash
$ swapon --show
NAME      TYPE      SIZE USED PRIO
/dev/sdb1 partition 4G   50%  -2
/dev/sdc1 partition 8G   10%  -2
# Both same priority
$ sudo swapoff /dev/sdb1
$ sudo swapon -p 10 /dev/sdb1
```
