---
title: "[Solution] C Condition Variable Error — How to Fix"
description: "Fix C11/POSIX condition variable errors including lost wakeups and spurious wakeups."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Condition Variable Error — How to Fix

Condition variables coordinate threads waiting for conditions. Common errors include signal without holding the mutex, not using a while loop for wait (spurious wakeups), and lost wakeups from signaling before the wait.

## Common Error Messages

- `Lost wakeup — condition signaled before wait`
- `Spurious wakeup causes incorrect behavior`
- `pthread_cond_wait without holding mutex`
- `Condition variable not initialized`

## How to Fix It

### Use while loop for condition wait

```c
#include <threads.h>
#include <stdio.h>

mtx_t lock;
cnd_t cond;
int ready = 0;

int consumer(void *arg) {
    mtx_lock(&lock);
    while (!ready)
        cnd_wait(&cond, &lock);
    printf("Got data!\n");
    mtx_unlock(&lock);
    return 0;
}

int producer(void *arg) {
    mtx_lock(&lock);
    ready = 1;
    cnd_signal(&cond);
    mtx_unlock(&lock);
    return 0;
}
```

### Initialize condition variable properly

```c
#include <threads.h>

mtx_t lock;
cnd_t cond;

int main(void) {
    mtx_init(&lock, mtx_plain);
    cnd_init(&cond);
    // ... use ...
    cnd_destroy(&cond);
    mtx_destroy(&lock);
    return 0;
}
```

### Use broadcast for multiple waiters

```c
#include <threads.h>
#include <stdio.h>

mtx_t lock;
cnd_t cond;
int count = 0;

void notify_all(void) {
    mtx_lock(&lock);
    count++;
    cnd_broadcast(&cond);
    mtx_unlock(&lock);
}
```

### Signal while holding the mutex

```c
mtx_lock(&lock);
data_ready = 1;
cnd_signal(&cond);
mtx_unlock(&lock);
```

## Common Scenarios

### Scenario 1: Producer signals before consumer starts waiting

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using if instead of while for wait causes spurious wakeup bugs

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Signaling without holding the associated mutex

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always use while-loop for cnd_wait, never if
- **Tip 2:** Signal condition while holding the associated mutex
- **Tip 3:** Initialize cnd_t with cnd_init before use
