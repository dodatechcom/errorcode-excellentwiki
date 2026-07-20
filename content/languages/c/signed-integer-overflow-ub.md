---
title: "[Solution] C SIGNED_INTEGER_OVERFLOW — Signed integer overflow UB"
description: "Fix C signed integer overflow undefined behavior by checking for overflow, using unsigned integers, or using -fwrapv. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 818
---

# C SIGNED_INTEGER_OVERFLOW — Signed integer overflow UB

Signed integer overflow is undefined behavior in C. When a signed integer operation produces a value that cannot be represented in the result type, the program behavior is completely unpredictable. GCC can optimize based on the assumption that signed overflow never occurs.

## Common Causes

```c
// Cause 1: Addition overflow
int a = INT_MAX;  // 2147483647
int b = 1;
int sum = a + b;  // undefined behavior: signed overflow
```

```c
// Cause 2: Multiplication overflow
int x = 100000;
int y = 100000;
int product = x * y;  // undefined: 10,000,000,000 doesn't fit in int
```

```c
// Cause 3: Negating INT_MIN
int x = INT_MIN;  // -2147483648
int neg = -x;     // undefined: 2147483648 doesn't fit in int
```

```c
// Cause 4: Abs of INT_MIN
int x = INT_MIN;
int a = abs(x);   // undefined behavior: abs(INT_MIN) overflows
```

```c
// Cause 5: Left shift causing overflow
int x = 1;
int result = x << 31;  // undefined if int is 32-bit (result would be negative)
```

## How to Fix

### Fix 1: Check for overflow before performing the operation

```c
#include <limits.h>

int safe_add(int a, int b) {
    if ((b > 0 && a > INT_MAX - b) ||
        (b < 0 && a < INT_MIN - b)) {
        // overflow would occur
        return INT_MAX; // or handle error
    }
    return a + b;
}

int safe_mul(int a, int b) {
    if (a > 0 && b > 0 && a > INT_MAX / b) return INT_MAX;
    if (a > 0 && b < 0 && b < INT_MIN / a) return INT_MIN;
    if (a < 0 && b > 0 && a < INT_MIN / b) return INT_MIN;
    if (a < 0 && b < 0 && a < INT_MAX / b) return INT_MAX;
    return a * b;
}
```

### Fix 2: Use unsigned integers for arithmetic that may overflow

```c
#include <stdint.h>

uint32_t a = UINT32_MAX;  // 4294967295
uint32_t b = 1;
uint32_t sum = a + b;     // well-defined: wraps to 0
// Note: unsigned overflow is well-defined (modular arithmetic)
```

### Fix 3: Use wider integer types to prevent overflow

```c
#include <stdint.h>

int32_t a = 100000;
int32_t b = 100000;
int64_t product = (int64_t)a * b;  // no overflow in 64-bit
```

### Fix 4: Use -fwrapv for signed overflow wrapping (GCC/Clang extension)

```bash
# Compile with wrapping semantics for signed integers
gcc -fwrapv main.c -o app
# Now signed overflow wraps around like unsigned (but less optimizable)
```

### Fix 5: Use safe integer libraries

```c
#include <stdbool.h>
#include <limits.h>

bool add_overflow_int(int a, int b, int *result) {
    if (b > 0 && a > INT_MAX - b) return false;
    if (b < 0 && a < INT_MIN - b) return false;
    *result = a + b;
    return true;
}

// Usage:
int result;
if (!add_overflow_int(a, b, &result)) {
    // handle overflow error
}
```

## Examples

```c
// Real-world: timestamp calculation that can overflow
#include <stdint.h>
#include <time.h>
#include <stdbool.h>

bool timestamp_add_seconds(time_t base, int64_t seconds, time_t *result) {
    // Check for overflow before adding
    if (seconds > 0 && base > INT64_MAX - seconds) return false;
    if (seconds < 0 && base < INT64_MIN - seconds) return false;
    *result = base + seconds;
    return true;
}

// Usage:
time_t now = time(NULL);
time_t future;
if (timestamp_add_seconds(now, 3600, &future)) {
    printf("One hour from now: %ld\n", (long)future);
} else {
    printf("Timestamp overflow!\n");
}
```

```c
// Real-world: size calculation that may overflow
#include <stddef.h>
#include <stdlib.h>
#include <stdbool.h>

void* safe_calloc(size_t count, size_t size) {
    // Check for multiplication overflow
    if (count > 0 && size > SIZE_MAX / count) return NULL;
    return calloc(count, size);
}
```

## Related Errors

- [C SHIFT_TOO_WIDE](/languages/c/shift-too-wide) — Shift count >= width of type
- [C DIVISION_OVERFLOW](/languages/c/division-overflow) — INT_MIN / -1 overflow
- [C CASTING_OUT_OF_RANGE](/languages/c/casting-out-of-range) — Casting out of range value
