---
title: "[Solution] C errno EOWNERDEAD — Owner died Fix"
description: "Fix C EOWNERDEAD (Owner died) by recovering robust mutex state, calling pthread_mutex_consistent, and reinitializing."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eownerdead", "owner-died", "robust-mutex", "pthreads", "mutex-recovery"]
weight: 5
---

# [Solution] C errno EOWNERDEAD — Owner died Fix

When a process holding a robust pthread mutex terminates abnormally (crashes), the next thread that attempts to acquire the mutex receives `EOWNERDEAD`. This error signals that the mutex owner died while holding the lock, leaving potentially inconsistent state.

## Common Causes

- The thread or process that held the robust mutex crashed or was killed.
- The mutex was locked in a PTHREAD_MUTEX_ROBUST mutex and the owner terminated.
- Memory corruption caused the owner to exit while holding the mutex.
- The system was rebooted while a robust mutex was held.

## How to Fix

Call `pthread_mutex_consistent()` to mark the mutex as consistent, then reinitialize or recover the shared state.

```c
#include <pthread.h>
#include <stdio.h>
#include <errno.h>

pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;

void init_robust_mutex(void) {
    pthread_mutexattr_t attr;
    pthread_mutexattr_init(&attr);
    pthread_mutexattr_setrobust(&attr, PTHREAD_MUTEX_ROBUST);
    pthread_mutex_init(&mtx, &attr);
    pthread_mutexattr_destroy(&attr);
}

int main(void) {
    init_robust_mutex();

    int ret = pthread_mutex_lock(&mtx);
    if (ret == EOWNERDEAD) {
        fprintf(stderr, "Previous owner died — recovering mutex\n");
        // Mark mutex as consistent
        pthread_mutex_consistent(&mtx);
        // Recover shared state here
    } else if (ret != 0) {
        fprintf(stderr, "pthread_mutex_lock failed: %d\n", ret);
        return 1;
    }

    // Critical section
    pthread_mutex_unlock(&mtx);
    return 0;
}
```

## Examples

Robust mutex recovery pattern:

```c
#include <pthread.h>
#include <stdio.h>
#include <errno.h>

pthread_mutex_t mtx;

void lock_robust(pthread_mutex_t *m) {
    int ret = pthread_mutex_lock(m);
    if (ret == EOWNERDEAD) {
        printf("Owner died — making mutex consistent\n");
        pthread_mutex_consistent(m);
    } else if (ret != 0) {
        fprintf(stderr, "Lock failed: %d\n", ret);
    }
}

int main(void) {
    pthread_mutexattr_t attr;
    pthread_mutexattr_init(&attr);
    pthread_mutexattr_setrobust(&attr, PTHREAD_MUTEX_ROBUST);
    pthread_mutex_init(&mtx, &attr);
    pthread_mutexattr_destroy(&attr);

    lock_robust(&mtx);
    // Safe to use shared resource
    pthread_mutex_unlock(&mtx);
    return 0;
}
```

## Related Errors

- [errno-130 EOWNERDEAD]({{< relref "/languages/c/errno-eOWNERDEAD" >}}) — owner died (numeric).
- [errno-131 ENOTRECOVERABLE]({{< relref "/languages/c/errno-eNOTRECOVERABLE" >}}) — state not recoverable.
- [errno-11 EAGAIN](/languages/c/errno-eOWNERDEAD/) — resource unavailable, try again.
