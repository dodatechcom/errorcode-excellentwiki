---
title: "[Solution] C errno 34 ERANGE — Math result not representable"
description: "Fix C errno 34 ERANGE (Math result not representable) by checking for overflow/underflow and using appropriate data types."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["erange", "errno-34", "math", "range", "overflow", "underflow"]
weight: 5
---

# [Solution] C errno 34 ERANGE — Math result not representable

Math result not representable occurs when a system call fails and sets `errno` to 34. This error indicates that the requested operation cannot be performed due to the specific condition described by ERANGE.

## Common Causes

- Result of a math function is too large to represent (overflow).
- Result is too small to represent as a non-zero value (underflow).
- Using exp() with a very large argument.
- Using pow() with arguments that produce huge results.

## How to Fix

```c
#include <math.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    errno = 0;
    double result = exp(1000.0);
    if (errno == ERANGE) {
        fprintf(stderr, "exp(1000) overflow: %s (errno %d)\n", strerror(errno), errno);
    }
    return 0;
}
```

## Examples

```c
#include <math.h>
#include <stdio.h>
#include <float.h>

int main(void) {
    double x = 1000.0;
    if (x > DBL_MAX_EXP) {
        fprintf(stderr, "exp(%f) will overflow\n", x);
    } else {
        double result = exp(x);
        printf("exp(%f) = %f\n", x, result);
    }
    return 0;
}
```

## Related Errors

- [errno-33 EDOM]({{< relref "/languages/c/errno-33" >}}) — math argument out of domain.
- [errno-34 ERANGE]({{< relref "/languages/c/errno-34" >}}) — math result not representable (self).
- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
