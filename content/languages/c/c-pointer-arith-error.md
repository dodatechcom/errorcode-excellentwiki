---
title: "[Solution] C Pointer Arithmetic Error — How to Fix"
description: "Fix C pointer arithmetic errors including out-of-bounds access, invalid pointer comparisons, and arithmetic on void*."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Pointer Arithmetic Error — How to Fix

Pointer arithmetic in C is only defined within arrays and one past the end. Common errors include comparing pointers from different allocations, arithmetic on void pointers (GCC extension), subtracting pointers of different types without proper casting, and dereferencing pointers beyond array bounds.

## Common Error Messages

- `Undefined behavior from pointer arithmetic outside array bounds`
- `Comparison of pointers from different allocations`
- `Arithmetic on void* is a GCC extension, not standard C`
- `Pointer subtraction type mismatch — wrong element size`

## How to Fix It

### Keep pointer arithmetic within array bounds

```c
#include <stdio.h>

int main(void) {
    int arr[5] = {10, 20, 30, 40, 50};
    int *p = arr;
    for (int i = 0; i < 5; i++)
        printf("arr[%d] = %d\n", i, *(p + i));
    return 0;
}
```

### Use proper types for pointer subtraction

```c
#include <stdio.h>

int main(void) {
    int arr[] = {1, 2, 3, 4, 5};
    int *start = &arr[0];
    int *end = &arr[4];
    ptrdiff_t diff = end - start;
    printf("Distance: %td\n", diff);
    return 0;
}
```

### Avoid void pointer arithmetic

```c
#include <stdio.h>
#include <stddef.h>

int main(void) {
    void *ptr = NULL;
    // WRONG: ptr + 1 on void*
    // CORRECT: use char* for byte arithmetic
    char *cptr = (char *)ptr + 10;
    printf("Offset: %td\n", (char *)cptr - (char *)ptr);
    return 0;
}
```

### Use array indexing instead of pointer arithmetic for clarity

```c
#include <stdio.h>

int main(void) {
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++)
        printf("arr[%d] = %d\n", i, arr[i]);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Comparing pointers from two different malloc calls

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Subtracting pointers of incompatible types

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Dereferencing a pointer one past the end of an array

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Only perform pointer arithmetic within a single array allocation
- **Tip 2:** Use ptrdiff_t for pointer subtraction results
- **Tip 3:** Prefer array indexing over pointer arithmetic for readability
