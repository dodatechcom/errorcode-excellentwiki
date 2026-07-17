---
title: "[Solution] C Floating point exception: division by zero"
description: "Fix C floating point exception from division by zero. Prevent division by zero errors."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["division-by-zero", "fpe", "floating-point", "sigfpe", "arithmetic"]
weight: 5
---

# Floating point exception: division by zero

Division by zero for integers causes a `SIGFPE` signal (Floating Point Exception). For floating-point numbers, it produces infinity or NaN rather than crashing, but integer division by zero terminates the program.

## Common Causes

```c
// Cause 1: Integer division by zero
int a = 10;
int b = 0;
int c = a / b; // SIGFPE

// Cause 2: Modulo by zero
int x = 5 % 0; // SIGFPE

// Cause 3: Uninitialized divisor
int divisor;
int result = 100 / divisor; // may be zero
```

## How to Fix

### Fix 1: Check before dividing

```c
if (divisor != 0) {
    result = a / divisor;
} else {
    fprintf(stderr, "Cannot divide by zero\n");
}
```

### Fix 2: Use safe division function

```c
int safe_div(int a, int b, int *result) {
    if (b == 0) return -1;
    *result = a / b;
    return 0;
}
```

### Fix 3: Use floating-point for flexibility

```c
double a = 10.0;
double b = 0.0;
double c = a / b; // produces +inf, no crash
```

## Examples

```c
#include <stdio.h>

int safe_divide(int a, int b, int *result) {
    if (b == 0) {
        fprintf(stderr, "Error: division by zero\n");
        return -1;
    }
    *result = a / b;
    return 0;
}

int main(void) {
    int result;
    if (safe_divide(10, 0, &result) == 0) {
        printf("Result: %d\n", result);
    }
    return 0;
}
```

## Related Errors

- [Integer overflow]({{< relref "/languages/c/integer-overflow" >}}) — arithmetic overflow.
- [Invalid argument]({{< relref "/languages/c/invalid-argument" >}}) — EINVAL error.
- [Segmentation fault]({{< relref "/languages/c/segmentation-fault-null" >}}) — null pointer crash.
