---
title: "[Solution] C NULL pointer dereference"
description: "Fix C NULL pointer dereference. Prevent crashes from null pointer access."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# NULL pointer dereference

A NULL pointer dereference occurs when a program attempts to access memory through a pointer that points to address 0 (NULL). This causes a segmentation fault.

## Common Causes

```c
// Cause 1: Dereferencing NULL directly
int *p = NULL;
*p = 10; // segfault

// Cause 2: Failed allocation
int *arr = malloc(100000000000LL);
*arr = 1; // segfault if malloc returned NULL

// Cause 3: Uninitialized pointer
struct Node *node;
node->next = NULL; // crash — node is garbage
```

## How to Fix

### Fix 1: Always check for NULL

```c
if (p != NULL) {
    *p = 10;
}
```

### Fix 2: Check malloc return

```c
int *arr = malloc(size);
if (arr == NULL) {
    perror("malloc");
    return 1;
}
```

### Fix 3: Initialize pointers to NULL

```c
int *ptr = NULL;
// Later set to valid address
ptr = &some_var;
```

## Examples

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *ptr = malloc(sizeof(int));
    if (ptr == NULL) {
        fprintf(stderr, "Out of memory\n");
        return 1;
    }
    
    *ptr = 42;
    printf("Value: %d\n", *ptr);
    
    free(ptr);
    ptr = NULL;
    
    return 0;
}
```

## Related Errors

- [Segfault at 0x0]({{< relref "/languages/c/segmentation-fault-0" >}}) — address 0x0 crash.
- [NULL pointer dereference]({{< relref "/languages/c/null-pointer-dereference" >}}) — detailed analysis.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — accessing freed memory.
