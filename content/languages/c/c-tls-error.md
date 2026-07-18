---
title: "[Solution] C Thread-Local Storage Error — How to Fix"
description: "Fix C _Thread_local / __thread storage errors including initialization, destruction, and portability."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Thread-Local Storage Error — How to Fix

Thread-local storage (TLS) provides per-thread copies of variables. Common errors include using non-atomic operations on TLS across threads, missing TLS initialization, and compiler portability issues with _Thread_local vs __thread.

## Common Error Messages

- `Thread-local variable not initialized in worker thread`
- `Non-portable TLS syntax between compilers`
- `TLS cleanup function never called`
- `Race condition on non-TLS variable mistaken for TLS`

## How to Fix It

### Use _Thread_local (C11) correctly

```c
#include <stdio.h>
#include <threads.h>

_Thread_local int tls_counter = 0;

int worker(void *arg) {
    tls_counter = *(int *)arg;
    printf("Thread %d: counter=%d\n", *(int *)arg, tls_counter);
    return 0;
}

int main(void) {
    int vals[] = {1, 2, 3};
    thrd_t t[3];
    for (int i = 0; i < 3; i++)
        thrd_create(&t[i], worker, &vals[i]);
    for (int i = 0; i < 3; i++)
        thrd_join(t[i], NULL);
    return 0;
}
```

### Use __thread for GCC compatibility

```c
#include <stdio.h>
__thread int tls_val = 0;

void *worker(void *arg) {
    tls_val = 42;
    printf("val: %d\n", tls_val);
    return NULL;
}
```

### Initialize TLS with constructor

```c
#include <stdio.h>

static _Thread_local int initialized = 0;
static _Thread_local int tls_data;

void ensure_init(void) {
    if (!initialized) {
        tls_data = 100;
        initialized = 1;
    }
}
```

### Use pthread_key_create for portable TLS with destructors

```c
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>

pthread_key_t key;
void destructor(void *val) { free(val); }

void init_tls(void) {
    pthread_key_create(&key, destructor);
}

void set_tls(int val) {
    int *p = malloc(sizeof(int));
    *p = val;
    pthread_setspecific(key, p);
}

int get_tls(void) {
    int *p = pthread_getspecific(key);
    return p ? *p : 0;
}
```

## Common Scenarios

### Scenario 1: TLS variable not having expected value in new thread

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using __thread instead of _Thread_local causing portability issues

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: TLS destructors not called on thread exit

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Use _Thread_local for C11 or __thread for GCC
- **Tip 2:** Initialize TLS variables explicitly in each thread
- **Tip 3:** Consider pthread_key_create for portable TLS with destructors
