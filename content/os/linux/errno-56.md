---
title: "[Solution] Linux EBADFD (errno 56) — File Descriptor in Bad State Fix"
description: "Fix Linux EBADFD (errno 56) File descriptor in bad state error. Solutions for corrupted file descriptor issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EBADFD (errno 56) — File Descriptor in Bad State

EBADFD (errno 56) means the file descriptor is in a bad state and cannot be used for the requested operation. This error occurs when a system call is given a file descriptor that has been closed, corrupted, or is in an inconsistent state. It is distinct from EBADF (errno 9) because EBADFD indicates the descriptor exists but is in an invalid state, not simply bad.

## Common Causes

- File descriptor was closed by another thread or process
- Use-after-free of file descriptor in multi-threaded programs
- Kernel driver bug leaving a descriptor in inconsistent state
- Corrupted user-space data structures referencing file descriptors

## How to Fix EBADFD

### 1. Check for Closed File Descriptors

Find which file descriptors are open:

```bash
ls -la /proc/self/fd/
ls -la /proc/<pid>/fd/
```

### 2. Use lsof to Track File Descriptors

Monitor open file descriptors:

```bash
lsof -p <pid>
```

### 3. Fix Race Conditions in Multi-Threaded Code

Ensure file descriptors are not closed while in use:

```bash
# Check for file descriptor leaks
ls /proc/<pid>/fd | wc -l
```

### 4. Validate File Descriptor Before Use

Always check if a file descriptor is valid before use:

```bash
# In C: check with fcntl
fcntl(fd, F_GETFD) != -1
```

### 5. Check for Driver Issues

Look for kernel driver errors:

```bash
dmesg | grep -i "error\|fail\|fd"
```

## Verification

After fixing the descriptor issue, confirm operations succeed:

```bash
lsof -p <pid> | grep <problematic_file>
```

## Related Error Codes

- [EBADF (errno 9)](/os/linux/errno-9/) — Bad file descriptor
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
