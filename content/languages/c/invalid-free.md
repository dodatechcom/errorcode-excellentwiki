---
title: "[Solution] C Invalid free: not a valid pointer"
description: "Fix C invalid free. Only free pointers returned by malloc, calloc, or realloc."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["invalid-free", "free", "malloc", "heap", "pointer"]
weight: 5
---

# Invalid free: not a valid pointer

An invalid free occurs when you call `free()` on a pointer that was not returned by `malloc()`, `calloc()`, or `realloc()`. This corrupts the heap and causes undefined behavior.

## Common Causes

```c
// Cause 1: Freeing stack memory
int x = 5;
free(&x); // invalid — x is on stack

// Cause 2: Freeing string literal
char *str = "hello";
free(str); // invalid — string literal

// Cause 3: Freeing already-freed pointer
int *p = malloc(sizeof(int));
free(p);
free(p); // invalid — double free

// Cause 4: Freeing non-heap pointer
int arr[10];
free(arr); // invalid — array on stack
```

## How to Fix

### Fix 1: Only free heap-allocated memory

```c
int *p = malloc(sizeof(int));
free(p); // valid
```

### Fix 2: Don't free string literals

```c
char *str = strdup("hello");
free(str); // valid — strdup allocates
```

### Fix 3: Set to NULL after free

```c
int *p = malloc(sizeof(int));
free(p);
p = NULL; // free(NULL) is safe
```

## Examples

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    // Valid: heap-allocated
    char *heap_str = strdup("hello");
    free(heap_str);
    
    // Invalid: stack memory
    // char stack_str[10] = "hello";
    // free(stack_str); // DON'T DO THIS
    
    // Invalid: string literal
    // char *lit = "hello";
    // free(lit); // DON'T DO THIS
    
    return 0;
}
```

## Related Errors

- [Double free]({{< relref "/languages/c/double-free-heap.md" >}}) — freeing twice.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — accessing freed memory.
- [Heap corruption]({{< relref "/languages/c/heap-corruption" >}}) — heap damage.
