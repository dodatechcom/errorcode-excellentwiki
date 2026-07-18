---
title: "[Solution] C Bit Shift Overflow Error — How to Fix"
description: "Fix C bit shift undefined behavior from shifting by too many bits or negative amounts."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Bit Shift Overflow Error — How to Fix

Bit shifting is undefined when shift amount is negative, >= type width, or left-shifting into sign bit. Common mistakes include variable shifts without bounds checking and shifting signed values.

## Common Error Messages

- `undefined behavior: shift exponent is negative`
- `undefined behavior: shift exponent too large`
- `shift overflow: left shift into sign bit`
- `shift exponent overflow`

## How to Fix It

### Validate shift amount

```c
#include <stdint.h>
uint32_t value = 1;
int shift = 31;
if (shift >= 0 && shift < 32)
    printf("Result: %u\n", value << shift);
```

### Use safe shift functions

```c
#include <stdint.h>
#include <stdbool.h>
bool safe_left_shift(uint32_t v, int s, uint32_t *r) {
    if (s < 0 || s >= 32) return false;
    if (v > (UINT32_MAX >> s)) return false;
    *r = v << s;
    return true;
}
```

### Use unsigned for bitwise ops

```c
#include <stdint.h>
uint32_t val = 0xFFFFFFFF;
printf("Shifted: 0x%08X\n", val >> 4);
printf("1<<31: 0x%08X\n", 1U << 31);
```

### Enable shift checking

```bash
gcc -fsanitize=undefined -g -o program program.c
```

## Common Scenarios

### Scenario 1: Left shifting 1 by 31 on signed int enters sign bit

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Variable shift from user input exceeds type width

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Right shifting negative signed value has implementation-defined result

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Validate shift amount is between 0 and width-1
- **Tip 2:** Use unsigned types for bitwise operations
- **Tip 3:** Compile with -fsanitize=undefined
