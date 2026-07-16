---
title: "[Solution] Linux ENOTRECOVERABLE (errno 88) — State Not Recoverable Fix"
description: "Fix Linux ENOTRECOVERABLE (errno 88) State not recoverable error. Solutions for unrecoverable mutex and state issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enotrecoverable", "mutex", "errno-88", "recovery", "robust"]
weight: 5
---

# Linux ENOTRECOVERABLE (errno 88) — State Not Recoverable

ENOTRECOVERABLE (errno 88) means the state protected by a robust mutex cannot be recovered. This error occurs after EOWNERDEAD when the application fails to make the mutex consistent, or when the protected state is irreparably corrupted. It is distinct from EOWNERDEAD (errno 87) because ENOTRECOVERABLE means recovery is impossible, while EOWNERDEAD means recovery can be attempted.

## Common Causes

- Failed to call `pthread_mutex_consistent()` after EOWNERDEAD
- Protected data structure was corrupted beyond repair
- Two processes attempted recovery simultaneously
- Application state is irrecoverable after owner death

## How to Fix ENOTRECOVERABLE

### 1. Destroy and Reinitialize the Mutex

The only fix is to reset the mutex:

```bash
# In C: destroy and reinitialize
pthread_mutex_destroy(&mutex);
pthread_mutex_init(&mutex, &attr);
```

### 2. Recover Application State

Rebuild the protected state from a checkpoint:

```bash
# Restore from last known good state
cp /var/lib/app/checkpoint.dat /var/lib/app/state.dat
```

### 3. Implement Proper Recovery

Handle both EOWNERDEAD and ENOTRECOVERABLE:

```bash
# In C: comprehensive recovery
int rc = pthread_mutex_lock(&mutex);
if (rc == EOWNERDEAD) {
    pthread_mutex_consistent(&mutex);
    recover_state();
} else if (rc == ENOTRECOVERABLE) {
    pthread_mutex_destroy(&mutex);
    pthread_mutex_init(&mutex, &attr);
    rebuild_state();
}
```

### 4. Use Checkpointing

Regularly save state to enable recovery:

```bash
#!/bin/bash
# Periodic checkpoint script
cp /var/lib/app/state.dat /var/lib/app/checkpoint.dat
```

## Verification

After implementing recovery, confirm the mutex works:

```bash
strace -e trace=futex ./program
```

## Related Error Codes

- [EOWNERDEAD (errno 87)](/os/linux/errno-87/) — Owner died
- [EDEADLK (errno 35)](/os/linux/errno-35/) — Resource deadlock avoided
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
