---
title: "[Solution] Linux: segmentation-fault — segmentation fault (core dumped)"
description: "Fix Linux segmentation-fault errors. segmentation fault (core dumped) with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["process-error"]
weight: 12
---
# Linux: Segmentation Fault (SIGSEGV)

A segmentation fault (SIGSEGV) occurs when a program tries to access memory it is not allowed to use, typically indicating a bug in software or a hardware problem.

## Common Causes

- Null pointer dereference in the program
- Buffer overflow corrupting memory
- Use-after-free bug (dangling pointer)
- Stack overflow from deep recursion
- Failing RAM hardware causing memory corruption
- Corrupted shared library or binary

## How to Fix

### 1. Enable and Check Core Dumps

```bash
ulimit -c unlimited
./myprogram

# Analyze core dump
gdb ./myprogram core
# (gdb) bt
```

### 2. Enable Core Dumps System-wide

```bash
sudo sysctl -w kernel.core_pattern=core.%p
echo "kernel.core_pattern=core.%p" | sudo tee -a /etc/sysctl.conf
```

### 3. Update or Reinstall the Software

```bash
sudo apt update && sudo apt upgrade
sudo apt install --reinstall <package>
```

### 4. Test Memory (RAM)

```bash
sudo memtester 1G 1
# Or install and run memtest86+ via GRUB
```

### 5. Use Valgrind

```bash
sudo apt install valgrind
valgrind --leak-check=full ./myprogram
```

## Examples

```bash
$ ./myprogram
Segmentation fault (core dumped)

$ gdb ./myprogram core.12345
(gdb) bt
#0  0x00005555555551a3 in process_data (buf=0x0, len=100) at src/main.c:87
#1  0x0000555555555280 in main (argc=2, argv=0x7fffffffe000) at src/main.c:120

$ valgrind ./myprogram
==12345== Invalid write of size 4
==12345==    at 0x555555551A3: process_data (main.c:87)
==12345==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
```
