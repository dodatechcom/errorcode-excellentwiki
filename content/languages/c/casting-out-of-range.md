---
title: "[Solution] C CASTING_OUT_OF_RANGE — Casting out of range value UB"
description: "Fix C casting out of range undefined behavior by checking ranges, avoiding narrowing casts, and using safe conversion functions. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 825
---

# C CASTING_OUT_OF_RANGE — Casting out of range value UB

Casting a value to a type that cannot represent it results in undefined behavior (for signed types) or implementation-defined truncation (for unsigned types). This commonly happens with narrowing casts, casting large integers to smaller types, or casting floating-point values to integers outside the representable range.

## Common Causes

```c
// Cause 1: Casting large int to small int
int big = 1000;
char small = (char)big;  // if char is 8-bit: implementation-defined or UB
```

```c
// Cause 2: Casting negative value to unsigned
int negative = -1;
unsigned int positive = (unsigned int)negative;  // well-defined in C (wraps), but often unintentional
```

```c
// Cause 3: Casting float out of int range
#include <float.h>
float huge = 1e30f;
int i = (int)huge;  // undefined behavior: value doesn't fit in int
```

```c
// Cause 4: Casting pointer to smaller integer type
void *ptr = malloc(100);
int id = (int)(uintptr_t)ptr;  // if int is 32-bit and pointer is 64-bit, truncation
```

```c
// Cause 5: Signed/unsigned comparison leading to bad cast
int idx = -1;
unsigned int uidx = (unsigned int)idx;  // wraps to 4294967295
if (uidx < array_size) {  // unexpected: 4294967295 is likely >= array_size
    // this block executes unexpectedly
}
```

## How to Fix

### Fix 1: Check range before casting

```c
#include <limits.h>

int safe_char_cast(int value) {
    if (value < CHAR_MIN || value > CHAR_MAX) {
        return CHAR_MAX;  // or handle error
    }
    return (char)value;
}

long safe_int_cast(long value) {
    if (value < INT_MIN || value > INT_MAX) {
        return INT_MAX;  // or handle error
    }
    return (int)value;
}
```

### Fix 2: Use safe conversion with range checking

```c
#include <limits.h>
#include <stdbool.h>
#include <stdint.h>

bool int_to_short(int value, int16_t *result) {
    if (value < INT16_MIN || value > INT16_MAX) {
        return false;
    }
    *result = (int16_t)value;
    return true;
}

bool long_to_int(long value, int *result) {
    if (value < INT_MIN || value > INT_MAX) {
        return false;
    }
    *result = (int)value;
    return true;
}
```

### Fix 3: Use wider types or unsigned types appropriately

```c
#include <stdint.h>

// Use the right-sized type for the data
uint8_t  pixel = (uint8_t)clamp(value, 0, 255);    // for 8-bit values
uint16_t sample = (uint16_t)clamp(value, 0, 65535); // for 16-bit values
uint32_t color = (uint32_t)value;                    // for 32-bit values
```

### Fix 4: Validate before narrowing conversions

```c
#include <stdint.h>

int32_t read_network_int(const uint8_t *buf) {
    uint32_t val = ((uint32_t)buf[0] << 24) |
                   ((uint32_t)buf[1] << 16) |
                   ((uint32_t)buf[2] << 8)  |
                   ((uint32_t)buf[3]);
    return (int32_t)val;  // well-defined: reinterpretation of bit pattern
}

// Safe narrowing from uint64_t to uint32_t
uint32_t safe_narrow(uint64_t value) {
    if (value > UINT32_MAX) return UINT32_MAX;
    return (uint32_t)value;
}
```

### Fix 5: Handle float-to-integer conversion safely

```c
#include <float.h>
#include <math.h>
#include <limits.h>

int safe_float_to_int(double value) {
    if (isnan(value) || isinf(value)) return 0;
    if (value > (double)INT_MAX) return INT_MAX;
    if (value < (double)INT_MIN) return INT_MIN;
    return (int)value;
}
```

## Examples

```c
// Real-world: parsing integers from strings with range checking
#include <stdlib.h>
#include <limits.h>
#include <errno.h>

int parse_int(const char *str) {
    long val = strtol(str, NULL, 10);
    if (errno == ERANGE || val < INT_MIN || val > INT_MAX) {
        return -1;  // or INT_MIN/INT_MAX as sentinel
    }
    return (int)val;
}

// Usage:
int x = parse_int("2147483647");   // 2147483647 (INT_MAX)
int y = parse_int("2147483648");   // -1 (overflow)
int z = parse_int("not_a_number"); // -1 (parsing error)
```

```c
// Real-world: safe type conversion for array indices
#include <stddef.h>
#include <stdint.h>

int safe_index(size_t index) {
    if (index > (size_t)INT_MAX) return -1;
    return (int)index;
}

// For size_t to int (POSIX-like)
#include <sys/types.h>
ssize_t safe_ssize(size_t value) {
    if (value > (size_t)SSIZE_MAX) return SSIZE_MAX;
    return (ssize_t)value;
}
```

## Related Errors

- [C SIGNED_INTEGER_OVERFLOW](/languages/c/signed-integer-overflow-ub) — Signed integer overflow UB
- [C SHIFT_TOO_WIDE](/languages/c/shift-too-wide) — Shift count >= width of type
- [C DIVISION_OVERFLOW](/languages/c/division-overflow) — INT_MIN / -1 overflow
