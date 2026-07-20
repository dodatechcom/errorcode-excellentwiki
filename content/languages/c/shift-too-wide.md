---
title: "[Solution] C SHIFT_TOO_WIDE — Shift count >= width of type UB"
description: "Fix C shift count too wide undefined behavior by checking shift amounts, using unsigned types, and masking shift values. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 823
---

# C SHIFT_TOO_WIDE — Shift count >= width of type UB

Shifting an integer by a number of bits greater than or equal to the width of the type is undefined behavior. For example, shifting a 32-bit `int` by 32 or more bits is UB. This applies to both left and right shifts.

## Common Causes

```c
// Cause 1: Shifting by the full width of the type
int x = 1;
int result = x << 32;  // UB: int is 32 bits, shift by 32
```

```c
// Cause 2: Right shift by full width
int x = 0x12345678;
int result = x >> 32;  // UB: same issue
```

```c
// Cause 3: Shift amount from untrusted input
int shift_by = read_user_input();
int result = 1 << shift_by;  // UB if shift_by >= 31 (or 32 for unsigned)
```

```c
// Cause 4: Shifting negative values
int x = -1;
int result = x << 1;  // UB: left-shifting negative values is UB in C
```

```c
// Cause 5: Shifting into or past the sign bit
int x = 1;
int result = x << 31;  // UB in C: result would be INT_MIN (negative)
// For 32-bit int: 1 << 31 sets the sign bit
```

## How to Fix

### Fix 1: Check shift amount before shifting

```c
#include <limits.h>
#include <stdint.h>

uint32_t safe_shift_left(uint32_t value, int shift) {
    if (shift < 0 || shift >= 32) {
        return 0;  // or handle error
    }
    return value << shift;
}

uint32_t safe_shift_right(uint32_t value, int shift) {
    if (shift < 0 || shift >= 32) {
        return 0;
    }
    return value >> shift;
}
```

### Fix 2: Use unsigned types for shifts

```c
#include <stdint.h>

uint32_t make_mask(int bit) {
    if (bit < 0 || bit >= 32) return 0;
    return (uint32_t)1 << bit;  // unsigned: well-defined even for bit=31
}
```

### Fix 3: Mask the shift amount to stay within bounds

```c
#include <stdint.h>

uint64_t shift_with_mask(uint64_t value, int shift) {
    // Mask shift to 0-63 range (for 64-bit types)
    return value << (shift & 63);
}
```

### Fix 4: Avoid left-shifting negative values

```c
// WRONG: left-shifting negative values
int x = -1;
int result = x << 1;  // UB

// CORRECT: use unsigned
unsigned int ux = (unsigned int)-1;
unsigned int result = ux << 1;  // well-defined: wraps modulo 2^32
```

### Fix 5: Use safe bit manipulation functions

```c
#include <stdint.h>
#include <stdbool.h>

bool set_bit(uint32_t *value, int bit) {
    if (bit < 0 || bit >= 32) return false;
    *value |= (uint32_t)1 << bit;
    return true;
}

bool clear_bit(uint32_t *value, int bit) {
    if (bit < 0 || bit >= 32) return false;
    *value &= ~((uint32_t)1 << bit);
    return true;
}

bool get_bit(uint32_t value, int bit) {
    if (bit < 0 || bit >= 32) return false;
    return (value >> bit) & 1;
}
```

## Examples

```c
// Real-world: safe bit field manipulation
#include <stdint.h>
#include <stdbool.h>

typedef struct {
    uint32_t flags;
} DeviceFlags;

#define FLAG_RESET    (1U << 0)
#define FLAG_ENABLE   (1U << 1)
#define FLAG_DEBUG    (1U << 2)
#define FLAG_VERBOSE  (1U << 3)

bool flag_set(DeviceFlags *dev, int bit) {
    if (bit < 0 || bit >= 32) return false;
    dev->flags |= (1U << (uint32_t)bit);
    return true;
}

bool flag_clear(DeviceFlags *dev, int bit) {
    if (bit < 0 || bit >= 32) return false;
    dev->flags &= ~(1U << (uint32_t)bit);
    return true;
}

// Usage:
DeviceFlags dev = {0};
flag_set(&dev, FLAG_ENABLE);
flag_set(&dev, FLAG_DEBUG);
printf("Flags: 0x%08x\n", dev.flags);
```

```c
// Real-world: endian-safe byte reading
#include <stdint.h>

uint32_t read_uint32_be(const uint8_t *buf) {
    return ((uint32_t)buf[0] << 24) |
           ((uint32_t)buf[1] << 16) |
           ((uint32_t)buf[2] << 8)  |
           ((uint32_t)buf[3]);
}

uint32_t read_uint32_le(const uint8_t *buf) {
    return ((uint32_t)buf[0])       |
           ((uint32_t)buf[1] << 8)  |
           ((uint32_t)buf[2] << 16) |
           ((uint32_t)buf[3] << 24);
}
```

## Related Errors

- [C SIGNED_INTEGER_OVERFLOW](/languages/c/signed-integer-overflow-ub) — Signed integer overflow UB
- [C DIVISION_OVERFLOW](/languages/c/division-overflow) — INT_MIN / -1 overflow
- [C CASTING_OUT_OF_RANGE](/languages/c/casting-out-of-range) — Casting out of range value
