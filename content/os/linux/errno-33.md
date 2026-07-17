---
title: "[Solution] Linux EDOM (errno 33) — Math Argument Out of Domain Fix"
description: "Fix Linux EDOM (errno 33) Math argument out of domain of func error. Solutions for math function domain issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EDOM (errno 33) — Math Argument Out of Domain of Function

EDOM (errno 33) means a mathematical function received an argument outside its domain of definition. This error occurs when you pass an invalid input to a math function, such as a negative number to `sqrt()` or a value outside [-1, 1] to `asin()`. It is distinct from ERANGE (errno 34) because EDOM indicates the input is invalid, while ERANGE indicates the result is too large to represent.

## Common Causes

- Passing a negative number to `sqrt()`, `log()`, or similar functions
- Using values outside [-1, 1] for `asin()`, `acos()`, or `atanh()`
- Dividing zero by zero in floating-point arithmetic
- Using `errno` to detect math errors without checking the return value

## How to Fix EDOM

### 1. Validate Input Before Math Operations

Check that arguments are within the valid domain:

```c
#include <math.h>

double safe_sqrt(double x) {
    if (x < 0) {
        errno = EDOM;
        return NAN;
    }
    return sqrt(x);
}
```

### 2. Use Error-Bounding Functions

Many math functions set `errno` and return specific values:

```c
errno = 0;
double result = sqrt(-1.0);
if (errno == EDOM) {
    fprintf(stderr, "Error: domain error\n");
}
```

### 3. Check Return Values for NaN

Detect domain errors by checking for NaN:

```c
double result = asin(2.0);
if (isnan(result)) {
    fprintf(stderr, "Error: input out of domain\n");
}
```

### 4. Use Conditional Logic

Guard against invalid inputs before calling math functions:

```bash
# In a shell script
if [ $(echo "$value < 0" | bc) -eq 1 ]; then
    echo "Error: negative value for sqrt"
fi
```

## Verification

After adding input validation, confirm no EDOM errors occur:

```bash
strace -e trace=write ./program 2>&1 | grep EDOM
```

## Related Error Codes

- [ERANGE (errno 34)](/os/linux/errno-34/) — Math result not representable
- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [ERANGE (errno 34)](/os/linux/errno-34/) — Result out of range
