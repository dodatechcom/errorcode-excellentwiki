---
title: "[Solution] C Implicit Conversion Error — How to Fix"
description: "Fix C implicit conversion errors that silently truncate data or change signedness."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Implicit Conversion Error — How to Fix

C performs implicit conversions between integer types, silently truncating, changing signedness, or producing unexpected results. Common issues include long-to-int truncation and signed/unsigned mixing.

## Common Error Messages

- `Implicit conversion loses integer precision`
- `Conversion from signed to unsigned changes sign`
- `Truncation of constant value`
- `Implicit declaration of function`

## How to Fix It

### Use explicit casts for narrowing

```c
#include <stdint.h>
int64_t big = 0x1FFFFFFFF;
int32_t narrow = (int32_t)big;
printf("int64: %ld -> int32: %d\n", (long)big, narrow);
```

### Use correct types for API params

```c
size_t len = 10;
int n = (int)len;
printf("n=%d\n", n);
```

### Enable conversion warnings

```bash
gcc -Wall -Wconversion -o program program.c
```

### Use proper printf format specifiers

```c
#include <stdint.h>
int32_t i = 42;
uint32_t u = 42;
int64_t l = 42;
printf("int32: %d uint32: %u int64: %ld\n", i, u, (long)l);
```

## Common Scenarios

### Scenario 1: Assigning 64-bit value to 32-bit variable silently truncates

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Passing signed int where unsigned expected

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Implicit function declaration from missing header

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Compile with -Wconversion for conversion warnings
- **Tip 2:** Use explicit casts to document intentional conversions
- **Tip 3:** Match printf format specifiers to argument types
