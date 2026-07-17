---
title: "[Solution] C Out of memory: malloc failed"
description: "Fix C malloc failure. Handle memory allocation errors gracefully."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Out of memory: malloc failed

malloc returns NULL when the system cannot allocate the requested memory. Dereferencing this NULL pointer causes a segmentation fault.

## Common Causes

```c
// Cause 1: Requesting too much memory
int *huge = malloc(100000000000LL * sizeof(int));

// Cause 2: Memory leak exhaustion
while (1) {
    malloc(1024); // leaks memory
}

// Cause 3: Not checking return value
int *p = malloc(sizeof(int));
*p = 5; // crash if malloc returned NULL
```

## How to Fix

### Fix 1: Always check malloc return

```c
int *p = malloc(n * sizeof(int));
if (p == NULL) {
    perror("malloc");
    return 1;
}
```

### Fix 2: Validate size before allocation

```c
if (n > SIZE_MAX / sizeof(int)) {
    fprintf(stderr, "Size too large\n");
    return 1;
}
int *p = malloc(n * sizeof(int));
```

### Fix 3: Use calloc for zero-initialized memory

```c
int *arr = calloc(n, sizeof(int));
if (arr == NULL) {
    fprintf(stderr, "calloc failed\n");
    return 1;
}
```

## Examples

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t n = 1000;
    int *arr = malloc(n * sizeof(int));
    
    if (arr == NULL) {
        fprintf(stderr, "Failed to allocate %zu bytes\n", n * sizeof(int));
        return 1;
    }
    
    for (size_t i = 0; i < n; i++) {
        arr[i] = i;
    }
    
    free(arr);
    return 0;
}
```

## Related Errors

- [Memory leak]({{< relref "/languages/c/memory-leak-valgrind" >}}) — leaked memory.
- [Double free]({{< relref "/languages/c/double-free-heap.md" >}}) — heap corruption.
- [Heap corruption]({{< relref "/languages/c/heap-corruption" >}}) — heap damage.
