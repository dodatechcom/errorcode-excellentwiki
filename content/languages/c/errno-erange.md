---
title: "[Solution] C errno ERANGE — Math result not representable Fix"
description: "Fix C ERANGE (Math result not representable) by handling overflow and underflow in math functions and strtod."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ERANGE — Math result not representable Fix

When a math function produces a result that is too large (overflow) or too close to zero (underflow) to be represented as a `double`, the function sets `errno` to `ERANGE`. This also applies to string-to-number conversions like `strtod()` and `strtol()`.

## Common Causes

- `exp()` overflows for large arguments (result exceeds `DBL_MAX`).
- `pow()` produces values too large to represent.
- `strtod()` or `strtol()` encounters a number outside the representable range.
- Small results underflow to zero when `errno` is set to `ERANGE`.

## How to Fix

Check `errno` after math functions and string conversions. Use `math_errhandling` to detect errors.

```c
#include <math.h>
#include <stdio.h>
#include <errno.h>
#include <float.h>
#include <string.h>

int main(void) {
    errno = 0;
    double result = exp(1000.0);
    if (errno == ERANGE) {
        fprintf(stderr, "exp(1000): overflow — result is infinity\n");
        fprintf(stderr, "Result: %f\n", result);  // inf
    }

    errno = 0;
    result = strtod("1e999", NULL);
    if (errno == ERANGE) {
        fprintf(stderr, "strtod overflow: %s\n", strerror(errno));
    }
    return 0;
}
```

## Examples

Overflow in `exp()`:

```c
#include <math.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    errno = 0;
    double result = exp(1000.0);
    if (errno == ERANGE) {
        fprintf(stderr, "exp(1000): ERANGE — result not representable\n");
    }
    return 0;
}
```

String-to-number conversion overflow:

```c
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char *endptr;
    errno = 0;
    long val = strtol("99999999999999999999", &endptr, 10);
    if (errno == ERANGE) {
        fprintf(stderr, "strtol: value out of range (errno %d)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-34 ERANGE]({{< relref "/languages/c/errno-erange" >}}) — math result not representable (numeric).
- [errno-33 EDOM]({{< relref "/languages/c/errno-edom" >}}) — math argument out of domain.
- [errno-22 EINVAL](/languages/c/errno-erange/) — invalid argument.
