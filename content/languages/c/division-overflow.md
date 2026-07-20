---
title: "[Solution] C DIVISION_OVERFLOW — INT_MIN / -1 overflow UB"
description: "Fix C division overflow undefined behavior by checking for INT_MIN, guarding division operations, and using safe division. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 822
---

# C DIVISION_OVERFLOW — INT_MIN / -1 overflow UB

In two's complement arithmetic, dividing `INT_MIN` by `-1` produces a result that cannot be represented in the type (the positive value is one greater than `INT_MAX`). This is undefined behavior in C and will crash on many platforms.

## Common Causes

```c
// Cause 1: Direct division without checking edge cases
int divide(int a, int b) {
    return a / b;  // UB if a == INT_MIN && b == -1
}
```

```c
// Cause 2: Negation of INT_MIN
int x = INT_MIN;
int result = -x;  // UB: -INT_MIN cannot be represented as int
```

```c
// Cause 3: Modulo with INT_MIN and -1
int x = INT_MIN;
int result = x % (-1);  // UB: same overflow issue
```

```c
// Cause 4: Division in expressions where values come from user input
int user_value = read_input();
int divisor = read_input();
int result = user_value / divisor;  // potential INT_MIN / -1
```

```c
// Cause 5: Signed overflow in division result
int a = -2147483648;  // INT_MIN
int b = -1;
int q = a / b;  // undefined behavior
int r = a % b;  // undefined behavior
```

## How to Fix

### Fix 1: Check for INT_MIN / -1 before dividing

```c
#include <limits.h>

int safe_div(int a, int b) {
    if (b == 0) return 0;  // or handle division by zero
    if (a == INT_MIN && b == -1) return INT_MAX;  // or handle overflow
    return a / b;
}

int safe_mod(int a, int b) {
    if (b == 0) return 0;
    if (a == INT_MIN && b == -1) return 0;  // overflow case
    return a % b;
}
```

### Fix 2: Use unsigned integers for division

```c
#include <stdint.h>

int32_t safe_div_unsigned(int32_t a, int32_t b) {
    if (b == 0) return 0;
    uint32_t ua = (uint32_t)a;
    uint32_t ub = (uint32_t)b;
    // INT_MIN / -1 in unsigned: 2147483648 / 4294967295 = 0
    return (int32_t)(ua / ub);
}
```

### Fix 3: Use wider types to detect overflow

```c
#include <stdint.h>

int64_t safe_div_wide(int32_t a, int32_t b) {
    if (b == 0) return 0;
    int64_t result = (int64_t)a / (int64_t)b;
    if (result > INT32_MAX || result < INT32_MIN) {
        return INT32_MAX;  // or handle overflow
    }
    return (int32_t)result;
}
```

### Fix 4: Guard with conditional before division

```c
#include <limits.h>

int divide_checked(int a, int b) {
    if (b == 0 || (a == INT_MIN && b == -1)) {
        // Handle error: return error code or use alternate computation
        return (b == 0) ? 0 : INT_MAX;
    }
    return a / b;
}
```

### Fix 5: Use -fwrapv to make signed overflow well-defined (GCC/Clang)

```bash
# Compile with wrapping semantics
gcc -fwrapv main.c -o app
# INT_MIN / -1 now wraps to INT_MIN (implementation-defined but not UB)
```

## Examples

```c
// Real-world: safe integer division library
#include <limits.h>
#include <stdbool.h>

typedef struct {
    int quotient;
    int remainder;
    bool overflow;
} DivResult;

DivResult int_div(int a, int b) {
    DivResult r = {0, 0, false};

    if (b == 0) {
        r.overflow = true;
        return r;
    }

    if (a == INT_MIN && b == -1) {
        r.overflow = true;
        return r;
    }

    r.quotient = a / b;
    r.remainder = a % b;
    return r;
}

// Usage:
DivResult result = int_div(INT_MIN, -1);
if (result.overflow) {
    printf("Division overflow!\n");
} else {
    printf("Quotient: %d, Remainder: %d\n", result.quotient, result.remainder);
}
```

```c
// Real-world: safe negation
#include <limits.h>

int safe_negate(int x) {
    if (x == INT_MIN) {
        return INT_MIN;  // or INT_MAX, or handle error
    }
    return -x;
}

// Check if negation would overflow
bool negation_would_overflow(int x) {
    return x == INT_MIN;
}
```

## Related Errors

- [C SIGNED_INTEGER_OVERFLOW](/languages/c/signed-integer-overflow-ub) — Signed integer overflow UB
- [C SHIFT_TOO_WIDE](/languages/c/shift-too-wide) — Shift count >= width of type
- [C CASTING_OUT_OF_RANGE](/languages/c/casting-out-of-range) — Casting out of range value
