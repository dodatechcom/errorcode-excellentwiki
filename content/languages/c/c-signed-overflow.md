---
title: "[Solution] C Signed Integer Overflow Error — How to Fix"
description: "Fix C signed integer overflow undefined behavior with bounds checking in arithmetic operations."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Signed Integer Overflow Error — How to Fix

Signed integer overflow is undefined behavior in C. Results may wrap, trap, or be optimized away. Common causes include unbounded arithmetic, unchecked size calculations, and incrementing past INT_MAX.

## Common Error Messages

- `undefined behavior: signed integer overflow`
- `runtime error: signed integer overflow`
- `SUM: signed integer overflow`
- `negation of minimum value of signed int`

## How to Fix It

### Check for overflow before arithmetic

```c
#include <limits.h>

int safe_add(int a, int b) {
    if ((b > 0 && a > INT_MAX - b) || (b < 0 && a < INT_MIN - b))
        return 0;
    return a + b;
}
```

### Use unsigned for size calculations

```c
#include <stddef.h>
size_t count = 1000;
size_t elem_size = sizeof(int);
if (count > SIZE_MAX / elem_size) { /* overflow */ }
```

### Use wider intermediate types

```c
#include <stdint.h>
int32_t a = 2000000000;
int32_t b = 2000000000;
int64_t result = (int64_t)a + (int64_t)b;
```

### Enable UB Sanitizer

```bash
gcc -fsanitize=undefined -g -o program program.c
```

## Common Scenarios

### Scenario 1: Multiplying large integers for size calculation wraps to small value

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Loop counter past INT_MAX causes UB

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Negating INT_MIN which has no positive counterpart

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Check overflow before every arithmetic operation
- **Tip 2:** Use size_t for size calculations
- **Tip 3:** Compile with -fsanitize=undefined
