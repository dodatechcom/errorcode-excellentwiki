---
title: "[Solution] C errno 33 EDOM — Math argument out of domain"
description: "Fix C errno 33 EDOM (Math argument out of domain) by validating input before calling math functions like sqrt, log, or asin."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["edom", "errno-33", "math", "domain", "out-of-domain"]
weight: 5
---

# [Solution] C errno 33 EDOM — Math argument out of domain

Math argument out of domain occurs when a system call fails and sets `errno` to 33. This error indicates that the requested operation cannot be performed due to the specific condition described by EDOM.

## Common Causes

- Passing a negative number to sqrt().
- Passing a number ≤ 0 to log().
- Passing a value outside [-1, 1] to asin() or acos().
- Using math functions with invalid arguments.

## How to Fix

```c
#include <math.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    double result = sqrt(-1.0);
    if (errno == EDOM) {
        fprintf(stderr, "sqrt failed: %s (errno %d)\n", strerror(errno), errno);
    }
    return 0;
}
```

## Examples

```c
#include <math.h>
#include <stdio.h>

int main(void) {
    double x = -1.0;
    if (x < 0) {
        fprintf(stderr, "Cannot compute sqrt of negative number\n");
    } else {
        double result = sqrt(x);
        printf("sqrt(%f) = %f\n", x, result);
    }
    return 0;
}
```

## Related Errors

- [errno-34 ERANGE]({{< relref "/languages/c/errno-34" >}}) — math result not representable.
- [errno-33 EDOM]({{< relref "/languages/c/errno-33" >}}) — math argument out of domain (self).
- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
