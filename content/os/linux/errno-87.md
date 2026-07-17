---
title: "[Solution] Linux EOWNERDEAD (errno 87) — Owner Died Fix"
description: "Fix Linux EOWNERDEAD (errno 87) Owner died error. Solutions for robust mutex and process recovery issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EOWNERDEAD (errno 87) — Owner Died

EOWNERDEAD (errno 87) means the previous owner of a robust mutex has terminated without releasing the lock. This error occurs when a process that held a `PTHREAD_MUTEX_ROBUST` mutex crashes or is killed, and another process tries to acquire the same mutex. It is distinct from EDEADLK (errno 35) because EOWNERDEAD indicates the owner process died, not a deadlock situation.

## Common Causes

- Process holding a robust mutex crashed or was killed
- Application terminated without releasing mutex locks
- Shared memory mutex left in inconsistent state
- Daemon process died while holding a lock

## How to Fix EOWNERDEAD

### 1. Recover the Mutex State

When EOWNERDEAD is returned, the mutex is now yours but in an inconsistent state. You must mark it consistent:

```bash
# In C: handle EOWNERDEAD
pthread_mutex_lock(&mutex);
if (rc == EOWNERDEAD) {
    // Mutex is now locked but inconsistent
    // Recover application state
    pthread_mutex_consistent(&mutex);
    // Now the mutex is usable
}
```

### 2. Use Robust Mutexes Properly

Initialize the mutex with robust attributes:

```bash
# In C: initialize robust mutex
pthread_mutexattr_t attr;
pthread_mutexattr_init(&attr);
pthread_mutexattr_setrobust(&attr, PTHREAD_MUTEX_ROBUST);
pthread_mutex_init(&mutex, &attr);
```

### 3. Clean Up Stale Locks

If the application does not use robust mutexes, clean up manually:

```bash
# Remove stale shared memory segments
ipcs -m
ipcrm -m <shmid>
```

### 4. Implement Signal Handlers

Handle unexpected termination to clean up locks:

```bash
# In C: set up cleanup handler
pthread_cleanup_push(cleanup_handler, &mutex);
// Critical section
pthread_cleanup_pop(0);
```

## Verification

After implementing robust mutex handling, confirm recovery works:

```bash
strace -e trace=futex ./program
```

## Related Error Codes

- [EDEADLK (errno 35)](/os/linux/errno-35/) — Resource deadlock avoided
- [ENOTRECOVERABLE (errno 88)](/os/linux/errno-88/) — State not recoverable
- [EAGAIN (errno 11)](/os/linux/errno-11/) — Resource temporarily unavailable
