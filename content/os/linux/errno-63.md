---
title: "[Solution] Linux ENOSYS (errno 63) — Function Not Implemented Fix"
description: "Fix Linux ENOSYS (errno 63) Function not implemented error. Solutions for unsupported system call issues on STREAMS."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enosys", "syscall", "errno-63", "streams", "kernel"]
weight: 5
---

# Linux ENOSYS (errno 63) — Function Not Implemented

ENOSYS (errno 63) means the function is not implemented in the kernel. This error occurs when a STREAMS-based or legacy system call is invoked but the kernel does not provide an implementation. It is distinct from EOPNOTSUPP (errno 95) because ENOSYS indicates the function is completely missing, not just unsupported for a specific object.

## Common Causes

- Legacy STREAMS-based system calls not implemented in Linux
- Using a function from a different UNIX variant on Linux
- Kernel compiled without support for a specific feature
- Container or chroot environment limiting available functions

## How to Fix ENOSYS

### 1. Check Kernel Version

Verify the running kernel version:

```bash
uname -r
uname -a
```

### 2. Identify the Missing Function

Determine which function is not implemented:

```bash
strace -e trace=all ./program 2>&1 | grep ENOSYS
```

### 3. Find Linux Alternatives

Look for Linux-specific alternatives to the missing function:

```bash
man -k function_name
apropos function_name
```

### 4. Upgrade the Kernel

Install a kernel that supports the required function:

```bash
sudo apt update
sudo apt install linux-generic-hwe-22.04
```

### 5. Use Compatibility Layers

For legacy STREAMS applications, use compatibility libraries:

```bash
# Install LiS (Linux STREAMS) if needed
sudo apt install streams
```

## Verification

After upgrading, confirm the function is available:

```bash
ausyscall --dump | grep function_name
```

## Related Error Codes

- [EOPNOTSUPP (errno 95)](/os/linux/errno-95/) — Operation not supported
- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [ENOSYS (errno 38)](/os/linux/errno-38/) — Function not implemented
