---
title: "[Solution] Linux EMFILE (errno 24) — Too Many Open Files Fix"
description: "Fix Linux EMFILE (errno 24) Too many open files error. Solutions for file descriptor limit issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EMFILE (errno 24) — Too Many Open Files

EMFILE (errno 24) means the process has reached its limit for open file descriptors. This error occurs when a program tries to open more files than the system allows. It is distinct from ENFILE (errno 23) because EMFILE is a per-process limit, while ENFILE is a system-wide limit.

## Common Causes

- A program opens files without closing them (file descriptor leak)
- The per-process file descriptor limit is too low for the workload
- Connection pools or thread pools opening many file descriptors
- Temporary files not being cleaned up

## How to Fix EMFILE

### 1. Check Current Limits

View the current per-process file descriptor limit:

```bash
ulimit -n
```

### 2. Increase the Limit Temporarily

Raise the limit for the current session:

```bash
ulimit -n 65535
```

### 3. Set Permanent Limits

Edit `/etc/security/limits.conf` for persistent changes:

```bash
sudo nano /etc/security/limits.conf
```

Add lines:

```
* soft nofile 65535
* hard nofile 65535
```

### 4. Find the Leaking Process

Identify processes with many open file descriptors:

```bash
ls /proc/*/fd | wc -l
for pid in /proc/[0-9]*/fd; do echo "$pid: $(ls $pid | wc -l)"; done | sort -t: -k2 -n -r | head -10
```

## Verification

After applying the fix, verify the new limit:

```bash
ulimit -n
```

## Related Error Codes

- [ENFILE (errno 23)](/os/linux/errno-23/) — Too many open files in system
- [ENOSPC (errno 28)](/os/linux/errno-28/) — No space left on device
- [EAGAIN (errno 7)](/os/linux/errno-7/) — Resource temporarily unavailable
