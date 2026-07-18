---
title: "[Solution] C realloc Error — How to Fix"
description: "Fix C realloc errors including NULL returns, memory leaks, and pointer invalidation. Learn safe realloc patterns."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C realloc Error — How to Fix

The `realloc` function can fail when the system cannot extend the existing memory block or allocate a new larger block. When `realloc` fails, it returns `NULL` but does not free the original pointer. A common mistake is assigning the result directly back to the original pointer, which causes a memory leak if `realloc` returns `NULL`. Additionally, using `realloc` on a pointer not obtained from `malloc`, `calloc`, or a previous `realloc` leads to undefined behavior.

## Common Error Messages

- `Segmentation fault after realloc returns NULL`
- `Memory leak when realloc result overwrites original pointer`
- `realloc: invalid pointer`
- `double free or corruption after realloc misuse`

## How to Fix It

### Use a temporary pointer for realloc results

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *arr = malloc(10 * sizeof(int));
    if (!arr) return 1;
    int *tmp = realloc(arr, 20 * sizeof(int));
    if (!tmp) {
        fprintf(stderr, "realloc failed\n");
        free(arr);
        return 1;
    }
    arr = tmp;
    free(arr);
    return 0;
}
```

### Never assign realloc directly to original pointer

```c
#include <stdlib.h>

int main(void) {
    int *p = malloc(10 * sizeof(int));
    int *tmp = realloc(p, 20 * sizeof(int));
    if (tmp) {
        p = tmp;
    }
    free(p);
    return 0;
}
```

### Check realloc size for overflow

```c
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

int main(void) {
    int *p = malloc(10 * sizeof(int));
    int *tmp = realloc(p, SIZE_MAX);
    if (!tmp) {
        fprintf(stderr, "realloc size overflow\n");
        free(p);
        return 1;
    }
    return 0;
}
```

### Use a safe_realloc wrapper

```c
#include <stdlib.h>
#include <string.h>

void *safe_realloc(void *ptr, size_t old_size, size_t new_size) {
    void *tmp = realloc(ptr, new_size);
    if (tmp && new_size > old_size) {
        memset((char *)tmp + old_size, 0, new_size - old_size);
    }
    return tmp;
}
```

## Common Scenarios

### Scenario 1: Growing a dynamic array without checking the realloc return value

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: A server reallocating buffer space under heavy load without error handling

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using realloc on stack-allocated or static memory

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always use a temporary pointer when calling realloc and check for NULL before assigning back
- **Tip 2:** Document the ownership semantics of buffers passed between functions that may call realloc
- **Tip 3:** Consider using a dynamic array library like kvec to avoid manual realloc logic
