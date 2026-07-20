---
title: "[Solution] C SIGFPE — Floating point exception handling"
description: "Fix and handle SIGFPE floating point exceptions by checking division, using signal handling, and enabling -fexceptions. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 827
---

# C SIGFPE — Floating point exception handling

SIGFPE (Floating Point Exception) is delivered on integer divide-by-zero or other arithmetic exceptions. Despite its name, it covers integer operations too. On most platforms, a divide-by-zero integer operation triggers SIGFPE rather than producing a defined result.

## Common Causes

```c
// Cause 1: Integer division by zero
int a = 10;
int b = 0;
int result = a / b;  // SIGFPE: integer divide by zero
```

```c
// Cause 2: Integer modulo by zero
int a = 10;
int b = 0;
int result = a % b;  // SIGFPE
```

```c
// Cause 3: Floating-point exception from invalid operation
#include <math.h>
double x = -1.0;
double y = sqrt(x);  // domain error — may raise SIGFPE on some platforms
```

```c
// Cause 4: Overflow in integer division (INT_MIN / -1)
#include <limits.h>
int a = INT_MIN;
int b = -1;
int result = a / b;  // UB / SIGFPE on many platforms
```

```c
// Cause 5: Floating-point divide by zero (may not raise SIGFPE on IEEE 754)
double x = 1.0;
double y = 0.0;
double result = x / y;  // returns +Inf on IEEE 754 systems — not SIGFPE
```

## How to Fix

### Fix 1: Check for zero before integer division

```c
int safe_div(int a, int b) {
    if (b == 0) {
        // Handle error: return sentinel, print error, etc.
        return 0;
    }
    return a / b;
}

int safe_mod(int a, int b) {
    if (b == 0) return 0;
    return a % b;
}
```

### Fix 2: Install a SIGFPE handler for graceful recovery

```c
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

static volatile sig_atomic_t fpe_count = 0;

void sigfpe_handler(int sig) {
    (void)sig;
    fpe_count++;
    // Note: after returning from handler, the faulting instruction
    // may be retried — use longjmp to recover, or set a flag
}

int main(void) {
    struct sigaction sa;
    sa.sa_handler = sigfpe_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;  // Do NOT use SA_RESETHAND for SIGFPE
    sigaction(SIGFPE, &sa, NULL);

    int a = 10, b = 0;
    if (b != 0) {
        printf("%d\n", a / b);
    } else {
        printf("Division by zero prevented\n");
    }
    return 0;
}
```

### Fix 3: Use signal-safe recovery with longjmp

```c
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;
static volatile sig_atomic_t can_jump = 0;

void sigfpe_handler(int sig) {
    (void)sig;
    if (can_jump) {
        can_jump = 0;
        siglongjmp(jump_buffer, 1);  // jump back to set point
    }
}

int safe_div_with_recovery(int a, int b) {
    if (b == 0) return 0;

    struct sigaction sa, old_sa;
    sa.sa_handler = sigfpe_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGFPE, &sa, &old_sa);

    can_jump = 1;
    if (sigsetjmp(jump_buffer, 1) == 0) {
        int result = a / b;
        sigaction(SIGFPE, &old_sa, NULL);
        can_jump = 0;
        return result;
    } else {
        sigaction(SIGFPE, &old_sa, NULL);
        can_jump = 0;
        return 0;  // recovered from SIGFPE
    }
}
```

### Fix 4: Check for INT_MIN / -1 separately

```c
#include <limits.h>

int safe_div_edge_cases(int a, int b) {
    if (b == 0) return 0;
    if (a == INT_MIN && b == -1) return INT_MAX;
    return a / b;
}
```

### Fix 5: Use floating-point exceptions properly (FE exceptions)

```c
#include <fenv.h>
#include <stdio.h>

#pragma STDC FENV_ACCESS ON

int main(void) {
    feclearexcept(FE_ALL_EXCEPT);

    double x = 1.0 / 0.0;  // IEEE 754: returns Inf, may raise FE_DIVBYZERO

    if (fetestexcept(FE_DIVBYZERO)) {
        printf("Division by zero occurred\n");
    }

    return 0;
}
```

## Examples

```c
// Real-world: calculator app with safe division
#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

typedef struct {
    double value;
    bool error;
} CalcResult;

CalcResult calc_divide(double a, double b) {
    CalcResult r = {0.0, false};

    if (b == 0.0) {
        r.error = true;
        return r;
    }

    r.value = a / b;
    return r;
}

CalcResult calc_int_divide(int a, int b) {
    CalcResult r = {0.0, false};

    if (b == 0) {
        r.error = true;
        return r;
    }
    if (a == INT_MIN && b == -1) {
        r.error = true;
        return r;
    }

    r.value = (double)(a / b);
    return r;
}

// Usage:
CalcResult res = calc_int_divide(10, 3);
if (res.error) {
    printf("Error: division failed\n");
} else {
    printf("Result: %.2f\n", res.value);
}
```

```c
// Real-world: safe modulo for hash tables
#include <stdint.h>

int32_t safe_mod(int32_t numerator, int32_t denominator) {
    if (denominator == 0) return 0;
    if (numerator == INT32_MIN && denominator == -1) return 0;
    return numerator % denominator;
}

// Usage: hash table bucket index
size_t hash_to_index(int64_t hash, size_t table_size) {
    if (table_size == 0) return 0;
    int32_t mod_result = safe_mod((int32_t)hash, (int32_t)table_size);
    return (size_t)(mod_result >= 0 ? mod_result : mod_result + (int32_t)table_size);
}
```

## Related Errors

- [C DIVISION_OVERFLOW](/languages/c/division-overflow) — INT_MIN / -1 overflow UB
- [C SIGNED_INTEGER_OVERFLOW](/languages/c/signed-integer-overflow-ub) — Signed integer overflow UB
- [C SIGSEGV](/languages/c/sigsegv-handling) — Segmentation fault handling
