---
title: "[Solution] C Pointer Comparison Error — How to Fix"
description: "Fix C pointer comparison undefined behavior including comparing pointers from different objects and invalid NULL checks."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Pointer Comparison Error — How to Fix

Comparing pointers in C is only defined when both pointers point to elements of the same array or one past the end. Comparing pointers from different allocations, comparing function pointers incorrectly, or comparing pointers with integers (other than NULL) results in undefined behavior.

## Common Error Messages

- `Undefined behavior from comparing pointers to different objects`
- `Pointer comparison with integer — incompatible types`
- `Comparing function pointers gives unexpected results`
- `Invalid pointer comparison across allocations`

## How to Fix It

### Only compare pointers within the same array

```c
#include <stdio.h>

int main(void) {
    int arr[5] = {10, 20, 30, 40, 50};
    int *p = &arr[1];
    int *q = &arr[3];
    if (p < q) printf("p comes before q\n");
    if (p == &arr[1]) printf("p points to arr[1]\n");
    return 0;
}
```

### Use NULL for null pointer comparison

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int));
    if (p != NULL) {
        *p = 42;
        printf("Value: %d\n", *p);
    }
    free(p);
    p = NULL;
    if (p == NULL) printf("p is NULL\n");
    return 0;
}
```

### Compare function pointers with == only

```c
#include <stdio.h>

void func_a(void) { printf("A\n"); }
void func_b(void) { printf("B\n"); }

int main(void) {
    void (*pa)(void) = func_a;
    void (*pb)(void) = func_b;
    if (pa == func_a) printf("pa is func_a\n");
    if (pa != pb) printf("pa is not pb\n");
    return 0;
}
```

### Use intptr_t for integer-pointer conversions

```c
#include <stdio.h>
#include <stdint.h>

int main(void) {
    int x = 42;
    int *p = &x;
    intptr_t addr = (intptr_t)p;
    printf("Address: 0x%lx\n", (unsigned long)addr);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Comparing pointers from two different malloc calls

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using > or < to compare function pointers instead of ==

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Casting an integer to a pointer and comparing with another pointer

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Only compare pointers within the same array or object
- **Tip 2:** Use == or != for function pointer comparisons, not relational operators
- **Tip 3:** Use intptr_t when you need to convert between pointers and integers
