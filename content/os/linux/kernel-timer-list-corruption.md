---
title: "[Solution] Linux: kernel-timer-list-corruption -- kernel timer list corruption"
description: "Fix Linux kernel timer list corruption errors. Kernel timer list corruption detected at runtime."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Timer List Corruption

Timer list corruption happens when the kernel detects inconsistent state in timer data structures.

## Common Causes

- Race condition in timer handling code
- Timer callback accessing freed memory
- SMP system with incorrect locking
- Power management interfering with timer hardware
- Faulty CPU causing incorrect timer values

## How to Fix

### 1. Check Timer Errors

```bash
sudo dmesg | grep -i "timer"
sudo journalctl -k | grep -i "timer_list"
```

### 2. Disable Deep C-States

```bash
echo "1" | sudo tee /sys/devices/system/cpu/cpu0/cpuidle/state3/disable
# Add to GRUB: intel_idle.max_cstate=1
```

### 3. Update BIOS and Kernel

```bash
sudo dmidecode -s system-product-name
sudo apt upgrade linux-image-$(uname -r)
```

## Examples

```bash
$ sudo dmesg | grep timer_list
[5555.111] LIST_HEAD corruption detected in timer_list
[5555.112] CPU: 2 PID: 0 Comm: swapper/2 Not tainted 5.15.0-56
[5555.113] Call Trace:
[5555.114]  __run_timers+0x23c/0x2a0
```
