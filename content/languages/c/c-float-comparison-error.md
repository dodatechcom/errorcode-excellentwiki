---
title: "[Solution] C Float Comparison Error — How to Fix"
description: "Fix C floating-point comparison errors from direct equality checks. Use epsilon-based comparison."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Float Comparison Error — How to Fix

Direct equality comparison of floats is unreliable due to rounding errors. 0.1 + 0.2 != 0.3 in IEEE 754. Common mistakes include == on floats, fixed epsilon without considering magnitude, and exact equality after calculations.

## Common Error Messages

- `Float comparison fails -- rounding error`
- `0.1 + 0.2 != 0.3 -- IEEE 754 issue`
- `Direct float equality gives false`
- `Float == produces wrong result`

## How to Fix It

### Use epsilon-based comparison

```c
#include <math.h>
#include <stdbool.h>
bool float_equal(float a, float b, float eps) {
    return fabsf(a - b) <= eps;
}
// Usage: float_equal(0.1f + 0.2f, 0.3f, 1e-6f)
```

### Use relative epsilon for large values

```c
#include <math.h>
#include <stdbool.h>
bool float_close(float a, float b, float rel) {
    float diff = fabsf(a - b);
    float largest = fmaxf(fabsf(a), fabsf(b));
    return diff <= largest * rel;
}
```

### Compare using ULP

```c
#include <stdint.h>
#include <string.h>
int float_to_bits(float f) { int b; memcpy(&b, &f, sizeof(b)); return b; }
bool within_ulp(float a, float b, int max) {
    return abs(float_to_bits(a) - float_to_bits(b)) <= max;
}
```

### Check for NaN separately

```c
#include <math.h>
float x = 0.0f / 0.0f;
if (isnan(x)) printf("x is NaN\n");
printf("NaN==NaN: %s\n", (x == x) ? "true" : "false");
```

## Common Scenarios

### Scenario 1: Direct == comparison of 0.1f+0.2f with 0.3f returns false

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Float after division gives wrong precision

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Comparing NaN with any value including itself

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Never use == for float comparison -- use epsilon
- **Tip 2:** Choose epsilon relative to magnitude
- **Tip 3:** Remember NaN != NaN -- check isnan() first
