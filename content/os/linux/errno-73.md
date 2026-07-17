---
title: "[Solution] Linux ETOOMANYREFS (errno 73) — Too Many References Fix"
description: "Fix Linux ETOOMANYREFS (errno 73) Too many references error. Solutions for reference count limit issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ETOOMANYREFS (errno 73) — Too Many References

ETOOMANYREFS (errno 73) means too many references have been created for a resource. This error typically occurs when using `splice()` or `tee()` between pipes and the reference count on a pipe buffer exceeds the kernel limit. It is distinct from EMLINK (errno 31) because ETOOMANYREFS refers to kernel reference counts, not filesystem hard links.

## Common Causes

- Excessive use of `splice()` or `tee()` on pipe buffers
- Kernel pipe buffer reference count overflow
- Memory pressure causing pipe buffer reuse issues
- Application creating too many duplicated pipe references

## How to Fix ETOOMANYREFS

### 1. Check Pipe Usage

Monitor active pipe file descriptors:

```bash
ls -la /proc/<pid>/fd | grep pipe
```

### 2. Reduce Splice Operations

Minimize the number of `splice()` calls:

```bash
# Use larger buffers to reduce operation count
splice(fd_in, NULL, fd_out, NULL, large_size, 0);
```

### 3. Increase Pipe Buffer Size

Adjust the kernel pipe buffer limit:

```bash
sudo sysctl -w fs.pipe-max-size=1048576
```

### 4. Use read/write Instead of splice

If possible, use standard read/write operations:

```bash
read(fd_in, buffer, size);
write(fd_out, buffer, size);
```

### 5. Check for Pipe Leaks

Find processes with many open pipes:

```bash
ls /proc/<pid>/fd -la | grep pipe | wc -l
```

## Verification

After reducing pipe references, confirm operations succeed:

```bash
strace -e trace=splice,tee ./program
ls /proc/<pid>/fd -la | grep pipe | wc -l
```

## Related Error Codes

- [EMLINK (errno 31)](/os/linux/errno-31/) — Too many links
- [ENOSPC (errno 28)](/os/linux/errno-28/) — No space left on device
- [EAGAIN (errno 11)](/os/linux/errno-11/) — Resource temporarily unavailable
