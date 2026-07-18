---
title: "[Solution] C Mutex Error — How to Fix"
description: "Fix C11/POSIX mutex errors including deadlock, uninitialized mutex, and wrong lock/unlock pairing."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Mutex Error — How to Fix

Mutex errors cause deadlocks, data races, and undefined behavior. Common mistakes include not initializing mutexes, forgetting to unlock (especially on error paths), and locking in wrong order causing deadlock.

## Common Error Messages

- `mutex deadlock detected`
- `pthread_mutex_lock: Invalid argument`
- `mutex unlocked by non-owner thread`
- `AddressSanitizer: mutex use-after-destroy`

## How to Fix It

### Always initialize mutex before use

```c
#include <threads.h>
#include <stdio.h>

mtx_t lock;

int main(void) {
    if (mtx_init(&lock, mtx_plain) != thrd_success) {
        fprintf(stderr, "mtx_init failed\n");
        return 1;
    }
    mtx_lock(&lock);
    printf("Critical section\n");
    mtx_unlock(&lock);
    mtx_destroy(&lock);
    return 0;
}
```

### Always unlock on error paths

```c
#include <threads.h>

mtx_t lock;

int process(int *data, size_t len) {
    mtx_lock(&lock);
    if (len == 0) {
        mtx_unlock(&lock);  // unlock before return!
        return -1;
    }
    data[0] = 42;
    mtx_unlock(&lock);
    return 0;
}
```

### Use consistent lock ordering to prevent deadlock

```c
#include <threads.h>

mtx_t lock_a, lock_b;

void func1(void) {
    mtx_lock(&lock_a);
    mtx_lock(&lock_b);
    // ... work ...
    mtx_unlock(&lock_b);
    mtx_unlock(&lock_a);
}

void func2(void) {
    mtx_lock(&lock_a);  // same order as func1
    mtx_lock(&lock_b);
    // ... work ...
    mtx_unlock(&lock_b);
    mtx_unlock(&lock_a);
}
```

### Use try_lock to avoid deadlock

```c
#include <threads.h>
#include <stdio.h>

mtx_t lock;

int try_process(void) {
    if (mtx_trylock(&lock) != thrd_success) {
        fprintf(stderr, "Could not acquire lock\n");
        return -1;
    }
    // ... critical section ...
    mtx_unlock(&lock);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Two threads locking mutexes in different order causing deadlock

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Forgetting to unlock mutex on error return path

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Destroying a mutex that is still locked

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always initialize mutexes with mtx_init
- **Tip 2:** Unlock mutexes on every exit path, including errors
- **Tip 3:** Use consistent lock ordering to prevent deadlock
