---
title: "[Solution] C Division by Zero Error — How to Fix"
description: "Fix C division by zero errors causing floating-point exceptions or undefined behavior."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Division by Zero Error — How to Fix

Division by zero is undefined for integers (crash/SIGFPE) and produces infinity/NaN for floats. Common causes include unchecked user input, uninitialized denominators, and missing zero checks.

## Common Error Messages

- `Floating point exception (core dumped)`
- `SIGFPE -- arithmetic exception`
- `Division by zero -- undefined behavior`
- `runtime error: division by zero`

## How to Fix It

### Check divisor before dividing

```c
#include <stdio.h>
int safe_divide(int a, int b, int *r) {
    if (b == 0) return -1;
    *r = a / b;
    return 0;
}
```

### Safe floating-point division

```c
#include <math.h>
double a = 10.0, b = 0.0;
if (fabs(b) < 1e-10) fprintf(stderr, "Too close to zero\n");
else printf("Result: %f\n", a / b);
```

### Handle NaN and infinity

```c
#include <math.h>
double r = 1.0 / 0.0;
if (isinf(r)) printf("infinity\n");
r = 0.0 / 0.0;
if (isnan(r)) printf("NaN\n");
```

### Enable FPE trapping

```c
#include <fenv.h>
feenableexcept(FE_DIVBYZERO | FE_INVALID);
```

## Common Scenarios

### Scenario 1: User supplies zero as denominator and program crashes

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Function returns 0 and caller divides without checking

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Integer division by zero in embedded systems causes trap

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check divisor for zero
- **Tip 2:** Use epsilon for float denominators
- **Tip 3:** Enable feenableexcept to catch issues early
