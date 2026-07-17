---
title: "[Solution] C errno ENOTRECOVERABLE — State not recoverable Fix"
description: "Fix C ENOTRECOVERABLE (State not recoverable) by handling unrecoverable mutex state and reinitializing shared resources."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENOTRECOVERABLE — State not recoverable Fix

When a robust mutex's state is inconsistent and cannot be recovered (either because `pthread_mutex_consistent()` was not called after `EOWNERDEAD`, or the state is truly unrecoverable), subsequent lock attempts fail with `errno` set to `ENOTRECOVERABLE`.

## Common Causes

- A robust mutex became inconsistent after the owner died, but `pthread_mutex_consistent()` was not called.
- The shared protected data is corrupted beyond recovery.
- The mutex owner died and the shared state is permanently invalid.
- The system cannot determine if the mutex state is safe to use.

## How to Fix

Reinitialize the mutex and shared state from scratch when `ENOTRECOVERABLE` occurs.

```c
#include <pthread.h>
#include <stdio.h>
#include <errno.h>

pthread_mutex_t mtx;

void init_mutex(void) {
    pthread_mutexattr_t attr;
    pthread_mutexattr_init(&attr);
    pthread_mutexattr_setrobust(&attr, PTHREAD_MUTEX_ROBUST);
    pthread_mutex_init(&mtx, &attr);
    pthread_mutexattr_destroy(&attr);
}

int lock_with_recovery(pthread_mutex_t *m) {
    int ret = pthread_mutex_lock(m);
    if (ret == EOWNERDEAD) {
        pthread_mutex_consistent(m);
        return 0;
    } else if (ret == ENOTRECOVERABLE) {
        fprintf(stderr, "Mutex not recoverable — reinitializing\n");
        pthread_mutex_destroy(m);
        init_mutex();
        return pthread_mutex_lock(m);
    }
    return ret;
}

int main(void) {
    init_mutex();
    lock_with_recovery(&mtx);
    // Use shared resource
    pthread_mutex_unlock(&mtx);
    return 0;
}
```

## Examples

Handling unrecoverable mutex:

```c
#include <pthread.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    pthread_mutex_t mtx;
    pthread_mutexattr_t attr;
    pthread_mutexattr_init(&attr);
    pthread_mutexattr_setrobust(&attr, PTHREAD_MUTEX_ROBUST);
    pthread_mutex_init(&mtx, &attr);

    int ret = pthread_mutex_lock(&mtx);
    if (ret == ENOTRECOVERABLE) {
        fprintf(stderr, "Mutex state not recoverable (errno %d)\n", ENOTRECOVERABLE);
        fprintf(stderr, "Must destroy and reinitialize mutex\n");
    }
    return 0;
}
```

## Related Errors

- [errno-131 ENOTRECOVERABLE]({{< relref "/languages/c/errno-eNOTRECOVERABLE" >}}) — state not recoverable (numeric).
- [errno-130 EOWNERDEAD]({{< relref "/languages/c/errno-eOWNERDEAD" >}}) — owner died.
- [errno-22 EINVAL](/languages/c/errno-eNOTRECOVERABLE/) — invalid argument.
