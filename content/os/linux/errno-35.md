---
title: "[Solution] Linux EDEADLK (errno 35) — Resource Deadlock Avoided Fix"
description: "Fix Linux EDEADLK (errno 35) Resource deadlock avoided error. Solutions for file locking and deadlock issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EDEADLK (errno 35) — Resource Deadlock Avoided

EDEADLK (errno 35) means a deadlock condition was detected and avoided during a file locking operation. This error occurs when a process attempts to acquire a lock that would cause all processes to be blocked indefinitely. The kernel prevents the deadlock by returning this error instead of allowing the lock. It is distinct from EAGAIN (errno 11) because EDEADLK specifically refers to deadlock prevention, not resource availability.

## Common Causes

- Two processes each holding a lock and requesting the other's lock
- Using `fcntl()` locking with conflicting lock ranges
- Recursive locking attempts on the same file region
- Improper lock ordering in multi-process applications

## How to Fix EDEADLK

### 1. Identify the Conflicting Locks

Use `lsof` to find which processes hold locks on the file:

```bash
lsof /path/to/locked_file
```

### 2. Implement Lock Ordering

Ensure all processes acquire locks in the same order to prevent deadlocks:

```bash
# Example: always lock file A before file B
# Process 1: lock file_a, then file_b
# Process 2: lock file_a, then file_b (same order)
```

### 3. Use Lock Retry with Backoff

Implement retry logic with exponential backoff:

```bash
#!/bin/bash
retries=5
for i in $(seq 1 $retries); do
  flock -w 5 /path/to/lockfile echo "lock acquired"
  if [ $? -eq 0 ]; then
    break
  fi
  sleep $((2 ** i))
done
```

### 4. Check for Stale Locks

Remove stale lock files if processes have crashed:

```bash
fuser -k /path/to/lockfile
rm -f /path/to/lockfile
```

## Verification

After fixing lock ordering, confirm operations complete without deadlock:

```bash
strace -e trace=fcntl ./my_application
```

## Related Error Codes

- [EAGAIN (errno 11)](/os/linux/errno-11/) — Resource temporarily unavailable
- [EBUSY (errno 16)](/os/linux/errno-16/) — Device or resource busy
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
