---
title: "[Solution] C Null Pointer Dereference Error — How to Fix"
description: "Fix C null pointer dereference crashes. Add null checks before dereferencing pointers from malloc and function returns."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Null Pointer Dereference Error — How to Fix

Dereferencing a NULL pointer causes a segmentation fault. This happens when malloc returns NULL due to memory exhaustion, when functions return NULL on error, or when pointers are not initialized. Null dereference is the most common cause of crashes in C programs.

## Common Error Messages

- `Segmentation fault (core dumped)`
- `NULL pointer dereference`
- `Attempt to dereference a null pointer`
- `Program received signal SIGSEGV`

## How to Fix It

### Check malloc return values

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(100 * sizeof(int));
    if (p == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }
    p[0] = 42;
    free(p);
    return 0;
}
```

### Validate pointers before use

```c
#include <stdio.h>

void process(int *data, size_t len) {
    if (data == NULL || len == 0) {
        fprintf(stderr, "Invalid input\n");
        return;
    }
    for (size_t i = 0; i < len; i++)
        printf("%d ", data[i]);
    printf("\n");
}

int main(void) {
    int arr[] = {1, 2, 3};
    process(arr, 3);
    process(NULL, 0);
    return 0;
}
```

### Initialize pointers to NULL

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = NULL;
    int *q = NULL;
    if (p != NULL) printf("%d\n", *p);
    else printf("p is NULL\n");
    free(p);
    free(q);
    return 0;
}
```

### Use a safe dereference macro

```c
#include <stdio.h>

#define SAFE_DEREF(ptr, default_val) ((ptr) ? *(ptr) : (default_val))

int main(void) {
    int x = 42;
    int *p = &x;
    int *q = NULL;
    printf("p: %d\n", SAFE_DEREF(p, 0));
    printf("q: %d\n", SAFE_DEREF(q, -1));
    return 0;
}
```

## Common Scenarios

### Scenario 1: malloc returns NULL due to memory exhaustion and the program dereferences it

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: A function returns NULL on error and the caller does not check

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: An uninitialized pointer is used before being assigned a valid address

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check malloc/calloc return values for NULL
- **Tip 2:** Initialize all pointers to NULL at declaration
- **Tip 3:** Use -fsanitize=undefined to detect null dereferences at runtime
