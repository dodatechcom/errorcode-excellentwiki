---
title: "[Solution] C Union Type Punning Error — How to Fix"
description: "Fix C union type punning undefined behavior in strict aliasing. Use memcpy or extensions for safe type punning."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Union Type Punning Error — How to Fix

Type punning through unions can cause undefined behavior under strict aliasing rules. Common mistakes include reading a union member that was not the last written, using union punning for floating-point bit manipulation across compilers, and strict aliasing violations causing miscompilation with optimization.

## Common Error Messages

- `Undefined behavior from union type punning with strict aliasing`
- `Compiler misoptimizes code using union type punning`
- `Floating-point bit manipulation through union is non-portable`
- `Strict aliasing violation from reading wrong union member`

## How to Fix It

### Use memcpy for well-defined type punning

```c
#include <stdio.h>
#include <string.h>
#include <stdint.h>

int main(void) {
    uint32_t bits = 0x3F800000;
    float f;
    memcpy(&f, &bits, sizeof(f));
    printf("bits=0x%08X -> float=%f\n", bits, f);
    return 0;
}
```

### Use union for C99/C11 type punning

```c
#include <stdio.h>
#include <stdint.h>

typedef union { uint32_t i; float f; } FloatPun;

int main(void) {
    FloatPun pun;
    pun.i = 0x3F800000;
    printf("float=%f\n", pun.f);
    pun.f = 2.0f;
    printf("bits=0x%08X\n", pun.i);
    return 0;
}
```

### Use compiler intrinsics

```c
#include <stdio.h>
#include <stdint.h>

int main(void) {
    float f = 3.14f;
    uint32_t bits;
    __builtin_memcpy(&bits, &f, sizeof(bits));
    printf("bits=0x%08X\n", bits);
    return 0;
}
```

### Compare floats using bit manipulation

```c
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

int float_bits_equal(float a, float b) {
    uint32_t ua, ub;
    memcpy(&ua, &a, sizeof(a));
    memcpy(&ub, &b, sizeof(b));
    return ua == ub;
}

int main(void) {
    float a = 0.1f + 0.2f;
    float b = 0.3f;
    printf("Exact equal: %s\n", float_bits_equal(a, b) ? "yes" : "no");
    return 0;
}
```

## Common Scenarios

### Scenario 1: Reading a union member that was not the last written — UB in C++

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using union type punning for floating-point manipulation non-portably

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Assuming union punning works identically with all optimization levels

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Use memcpy for type punning — it's portable and optimized by compilers
- **Tip 2:** In C99/C11 union type punning is defined, but avoid in C++
- **Tip 3:** For float comparison, use bit-level comparison with memcpy
