---
title: "[Solution] C Array Decay Error — How to Fix"
description: "Fix C array decay issues where arrays lose size information when passed to functions. Preserve array dimensions."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Array Decay Error — How to Fix

In C, arrays decay to pointers when passed to functions, losing their size information. Common errors include using sizeof on a decayed array pointer (which gives pointer size, not array size), not passing the array size separately, and assuming the function knows the array length.

## Common Error Messages

- `sizeof returns pointer size instead of array size after decay`
- `Array size unknown inside function — missing length parameter`
- `Buffer overflow from unbounded array access in function`
- `Array decay causes unexpected pointer arithmetic`

## How to Fix It

### Pass array size as a separate parameter

```c
#include <stdio.h>

void print_array(const int *arr, size_t len) {
    for (size_t i = 0; i < len; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(void) {
    int arr[] = {1, 2, 3, 4, 5};
    print_array(arr, sizeof(arr) / sizeof(arr[0]));
    return 0;
}
```

### Use macros for array size

```c
#include <stdio.h>

#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))

void process(int *arr, size_t len) {
    for (size_t i = 0; i < len; i++)
        arr[i] *= 2;
}

int main(void) {
    int arr[] = {1, 2, 3, 4, 5};
    size_t len = ARRAY_SIZE(arr);
    process(arr, len);
    for (size_t i = 0; i < len; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```

### Use struct wrapper for arrays

```c
#include <stdio.h>

typedef struct {
    int data[5];
    size_t len;
} IntArray;

void print_array(const IntArray *a) {
    for (size_t i = 0; i < a->len; i++)
        printf("%d ", a->data[i]);
    printf("\n");
}

int main(void) {
    IntArray a = {{1, 2, 3, 4, 5}, 5};
    print_array(&a);
    return 0;
}
```

### Use sizeof before decay

```c
#include <stdio.h>

void fill(int *arr, size_t len, int value) {
    for (size_t i = 0; i < len; i++)
        arr[i] = value;
}

int main(void) {
    int arr[10];
    size_t len = sizeof(arr) / sizeof(arr[0]);
    fill(arr, len, 42);
    printf("First: %d, Last: %d\n", arr[0], arr[9]);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Using sizeof(arr) inside a function where arr is a parameter

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Forgetting to pass array length and accessing out of bounds

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using sizeof on a pointer received as a function argument

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always pass array length as a separate parameter to functions
- **Tip 2:** Use the ARRAY_SIZE macro before the array decays to a pointer
- **Tip 3:** Consider struct wrappers when arrays need to carry their size
