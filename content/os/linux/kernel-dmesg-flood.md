---
title: "[Solution] Linux: kernel-dmesg-flood -- kernel dmesg buffer flooding"
description: "Fix Linux kernel dmesg flood errors. Kernel ring buffer flooding with rapid error messages."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Dmesg Flood

Dmesg flood occurs when the kernel ring buffer fills rapidly with messages, making errors hard to identify.

## Common Causes

- Faulty hardware generating repeated interrupts
- Network driver dropping excessive packets
- USB device causing continuous error messages
- Disk controller reporting repeated I/O errors
- Broken sensor driver producing spam

## How to Fix

### 1. Check Current Messages

```bash
dmesg --level=err,warn | tail -50
dmesg -T | tail -100
```

### 2. Reduce Verbosity

```bash
sudo dmesg -n 1
sudo sysctl kernel.printk=4 4 1 7
```

### 3. Find Source of Flood

```bash
dmesg -T | awk '{print $1}' | sort | uniq -c | sort -rn | head -10
sudo journalctl -k --no-pager -o cat | tail -200
```

## Examples

```bash
$ dmesg --level=err,warn | wc -l
4823
$ dmesg -T | awk '{print $1}' | sort | uniq -c | sort -rn | head -5
  1204 [UFW BLOCK]
   892 usb 1-1: device not accepting address
   445 EXT4-fs error
```
