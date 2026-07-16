---
title: "[Solution] Linux ENOSYS (errno 38) — Function Not Implemented Fix"
description: "Fix Linux ENOSYS (errno 38) Function not implemented error. Solutions for unsupported system call issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enOSYS", "syscall", "errno-38", "kernel"]
weight: 5
---

# Linux ENOSYS (errno 38) — Function Not Implemented

ENOSYS (errno 38) means the requested system call is not implemented by the kernel. This error occurs when a program tries to use a system call that does not exist on the current kernel version or platform. It is distinct from EINVAL (errno 22) because ENOSYS indicates the syscall itself is missing, not that the arguments are wrong.

## Common Causes

- Running a program compiled for a newer kernel on an older kernel
- Using system calls not available on the current CPU architecture
- The kernel was compiled without support for certain features
- Container or chroot environment limiting available syscalls

## How to Fix ENOSYS

### 1. Check Kernel Version

Verify the running kernel version:

```bash
uname -r
```

### 2. Verify Syscall Availability

Check if the specific syscall exists:

```bash
ausyscall --dump | grep <syscall_name>
```

### 3. Upgrade the Kernel

Install a newer kernel that supports the required syscall:

```bash
sudo apt update
sudo apt install linux-generic-hwe-22.04
```

### 4. Recompile the Program

Compile against the current kernel's headers:

```bash
uname -r
ls /usr/src/linux-headers-$(uname -r)
gcc -o program source.c
```

## Verification

After upgrading the kernel, confirm the syscall is available:

```bash
strace -e trace=<syscall_name> ./program
```

## Related Error Codes

- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [ENOSYS (errno 38)](/os/linux/errno-38/) — Function not implemented
- [EOPNOTSUPP (errno 95)](/os/linux/errno-95/) — Operation not supported
