---
title: "[Solution] Linux ENFILE (errno 23) — Too Many Open Files in System Fix"
description: "Fix Linux ENFILE (errno 23) Too many open files in system error. Solutions for system-wide file descriptor limits."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENFILE (errno 23) — Too Many Open Files in System

ENFILE (errno 23) means the system has reached its maximum limit for open file descriptors system-wide. This error occurs when the kernel cannot allocate a new file descriptor because the total number of open files across all processes has hit the system limit. It is distinct from EMFILE (errno 24) because ENFILE refers to a system-wide limit, not a per-process limit.

## Common Causes

- Too many processes running simultaneously with open files
- File descriptor leaks in long-running applications
- System-wide limit too low for the workload
- Database or web server exhausts available descriptors

## How to Fix ENFILE

### 1. Check Current System Limits

View the system-wide file descriptor limits:

```bash
cat /proc/sys/fs/file-max
cat /proc/sys/fs/file-nr
```

### 2. Increase the System-Wide Limit

Raise the maximum number of open files:

```bash
sudo sysctl -w fs.file-max=2097152
```

Make it permanent:

```bash
echo "fs.file-max=2097152" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

### 3. Check Per-Process Limits

Verify per-process limits:

```bash
ulimit -n
```

### 4. Increase Per-Process Limits

Edit `/etc/security/limits.conf`:

```bash
sudo nano /etc/security/limits.conf
```

Add:

```
* soft nofile 65535
* hard nofile 65535
```

### 5. Find Processes Using Many File Descriptors

Identify which processes are consuming the most descriptors:

```bash
for pid in /proc/[0-9]*/fd; do
  count=$(ls "$pid" 2>/dev/null | wc -l)
  echo "$count $pid"
done | sort -rn | head -20
```

## Verification

After applying changes, confirm the new limits:

```bash
cat /proc/sys/fs/file-max
ulimit -n
```

## Related Error Codes

- [EMFILE (errno 24)](/os/linux/errno-24/) — Too many open files in process
- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
- [ENOSPC (errno 28)](/os/linux/errno-28/) — No space left on device
