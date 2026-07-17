---
title: "[Solution] C Integer overflow in signed arithmetic"
description: "Fix C integer overflow in signed arithmetic. Prevent undefined behavior from arithmetic overflow."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Integer overflow in signed arithmetic

Signed integer overflow is undefined behavior in C. The result can wrap around, produce incorrect values, or cause the compiler to make unexpected optimizations.

## Common Causes

```c
// Cause 1: Adding large values
int x = INT_MAX;
int y = x + 1; // overflow — undefined behavior

// Cause 2: Multiplication overflow
int a = 100000;
int b = 100000;
int c = a * b; // overflow

// Cause 3: Negative shift
int val = -1;
unsigned int shifted = val << 3; // undefined behavior
```

## How to Fix

### Fix 1: Check before operation

```c
#include <limits.h>

int safe_add(int a, int b) {
    if (a > 0 && b > INT_MAX - a) {
        fprintf(stderr, "overflow\n");
        return INT_MAX;
    }
    return a + b;
}
```

### Fix 2: Use unsigned types when possible

```c
unsigned int x = UINT_MAX;
unsigned int y = x + 1; // well-defined wrap
```

### Fix 3: Use compiler built-ins

```c
#include <stdint.h>

int32_t result;
if (__builtin_add_overflow(a, b, &result)) {
    fprintf(stderr, "overflow\n");
}
```

## Related Errors

- [Division by zero]({{< relref "/languages/c/division-by-zero-fpe" >}}) — floating point exception.
- [Null pointer dereference]({{< relref "/languages/c/null-pointer-dereference" >}}) — null pointer crash.
- [Out of memory]({{< relref "/languages/c/out-of-memory-malloc" >}}) — allocation failure.
