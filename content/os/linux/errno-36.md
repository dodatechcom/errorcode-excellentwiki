---
title: "[Solution] Linux ENOLCK (errno 36) — No Record Locks Available Fix"
description: "Fix Linux ENOLCK (errno 36) No record locks available error. Solutions for file locking and NFS issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENOLCK (errno 36) — No Record Locks Available

ENOLCK (errno 36) means the system has run out of available record locks. This error occurs when too many files have advisory locks held by processes, exhausting the kernel's lock table. It is distinct from EAGAIN (errno 7) because ENOLCK specifically refers to lock resources, not general resource availability.

## Common Causes

- Too many processes holding simultaneous file locks
- NFS lock daemon (lockd) has exhausted its lock limit
- A process acquired many locks without releasing them
- The `sysctl` limit for file locks is too low

## How to Fix ENOLCK

### 1. Check Current Lock Limits

View the kernel parameters for file locks:

```bash
sysctl fs.file-max
sysctl fs.lockd.nlm_udpport
```

### 2. Increase Lock Limits

Raise the maximum number of locks:

```bash
sudo sysctl -w fs.file-max=2097152
```

### 3. Identify Processes Holding Locks

Find processes with many locks:

```bash
cat /proc/*/locks | wc -l
ls -la /proc/*/fd | grep lock
```

### 4. Release Stale Locks

Kill processes holding unnecessary locks:

```bash
fuser -k /path/to/locked/file
```

## Verification

After adjusting limits, confirm locks can be acquired:

```bash
flock /tmp/test.lock echo "Lock acquired successfully"
```

## Related Error Codes

- [EAGAIN (errno 7)](/os/linux/errno-7/) — Resource temporarily unavailable
- [EDEADLK (errno 35)](/os/linux/errno-35/) — Resource deadlock avoided
- [EMFILE (errno 24)](/os/linux/errno-24/) — Too many open files
