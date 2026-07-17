---
title: "[Solution] C errno EDOM — Math argument out of domain Fix"
description: "Fix C EDOM (Math argument out of domain) by validating inputs before calling math functions like sqrt, log, and asin."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EDOM — Math argument out of domain Fix

When a math function receives an argument outside its mathematical domain, the function returns an error indicator and sets `errno` to `EDOM`. For example, passing a negative number to `sqrt()` or a value greater than 1 to `asin()` triggers this error.

## Common Causes

- Passing a negative number to `sqrt()`, `log()` (for real-valued results), or `pow()` with fractional exponents.
- Passing a value outside [-1, 1] to `asin()`, `acos()`, or `atanh()`.
- Using `log()` with zero or negative arguments.
- Inadequate input validation before calling math functions.

## How to Fix

Validate inputs before calling math functions. Check the domain of the argument and handle edge cases.

```c
#include <math.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

double safe_sqrt(double x) {
    if (x < 0) {
        fprintf(stderr, "sqrt: domain error for %g\n", x);
        errno = EDOM;
        return NAN;
    }
    return sqrt(x);
}

int main(void) {
    double result = safe_sqrt(-4.0);
    if (isnan(result)) {
        fprintf(stderr, "Invalid input: sqrt of negative number\n");
    }
    return 0;
}
```

## Examples

Calling `sqrt()` with a negative number:

```c
#include <math.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    errno = 0;
    double result = sqrt(-1.0);
    if (errno == EDOM) {
        fprintf(stderr, "sqrt(-1): domain error (errno %d)\n", errno);
        fprintf(stderr, "Result: %f\n", result);  // NaN
    }
    return 0;
}
```

Calling `asin()` with a value outside [-1, 1]:

```c
#include <math.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    errno = 0;
    double result = asin(2.0);
    if (errno == EDOM) {
        fprintf(stderr, "asin(2.0): domain error (errno %d)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-33 EDOM](/languages/c/errno-edom/) — math argument out of domain (numeric).
- [errno-34 ERANGE]({{< relref "/languages/c/errno-erange" >}}) — math result not representable.
- [errno-22 EINVAL](/languages/c/errno-edom/) — invalid argument.
