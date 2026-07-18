---
title: "[Solution] C Integer Promotion Error — How to Fix"
description: "Fix C integer promotion surprises in expressions. Understand implicit type promotion rules."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Integer Promotion Error — How to Fix

C automatically promotes smaller types (char, short) to int in expressions. This causes unexpected results when mixing signed/unsigned or comparing promoted values against larger types.

## Common Error Messages

- `Signed and unsigned comparison mismatch`
- `Implicit conversion changes signedness`
- `Integer promotion causes unexpected result`
- `char arithmetic produces wrong value`

## How to Fix It

### Explicitly cast to avoid surprises

```c
char a = 127;
char b = 1;
int result = a + b;  // promoted to int, result is 128
char c = (char)(a + b);  // overflow if char is 8-bit
printf("as int: %d\n", result);
```

### Be careful with signed/unsigned mixing

```c
int a = -1;
unsigned int b = 2;
if (a < 0 || (unsigned int)a < b)
    printf("a < b (correctly)\n");
```

### Use explicit types in boolean contexts

```c
char c = (char)0xFF;
if (c != 0) printf("nonzero\n");  // promoted to int(-1), true
```

### Use fixed-width types

```c
#include <stdint.h>
int8_t a = -1;
uint8_t b = 255;
printf("Sum as int: %d\n", (int)a + (int)b);
```

## Common Scenarios

### Scenario 1: Comparing int with unsigned where negatives wrap to huge positives

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: char arithmetic producing different results by signedness

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Bitwise ops on signed chars producing unexpected results

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Use explicit casts when mixing signed and unsigned
- **Tip 2:** Use fixed-width types when exact size matters
- **Tip 3:** Compile with -Wsign-conversion
