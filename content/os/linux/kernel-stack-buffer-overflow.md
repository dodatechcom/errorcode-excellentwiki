---
title: "[Solution] Linux: kernel-stack-buffer-overflow -- kernel stack buffer overflow"
description: "Fix Linux kernel stack buffer overflow errors. Kernel stack buffer overflow in module or driver."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Kernel Stack Buffer Overflow

A kernel stack buffer overflow occurs when a kernel function writes beyond the allocated stack frame.

## Common Causes

- Deeply nested function calls exhausting stack space
- Large stack-allocated arrays in kernel code
- Recursive filesystem or networking calls
- Bug in kernel module allocating excessive stack memory
- Compiler optimization changing stack layout

## How to Fix

### 1. Check Kernel Logs

```bash
sudo dmesg | grep -i "stack overflow"
sudo journalctl -k | grep -i "stack"
```

### 2. Increase Stack Size

```bash
cat /proc/<pid>/limits | grep "Stack size"
# Add to GRUB: thread_info.order=2
```

### 3. Update or Revert Kernel

```bash
sudo apt list --installed | grep linux-image
sudo apt install linux-image-<previous-version>
```

## Examples

```bash
$ sudo dmesg | grep -i "stack"
[9876.543] NMI watchdog: BUG: stack overflow on CPU 0
[9876.544] Call Trace:
[9876.545]  recursive_func+0x45/0x80
[9876.546]  recursive_func+0x5e/0x80
```
