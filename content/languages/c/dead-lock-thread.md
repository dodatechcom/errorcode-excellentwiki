---
title: "[Solution] C Deadlock in multithreaded program"
description: "Fix C deadlock in multithreaded programs. Prevent threads from waiting on each other indefinitely."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["deadlock", "mutex", "thread", "pthreads", "concurrency"]
weight: 5
---

# Deadlock in multithreaded program

A deadlock occurs when two or more threads are each waiting for the other to release a resource, creating a circular dependency. All threads block indefinitely.

## Common Causes

```c
// Cause 1: Lock ordering violation
// Thread 1: lock A, then B
// Thread 2: lock B, then A
pthread_mutex_lock(&mutexA);
pthread_mutex_lock(&mutexB); // deadlock if Thread 2 holds B

// Cause 2: Missing unlock
pthread_mutex_lock(&mutex);
// ... critical section ...
// forgot pthread_mutex_unlock

// Cause 3: Recursive lock without recursive mutex
pthread_mutex_lock(&mutex);
pthread_mutex_lock(&mutex); // deadlock
```

## How to Fix

### Fix 1: Always lock in same order

```c
// Both threads: lock A first, then B
pthread_mutex_lock(&mutexA);
pthread_mutex_lock(&mutexB);
// ... critical section ...
pthread_mutex_unlock(&mutexB);
pthread_mutex_unlock(&mutexA);
```

### Fix 2: Use trylock

```c
if (pthread_mutex_trylock(&mutex) == 0) {
    // acquired lock
    pthread_mutex_unlock(&mutex);
} else {
    // couldn't acquire — retry or skip
}
```

### Fix 3: Use recursive mutex

```c
pthread_mutexattr_t attr;
pthread_mutexattr_init(&attr);
pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_RECURSIVE);
pthread_mutex_init(&mutex, &attr);
```

## Examples

```c
#include <stdio.h>
#include <pthread.h>

pthread_mutex_t lockA = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t lockB = PTHREAD_MUTEX_INITIALIZER;

void *thread1(void *arg) {
    pthread_mutex_lock(&lockA);
    pthread_mutex_lock(&lockB);
    printf("Thread 1\n");
    pthread_mutex_unlock(&lockB);
    pthread_mutex_unlock(&lockA);
    return NULL;
}

void *thread2(void *arg) {
    pthread_mutex_lock(&lockA); // same order!
    pthread_mutex_lock(&lockB);
    printf("Thread 2\n");
    pthread_mutex_unlock(&lockB);
    pthread_mutex_unlock(&lockA);
    return NULL;
}
```

## Related Errors

- [Race condition]({{< relref "/languages/c/race-condition-thread" >}}) — data race.
- [Stack overflow]({{< relref "/languages/c/stack-overflow-recursive" >}}) — recursion depth.
- [Infinite loop]({{< relref "/languages/c/infinite-loop" >}}) — loop hang.
