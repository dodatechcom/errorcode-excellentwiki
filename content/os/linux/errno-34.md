---
title: "[Solution] Linux ERANGE (errno 34) — Math Result Not Representable Fix"
description: "Fix Linux ERANGE (errno 34) Math result not representable error. Solutions for math overflow and range issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enRANGE", "math", "errno-34", "overflow"]
weight: 5
---

# Linux ERANGE (errno 34) — Math Result Not Representable

ERANGE (errno 34) means a mathematical function produced a result that is too large or too small to be represented as a finite floating-point number. This error occurs when the result overflows to infinity or underflows to zero. It is distinct from EDOM (errno 33) because ERANGE indicates the input is valid but the output exceeds the representable range.

## Common Causes

- Computing exponentials of very large numbers (e.g., `exp(1000)`)
- Taking the logarithm of a very small positive number
- Factorial or power functions producing values exceeding `DBL_MAX`
- Overflow in financial or scientific calculations

## How to Fix ERANGE

### 1. Check Return Value and errno

Detect range errors by checking both the return value and `errno`:

```c
#include <math.h>
#include <errno.h>

errno = 0;
double result = exp(1000);
if (errno == ERANGE) {
    fprintf(stderr, "Error: result out of range\n");
    if (isinf(result)) {
        fprintf(stderr, "Result overflowed to infinity\n");
    }
}
```

### 2. Use Scaled or Logarithmic Computation

Avoid overflow by using logarithmic math:

```c
// Instead of:
double result = exp(a + b);

// Use:
double result = exp(a) * exp(b);
```

### 3. Validate Input Ranges

Check input values before computation:

```c
if (x > 709) {  // exp(709) is near DBL_MAX
    fprintf(stderr, "Error: input too large for exp()\n");
    return -1;
}
```

### 4. Use Arbitrary-Precision Libraries

For computations requiring very large or very small results:

```bash
# Install GNU bc for arbitrary precision
sudo apt install bc
echo "scale=100; e(1000)" | bc -l
```

## Verification

After implementing range checks, confirm no ERANGE errors:

```bash
strace -e trace=write ./program 2>&1 | grep ERANGE
```

## Related Error Codes

- [EDOM (errno 33)](/os/linux/errno-33/) — Math argument out of domain of func
- [EOVERFLOW (errno 75)](/os/linux/errno-75/) — Value too large for defined data type
- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
