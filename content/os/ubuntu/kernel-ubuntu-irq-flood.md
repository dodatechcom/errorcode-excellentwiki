---
title: "[Solution] Ubuntu Server: kernel-ubuntu-irq-flood"
description: "Fix Ubuntu kernel-ubuntu-irq-flood. IRQ line floods causing system slowdown or hang."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Ubuntu IRQ Flood

An IRQ line floods the system with interrupts, causing slowdown or hang.

## Common Causes
- Faulty hardware device generating excessive interrupts
- IRQ routing conflict between devices
- Broken NIC driver triggering interrupt storm
- Virtual machine passthrough issue

## How to Fix
1. Check IRQ distribution
```bash
cat /proc/interrupts
```
2. Check for interrupt storm
```bash
watch -n 1 cat /proc/interrupts
```
3. Isolate problematic device
```bash
sudo sh -c "echo 0 > /proc/irq/<IRQ_NUM>/smp_affinity"
```

## Examples
```bash
$ watch -n 1 cat /proc/interrupts
           CPU0       CPU1
  42:   9999999   0   PCI-MSI-edge  eth0
```
