---
title: "[Solution] Linux Segmentation Fault (SIGSEGV) — Fix Crash Errors"
description: "Fix Linux 'Segmentation fault (core dumped)' errors. Diagnose segfaults with crash logs, memory tools, and software fixes."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["segmentation-fault", "segfault", "sigsegv", "core-dumped", "memory"]
weight: 5
---

# Linux: Segmentation Fault (SIGSEGV)

A `Segmentation fault (core dumped)` means a process tried to access memory it's not allowed to use — either reading or writing to an invalid memory address. This typically indicates a bug in the software (null pointer dereference, buffer overflow, use-after-free) but can also be caused by failing RAM or corrupted libraries.

## Common Causes

- Software bug (null pointer dereference, buffer overflow, use-after-free)
- Corrupted shared libraries or binary
- Failing or faulty RAM modules
- Insufficient stack space for the process
- Incompatible or outdated software

## How to Fix

### 1. Check for Core Dumps

If the program generated a core dump, you can analyze it with `gdb`:

```bash
# Enable core dumps if not already enabled
ulimit -c unlimited

# Run the crashing program
./myprogram

# Analyze the core dump
gdb ./myprogram core
```

In gdb, use `bt` (backtrace) to see where the crash occurred:

```
(gdb) bt
#0  0x00007fff12345678 in my_function () from ./libsomething.so
#1  0x0000555555560000 in main () at main.c:42
```

### 2. Enable Core Dumps System-Wide

```bash
# Check current core dump pattern
cat /proc/sys/kernel/core_pattern

# Enable core dumps for all users
sudo sysctl -w kernel.core_pattern=core.%p

# Make persistent
echo "kernel.core_pattern=core.%p" | sudo tee -a /etc/sysctl.conf
```

### 3. Update or Reinstall the Software

A segfault in a specific application is often fixed by updating:

```bash
# Debian/Ubuntu
sudo apt update && sudo apt upgrade

# RHEL/CentOS/Fedora
sudo dnf update

# Reinstall the specific package
sudo apt reinstall package-name
```

### 4. Test Memory (RAM)

Failing RAM can cause random segfaults across multiple programs:

```bash
# Install memtest86+
sudo apt install memtest86+    # Debian/Ubuntu
sudo dnf install memtest86+    # RHEL/CentOS

# Run from GRUB menu at boot
sudo update-grub
```

Or run the userspace test (less thorough but doesn't require reboot):

```bash
sudo memtester 1G 1
```

### 5. Check for Stack Overflow

A process with too-small a stack can segfault:

```bash
# Check current stack size limit
ulimit -s

# Increase stack size
ulimit -s unlimited

# Or for a specific run
ulimit -s 65536 && ./myprogram
```

### 6. Use Valgrind for Memory Bugs

```bash
# Install valgrind
sudo apt install valgrind

# Run your program through valgrind
valgrind --leak-check=full ./myprogram
```

Valgrind will report memory leaks, invalid reads/writes, and use of uninitialized memory.

## Examples

```bash
$ ./myprogram
Segmentation fault (core dumped)

$ gdb ./myprogram core.12345
(gdb) bt
#0  0x00005555555551a3 in process_data (buf=0x0, len=100) at src/main.c:87
#1  0x0000555555555280 in main (argc=2, argv=0x7fffffffe000) at src/main.c:120

# A null pointer (buf=0x0) was passed to process_data
```

## Related Errors

- [Out of memory / OOM killer]({{< relref "/os/linux/oom-killer" >}}) — Process killed by OOM
- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — Memory allocation failure
- [Kernel panic]({{< relref "/os/linux/kernel-panic2" >}}) — System crash
