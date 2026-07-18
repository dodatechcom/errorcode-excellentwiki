---
title: "[Solution] C sizeof Error — How to Fix"
description: "Fix C sizeof mistakes including sizeof pointer vs array and sizeof on expressions."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C sizeof Error — How to Fix

sizeof returns type size in bytes. Common errors include sizeof on pointer instead of array, forgetting padding, and arrays decaying to pointers. sizeof is compile-time for static types.

## Common Error Messages

- `sizeof returns pointer size instead of array size`
- `sizeof on expression gives unexpected result`
- `Array size wrong due to decayed pointer`
- `sizeof does not include struct padding`

## How to Fix It

### Use ARRAY_SIZE macro

```c
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))
void process(int *arr, size_t len) {
    printf("len=%zu (sizeof would give %zu)\n", len, sizeof(arr));
}
int main(void) {
    int arr[] = {1,2,3,4,5};
    process(arr, ARRAY_SIZE(arr));
    return 0;
}
```

### Use sizeof for allocation

```c
int arr[10];
int *copy = malloc(sizeof(arr));
if (!copy) return 1;
memcpy(copy, arr, sizeof(arr));
free(copy);
```

### Use sizeof for memset

```c
typedef struct { int x; int y; } Point;
Point p;
memset(&p, 0, sizeof(Point));
```

### Use sizeof for type portability

```c
#include <stdint.h>
printf("int32_t: %zu\n", sizeof(int32_t));
printf("int64_t: %zu\n", sizeof(int64_t));
```

## Common Scenarios

### Scenario 1: Using sizeof(ptr) instead of sizeof(*ptr)

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using sizeof inside function on array parameter

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Assuming sizeof(int) is always 4

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Use ARRAY_SIZE before array decays
- **Tip 2:** Use sizeof(type) for portable allocation
- **Tip 3:** sizeof is compile-time for static types
