---
title: "[Solution] C call_once / once_init Error — How to Fix"
description: "Fix C11 call_once initialization errors. Ensure thread-safe one-time initialization."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C call_once / once_init Error — How to Fix

call_once ensures a function runs exactly once even with multiple threads. Common errors include using call_once with incorrect once_flag initialization, performing blocking operations inside the once callback, and not checking once_flag state properly.

## Common Error Messages

- `call_once function throws exception`
- `Once flag not properly initialized with ONCE_FLAG_INIT`
- `Blocking inside call_once causes thread starvation`
- `Deadlock from call_once callback acquiring same lock`

## How to Fix It

### Initialize once_flag correctly

```c
#include <threads.h>
#include <stdio.h>

static once_flag flag = ONCE_FLAG_INIT;
static int initialized = 0;

void init_once(void) {
    initialized = 42;
    printf("Initialized once!\n");
}

int main(void) {
    call_once(&flag, init_once);
    call_once(&flag, init_once);  // does nothing
    printf("value: %d\n", initialized);
    return 0;
}
```

### Use for thread-safe singleton

```c
#include <threads.h>
#include <stdlib.h>

static once_flag flag = ONCE_FLAG_INIT;
static void *instance = NULL;

void create_instance(void) {
    instance = malloc(1024);
}

void *get_instance(void) {
    call_once(&flag, create_instance);
    return instance;
}
```

### Avoid blocking in call_once callback

```c
#include <threads.h>

static once_flag flag = ONCE_FLAG_INIT;
static int config = 0;

void load_config(void) {
    config = 1;  // fast operation only
    // Do NOT call sem_wait, mtx_lock, or sleep here
}

int get_config(void) {
    call_once(&flag, load_config);
    return config;
}
```

### Error handling in call_once

```c
#include <threads.h>
#include <stdio.h>

static once_flag init_flag = ONCE_FLAG_INIT;
static int init_result = -1;

void try_init(void) {
    init_result = 0;  // simplified
}

int ensure_init(void) {
    call_once(&init_flag, try_init);
    return init_result;
}
```

## Common Scenarios

### Scenario 1: call_once callback blocks causing thread starvation

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: once_flag not initialized with ONCE_FLAG_INIT

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Recursive call_once from within callback causes deadlock

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Keep call_once callbacks fast and non-blocking
- **Tip 2:** Always initialize once_flag with ONCE_FLAG_INIT at declaration
- **Tip 3:** Never call call_once recursively from within the callback
