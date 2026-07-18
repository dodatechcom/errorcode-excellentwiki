---
title: "[Solution] C setjmp/longjmp Error — How to Fix"
description: "Fix C setjmp/longjmp errors including stack corruption and non-volatile local variable loss."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C setjmp/longjmp Error — How to Fix

setjmp/longjmp provides non-local jumps. Common errors include using automatic (stack) local variables after longjmp, not checking setjmp return value, and using longjmp across different threads. Local variables not declared volatile may have indeterminate values after longjmp.

## Common Error Messages

- `Value of automatic variable indeterminate after longjmp`
- `longjmp to invalid or expired stack frame`
- `setjmp called in nested function with VLA`
- `Stack corruption from longjmp across incompatible frames`

## How to Fix It

### Declare variables modified after longjmp as volatile

```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf env;

void handler(void) {
    longjmp(env, 1);
}

int main(void) {
    volatile int x = 0;
    if (setjmp(env) == 0) {
        x = 42;
        handler();
    } else {
        printf("x = %d\n", x);  // guaranteed to be 42
    }
    return 0;
}
```

### Always check setjmp return value

```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf env;

int safe_operation(void) {
    if (setjmp(env) != 0) {
        fprintf(stderr, "Error recovered\n");
        return -1;
    }
    // normal path
    return 0;
}
```

### Use setjmp for structured error recovery

```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf env;

typedef enum { ERR_NONE, ERR_IO, ERR_MEM } Error;

Error try_operation(void) {
    if (setjmp(env) != 0) return ERR_IO;
    // ... operation that may longjmp on error ...
    return ERR_NONE;
}

int main(void) {
    Error e = try_operation();
    if (e != ERR_NONE) printf("Error: %d\n", e);
    return 0;
}
```

### Avoid longjmp from signal handlers safely

```c
#include <setjmp.h>
#include <signal.h>

static jmp_buf env;

void handler(int sig) {
    longjmp(env, sig);
}

int main(void) {
    signal(SIGFPE, handler);
    if (setjmp(env) == 0) {
        int x = 1 / 0;  // triggers SIGFPE
    } else {
        printf("Caught signal\n");
    }
    return 0;
}
```

## Common Scenarios

### Scenario 1: Automatic variable lost after longjmp

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: longjmp to expired stack frame in returned-from function

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using longjmp across threads that created different setjmp

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Declare post-longjmp variables as volatile
- **Tip 2:** Never longjmp to a function that has already returned
- **Tip 3:** Use setjmp/longjmp sparingly -- prefer error codes or exceptions
