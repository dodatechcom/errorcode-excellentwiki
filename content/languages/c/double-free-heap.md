---
title: "[Solution] C Double free or corruption (fasttop)"
description: "Fix C double free or heap corruption. Prevent heap memory errors with proper allocation management."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["double-free", "heap-corruption", "glibc", "fasttop", "memory"]
weight: 5
---

# Double free or corruption (fasttop)

A double free occurs when you call `free()` on the same pointer twice. The heap manager detects the corruption and aborts the program with an error like "double free or corruption (fasttop)".

## Common Causes

```c
// Cause 1: Explicit double free
int *p = malloc(sizeof(int));
free(p);
free(p); // double free

// Cause 2: Free in conditional without NULL check
int *p = malloc(sizeof(int));
if (condition) {
    free(p);
}
free(p); // may double free if condition was true

// Cause 3: Use-after-free leading to double free
int *p = malloc(sizeof(int));
free(p);
*p = 10; // use-after-free
free(p); // double free
```

## How to Fix

### Fix 1: Set pointer to NULL after free

```c
int *p = malloc(sizeof(int));
free(p);
p = NULL; // safe — free(NULL) is a no-op
```

### Fix 2: Use a flag to track allocation

```c
int *p = malloc(sizeof(int));
int allocated = 1;
if (allocated) {
    free(p);
    allocated = 0;
}
```

### Fix 3: Check with Valgrind

```bash
gcc -g -o prog prog.c
valgrind --tool=memcheck --leak-check=full ./prog
```

## Examples

```c
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int *arr = malloc(5 * sizeof(int));
    if (!arr) return 1;
    
    // Use arr...
    
    free(arr);
    arr = NULL; // prevents double free
    
    // Later, safe to free again
    free(arr); // no-op
    
    return 0;
}
```

## Related Errors

- [Heap corruption detected]({{< relref "/languages/c/heap-corruption" >}}) — general heap corruption.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — accessing freed memory.
- [Invalid free]({{< relref "/languages/c/invalid-free" >}}) — freeing invalid pointer.
