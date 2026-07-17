---
title: "[Solution] C Race condition in thread shared data"
description: "Fix C race condition in multithreaded programs. Protect shared data with proper synchronization."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Race condition in thread shared data

A race condition occurs when multiple threads access shared data concurrently and at least one thread modifies the data. The outcome depends on unpredictable thread scheduling.

## Common Causes

```c
// Cause 1: Unprotected shared variable
int counter = 0;

void *increment(void *arg) {
    for (int i = 0; i < 1000000; i++) {
        counter++; // race condition
    }
    return NULL;
}

// Cause 2: Read-modify-write without lock
shared_struct.data = shared_struct.data + 1;

// Cause 3: TOCTOU race
if (access("file", F_OK) == 0) {
    // another process may delete file here
    FILE *f = fopen("file", "r"); // may fail
}
```

## How to Fix

### Fix 1: Use mutex for shared data

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
int counter = 0;

void *increment(void *arg) {
    for (int i = 0; i < 1000000; i++) {
        pthread_mutex_lock(&lock);
        counter++;
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}
```

### Fix 2: Use atomic operations

```c
#include <stdatomic.h>
atomic_int counter = 0;

void *increment(void *arg) {
    for (int i = 0; i < 1000000; i++) {
        counter++;
    }
    return NULL;
}
```

### Fix 3: Use thread-safe functions

```c
// Use strtok_r instead of strtok
char *saveptr;
char *token = strtok_r(str, " ", &saveptr);
```

## Examples

```c
#include <stdio.h>
#include <pthread.h>

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
int shared = 0;

void *worker(void *arg) {
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&lock);
        shared++;
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}
```

## Related Errors

- [Deadlock]({{< relref "/languages/c/dead-lock-thread" >}}) — threads stuck.
- [Stack overflow]({{< relref "/languages/c/stack-overflow-recursive" >}}) — recursion depth.
- [Memory leak]({{< relref "/languages/c/memory-leak-valgrind" >}}) — leaked memory.
